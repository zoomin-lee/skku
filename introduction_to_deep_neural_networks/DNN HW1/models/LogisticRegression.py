import numpy as np
import matplotlib.pyplot as plt
import matplotlib

class LogisticRegression:
    def __init__(self, num_features):
        self.num_features = num_features
        self.W = np.random.rand(self.num_features, 1)

    def train(self, x, y, epochs, batch_size, lr, optim):
        loss = None   # loss of final epoch

        # Train should be done for 'epochs' times with minibatch size of 'batch size'
        # The function 'train' should return the loss of final epoch
        # Loss of an epoch is calculated as an average of minibatch losses
        # Weights are updated through the optimizer, not directly within 'train' function.

        # Tip : log computation may cause some error, so try to solve it by adding an epsilon(small value) within log term.
        epsilon = 1e-7

        # ========================= EDIT HERE ========================
        plt_loss = []
        plt_acc = []
        plt_list = [i for i in range(29,300,30)]

        w = self.W
        num = int(np.ceil(x.shape[0]/batch_size))

        for j in range(epochs):
            acc = 0
            minibatch_losses = 0
            for i in range(num):
                batch = np.random.choice(x.shape[0], batch_size, replace=False)
                minibatch_loss = 0
                wd = np.zeros_like(self.W)

                for batch_num in batch:
                    y_predicted = np.dot(x[batch_num], w)
                    y_predicted = LogisticRegression._sigmoid(self, y_predicted)

                    minibatch_loss -= (y[batch_num] * np.log(y_predicted + epsilon)
                             + (1 - y[batch_num])  * np.log(1 - y_predicted + epsilon)) / batch_size

                    wd += ((x[batch_num] * (y_predicted - y[batch_num])) / batch_size ).reshape(self.num_features, 1)

                    ############### plt 그릴때만 ###################
                    if j in plt_list :
                        y_predicted[y_predicted >= 0.5] = 1
                        y_predicted[y_predicted < 0.5] = 0
                        if y_predicted == y[batch_num]:
                            acc += 1
                    ##############################################

                minibatch_losses += minibatch_loss
                w = optim.update(w,wd,lr)
                self.W = w

            loss = minibatch_losses/num

        ################### plt 그릴때만 ###############################
            if j in plt_list:
                plt_loss.append(loss)
                plt_acc.append(acc/x.shape[0])

        plt.figure(1)
        plt.scatter(plt_list, plt_acc)
        plt.xticks(np.arange(0, 301, 30))
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.title("Epochs & Accuracy")
        plt.savefig('./batchsize'+str(batch_size)+'_epochs_accuracy.png')

        plt.figure(2)
        plt.scatter(plt_list, plt_loss)
        plt.xticks(np.arange(0, 301, 30))
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.title("Epochs & Loss")
        plt.savefig('./batchsize'+str(batch_size)+'_epochs_loss.png')
        plt.show()
        ##############################################################

        # ============================================================
        return loss

    def forward(self, x):
        threshold = 0.5
        y_predicted = None

        # Evaluation Function
        # Given the input 'x', the function should return prediction for 'x'
        # The model predicts the label as 1 if the probability is greater or equal to 'threshold'
        # Otherwise, it predicts as 0

        # ========================= EDIT HERE ========================
        y_predicted = np.dot(x, self.W)
        y_predicted = LogisticRegression._sigmoid(self, y_predicted)
        y_predicted[y_predicted >= 0.5] = 1
        y_predicted[y_predicted < 0.5] = 0
        # ============================================================

        return y_predicted

    def _sigmoid(self, x):
        sigmoid = None

        # Sigmoid Function
        # The function returns the sigmoid of 'x'

        # ========================= EDIT HERE ========================
        sigmoid = 1 / (1+np.exp(-x))
        # ============================================================
        return sigmoid
