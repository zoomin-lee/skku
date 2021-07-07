import numpy as np
import matplotlib.pyplot as plt

plt2 = [i for i in range(0,301,30)]
plt_loss = [i for i in range(30)]

plt.scatter(plt2, plt_loss)
plt.xticks(np.arange(0, 301, 30))
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title("Epochs & Accuracy")
plt.show()