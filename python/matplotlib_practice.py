import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np


xpoint= np.array([0,60])
ypoint=np.array([0,250])

plt.plot(xpoint,ypoint)
print(plt.show())