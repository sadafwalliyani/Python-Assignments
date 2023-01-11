import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np

# Matplotlib Pyplot

# xpoint= np.array([0,60])
# ypoint=np.array([0,250])

# plt.plot(xpoint,ypoint)
# print(plt.show())

# # Matplotlib Plotting
# # Draw a line in a diagram from position 
# # (1, 3) to position (8, 10):
# xpoints= np.array([1,8])
# ypoints= np.array([3,10])

# plt.plot(xpoints,ypoints)
# print(plt.show())

# Draw two points in the diagram, one 
# at position (1, 3) and one in position (8, 10):

xpoin= np.array([1,8])
ypoin=np.array([3,10])
plt.plot(xpoin,ypoin, 'o')
print(plt.show())