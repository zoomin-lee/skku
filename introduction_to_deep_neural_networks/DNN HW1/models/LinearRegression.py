import numpy as np

class LinearRegression:
    def __init__(self, num_features):
        self.num_features = num_features
        self.W = np.zeros((self.num_features, 1))

    def train(self, x, y, epochs, batch_size, lr, optim):
        final_loss = None   # loss of final epoch

        # Train should be done for 'epochs' times with minibatch size of 'batch_size'
        # The function 'train' should return the loss of final epoch
        # Loss of an epoch is calculated as an average of minibatch losses
        # Weights are updated through the optimizer, not directly within 'train' function.

        # ========================= EDIT HERE ========================

        w = self.W
        num = int(np.ceil(x.shape[0]/batch_size))

        for j in range(epochs):
            minibatch_losses = 0
            for i in range(num):

                batch = np.random.choice(x.shape[0], batch_size, replace=False)
                minibatch_loss = 0
                wd = np.zeros_like(self.W)

                for batch_num in batch:
                    y_predicted = self.forward(x[batch_num])

                    minibatch_loss += (y_predicted - y[batch_num])**2 / batch_size
                    wd += ( (2 * x[batch_num] * (y_predicted - y[batch_num]))/ batch_size ).reshape(self.num_features, 1)

                minibatch_losses += minibatch_loss
                w = optim.update(w, wd, lr)
                self.W = w

            final_loss = minibatch_losses / num
        # ============================================================
        return final_loss

    def forward(self, x):
        y_predicted = None

        # Evaluation Function
        # Given the input 'x', the function should return prediction for 'x'

        # ========================= EDIT HERE ========================
        y_predicted = np.dot(x, self.W)
        # ============================================================
        return y_predicted
