import numpy as np
import matplotlib.pyplot as plt
x =np.arange(0,11)
y = x^4+5
plt.plot(x,y)
plt.title("y = x^4+5")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
