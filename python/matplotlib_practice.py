import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

# Matplotlib Pyplot

xpoint= np.array([0,60])
ypoint=np.array([0,250])

plt.plot(xpoint,ypoint)
# print(plt.show())

# Matplotlib Plotting
# Draw a line in a diagram from position 
# (1, 3) to position (8, 10):

xpoint=np.array([1,8])
ypoint=np.array([3,10])

plt.plot(xpoint,ypoint)
print(plt.show)
