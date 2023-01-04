print("Amrutha Biju")
print("21mca003")
from matplotlib import pyplot as plt
import numpy as np
x = np.array([2001,2002,2003,2004,2005,2006,2007])
y = np.array([24000,22500,19700,17500,14500,10000,5800])
plt.plot(x,y)
plt.xlabel("year")
plt.ylabel("car value")
plt.title("Value Description",loc='left')
plt.plot(x,y,linestyle='dashed',color='r',marker='*',markersize='20',markerfacecolor='green')
plt.show()
