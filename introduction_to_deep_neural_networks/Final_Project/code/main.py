import numpy as np
import pandas as pd

from dataset import SSL_Dataset
from model import CNN
from utils import save_prediction, plot_accuracy

import torch
from torch.utils.data import DataLoader
import torch.optim as optim
import torch.nn.functional as F
from torchvision import transforms
import torchvision.models as models
import torch.nn as nn
from time import time
from efficientnet_pytorch import EfficientNet

"""
Please use this code as a guideline. 
Feel free to create your own code for training, testing, ... etc.
But for creating "submission.csv" file, utilizing this code is highly recommended.
"""


class Trainer:
    def __init__(self, model, device, weight_path, model_name, patience, momentum, weight_decay, learning_rate,
                 num_epoch, print_every):

        self.patience = patience
        self.momentum = momentum
        self.weight_decay = weight_decay
        self.lr = learning_rate
        self.num_epoch = num_epoch
        self.print_every = print_every

        self.best_acc = 0
        self.best_epoch = 0
        self.crnt_epoch = 0
        self.endure = 0
        self.stop_flag = False
        self.num_class = 10
        self.device = device
        self.weight_path = weight_path
        self.model_name = model_name

        self.model = model
        self.loss_fn = nn.CrossEntropyLoss()
        self.optimizer = optim.SGD(self.model.parameters(), lr=self.lr, momentum=self.momentum,
                                   weight_decay=self.weight_decay)

        self.train_acc = []
        self.valid_acc = []

    # test
    def _test(self, mode, data_loader):
        test_preds = []
        self.model.eval()
        correct = 0
        total = 0

        if mode == 'Valid':
            with torch.no_grad():
                for batch_data in data_loader:
                    batch_x, batch_y = batch_data
                    inputs, targets = batch_x.to(self.device), batch_y.to(self.device)

                    outputs = self.model(inputs)
                    _, predicted = torch.max(outputs, 1)

                    total += targets.size(0)
                    correct += predicted.eq(targets).cpu().sum().item()
                    if self.device == 'cuda':
                        test_preds += predicted.detach().cpu().numpy().tolist()
                    else:
                        test_preds += predicted.detach().numpy().tolist()

            total_acc = correct / total

            print("| \033[31m%s Epoch #%d\t Accuracy: %.2f%%\033[0m" % (mode, self.crnt_epoch + 1, 100. * total_acc))
            if self.crnt_epoch % self.print_every == 0:
                self.valid_acc.append(total_acc)
            if self.best_acc < total_acc:
                print('| \033[32mBest Accuracy updated (%.2f => %.2f)\033[0m\n' % (
                100. * self.best_acc, 100. * total_acc))
                self.best_acc = total_acc
                self.best_epoch = self.crnt_epoch
                self.endure = 0
                # Save best model
                torch.save(self.model.state_dict(), self.weight_path + self.model_name)
            else:
                self.endure += 1
                print(f'| Endure {self.endure} out of {self.patience}\n')
                if self.endure >= self.patience:
                    print('Early stop triggered...!')
                    self.stop_flag = True

        if mode == 'Test':
            print('Predicting Starts...')
            with torch.no_grad():
                for batch_data in data_loader:
                    batch_x = batch_data
                    inputs = batch_x.to(self.device)

                    outputs = self.model(inputs)
                    _, predicted = torch.max(outputs, 1)
                    if self.device == 'cuda':
                        test_preds += predicted.detach().cpu().numpy().tolist()
                    else:
                        test_preds += predicted.detach().numpy().tolist()

            return test_preds, self.crnt_epoch, self.train_acc, self.valid_acc

    # train
    def _train(self, labeled_trainloader, labeled_validloader):
        self.model.train()
        print('Training Starts...')
        total = 0
        correct = 0
        for epoch in range(self.num_epoch):
            self.crnt_epoch = epoch
            for batch_data in labeled_trainloader:
                batch_x, batch_y = batch_data
                batch_size = batch_x.size(0)
                batch_y = torch.zeros(batch_size, self.num_class).scatter_(1, batch_y.view(-1, 1), 1)
                inputs_l, targets_l = batch_x.to(self.device), batch_y.long().to(self.device)

                outputs = self.model(inputs_l)
                loss = self.loss_fn(outputs, torch.argmax(targets_l, dim=-1))

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                print(f"Epoch: {epoch + 1}, Loss:{loss:.4f}")

                _, predicted = torch.max(outputs, 1)

                total += targets_l.size(0)
                correct += predicted.eq(torch.argmax(targets_l, dim=-1)).cpu().sum().item()

            total_acc = correct / total
            if self.crnt_epoch % self.print_every == 0:
                self.train_acc.append(total_acc)
            print("\n| \033[31mTrain Epoch #%d\t Accuracy: %.2f%%\033[0m" % (self.crnt_epoch + 1, 100. * total_acc))
            pred = self._test("Valid", labeled_validloader)
            if self.stop_flag: break
        print('Training Finished...!!')

    #################### EDIT HERE ####################

    # pseudo_label
    def _pseudo_label(self, train_unlabeled_dataset, train_batch):
        print("Pseudo Labeling Starts")
        threshold_datas = []
        threshold_labels = []
        threshold_names = []
        name_and_labels = []
        self.model.eval()
        correct = 0
        total = 0

        cnt = 0
        len1 = 0
        len2 = 0
        names = train_unlabeled_dataset.data
        unlabeled_trainloader = DataLoader(train_unlabeled_dataset, train_batch)

        with torch.no_grad():
            for batch_data in unlabeled_trainloader:
                threshold_data = None
                threshold_label = None
                mask = []

                threshold_name = None
                if cnt == 0:
                    len1 = len(batch_data)
                    len2 = len(batch_data)
                if cnt == len(names) // train_batch:
                    len2 = len(batch_data)
                batch_name = names[cnt * len1: cnt * len1 + len2]
                cnt += 1

                batch_x = batch_data
                batch_size = batch_x.size(0)
                inputs = batch_x.to(self.device)

                outputs = self.model(inputs)
                exp_outputs = torch.exp(outputs)
                sum_exp_outputs = torch.sum(exp_outputs, axis=1).reshape(batch_size, 1)
                softmax_outputs = exp_outputs / sum_exp_outputs

                softmax_outputs_square = torch.pow(softmax_outputs, 2)
                softmax_outputs_square_sum = torch.sum(softmax_outputs_square, axis=1).reshape(batch_size, 1)
                sharpening_outputs = softmax_outputs_square / softmax_outputs_square_sum

                for i in range(len(sharpening_outputs)):
                    idx = torch.argmax(sharpening_outputs[i])
                    if sharpening_outputs[i][idx] > 0.8:
                        mask.append(i)

                _, predicted = torch.max(sharpening_outputs, 1)
                threshold_label = [int(predicted[i]) for i in mask]
                threshold_name = [batch_name[i] for i in mask]

                threshold_labels.append(threshold_label)
                threshold_names.append(threshold_name)

        threshold_labels = sum(threshold_labels, [])
        threshold_names = sum(threshold_names, [])
        print("Pseudo Labeling Finish")
        for i in range(len(threshold_names)):
            name_and_label = str(threshold_names[i]) + ' ' + str(threshold_labels[i]) + '\n'
            name_and_labels.append(name_and_label)

        with open('/content/kaggle_data/annotation/over_threshold_name_list.txt', 'w') as f:
            f.writelines(name_and_labels)
    ###################################################


def main():
    #################### EDIT HERE ####################
    """
    You can change any values of hyper-parameter below.
    *test_only: If this parameter is True, you can just test with a model that already exists without training step.
    (for your time saving..!)
    """
    random_seed = 1

    patience = 10
    momentum = 0.9
    weight_decay = 5e-4
    learning_rate = 0.005

    num_epoch = 30
    print_every = 1
    train_batch = 512
    test_batch = 1000
    valid_ratio = 0.1

    model_name = 'my_model.p'

    test_only = False
    ###################################################

    np.random.seed(random_seed)
    torch.manual_seed(random_seed)

    if torch.cuda.is_available():
        device = 'cuda'
        torch.cuda.manual_seed_all(random_seed)
        torch.backends.cudnn.deterministic = True
    else:
        device = 'cpu'

    weight_path = './best_model/'

    transform = transforms.Compose([
        transforms.Resize(size=(32, 32)),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    train_examples = SSL_Dataset(root='../', transform=transform, mode='labeled_train')
    num_train = len(train_examples)
    num_valid = int(num_train * valid_ratio)
    train_labeled_dataset, valid_labeled_dataset = torch.utils.data.random_split(train_examples,
                                                                                 [num_train - num_valid, num_valid])
    train_unlabeled_dataset = SSL_Dataset(root='../', transform=transform, mode='unlabeled_train')
    test_labeled_dataset = SSL_Dataset(root='../', transform=transform, mode="test")
    test_idx = test_labeled_dataset.idx

    labeled_trainloader = DataLoader(train_labeled_dataset, batch_size=train_batch, shuffle=True)
    labeled_validloader = DataLoader(valid_labeled_dataset, batch_size=test_batch, shuffle=False)
    labeled_testloader = DataLoader(test_labeled_dataset, batch_size=test_batch, shuffle=False)
    #################### EDIT HERE ####################

    model = EfficientNet.from_pretrained('efficientnet-b3').to(device)
    feature = model._fc.in_features
    model._fc = nn.Linear(in_features=feature, out_features=10, bias=True).to(device)

    ###################################################

    trainer = Trainer(model, device, weight_path, model_name, patience, momentum, weight_decay, learning_rate,
                      num_epoch, print_every)

    if test_only == False:
        print(f"# Train data: {len(train_labeled_dataset)}, # Valid data: {len(valid_labeled_dataset)}")
        train_start = time()
        trainer._train(labeled_trainloader, labeled_validloader)
        train_elapsed = time() - train_start
        print('Train Time: %.4f\n' % train_elapsed)

    #################### EDIT HERE ####################
    trainer._pseudo_label(train_unlabeled_dataset, train_batch)
    pseudo_data = SSL_Dataset(root='../', transform=transform, mode='pseudo_train')
    num_train = len(pseudo_data)
    num_valid = int(num_train * 0.25)
    train_pseudo_dataset, valid_pseudo_dataset = torch.utils.data.random_split(pseudo_data,
                                                                               [num_train - num_valid, num_valid])

    pseudo_trainloader = DataLoader(train_pseudo_dataset, batch_size=train_batch, shuffle=True)
    pseudo_validloader = DataLoader(valid_pseudo_dataset, batch_size=test_batch, shuffle=False)

    model.load_state_dict(torch.load(weight_path + model_name))
    # for n, p in model.named_parameters():
    #     if '_fc' not in n:
    #         p.requires_grad = False

    if test_only == False:
        print(f"# Pseudo Train data: {len(train_pseudo_dataset)}, # Pseudo Valid data: {len(valid_pseudo_dataset)}")
        train_start = time()
        trainer._train(pseudo_trainloader, pseudo_validloader)
        train_elapsed = time() - train_start
        print('Train Time: %.4f\n' % train_elapsed)
    ###################################################

    print(f"# Test data: {len(test_labeled_dataset)}")
    model.load_state_dict(torch.load(weight_path + model_name))
    pred, num_epochs, train_acc, valid_acc = trainer._test("Test", labeled_testloader)
    save_prediction(weight_path, pred, test_idx)


if __name__ == "__main__":
    main()