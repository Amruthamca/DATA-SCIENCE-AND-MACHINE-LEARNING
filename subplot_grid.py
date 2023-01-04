print("Amrutha Biju")
print("21mca003")
import matplotlib.pyplot as plt
x = ['Mon','Tue','Wed','Thurs','Fri']
y = [300,450,150,400,650]
plt.subplot(2,1,1)
plt.plot(x,y,linestyle='dotted',color='cyan',marker='h',markerfacecolor='magenta',markeredgecolor='black')
plt.xlabel('Days of weak')
plt.ylabel('Sales of Drink')
plt.title("Sales Data1")
plt.grid(color='blue',linestyle=':')

x = ['Mon','Tue','Wed','Thurs','Fri']
y = [400,500,350,300,500]
plt.subplot(2,1,2)
plt.plot(x,y,linestyle='dashed',color='yellow',marker='D',markerfacecolor='green',markeredgecolor='red')
plt.xlabel('Days of weak')
plt.ylabel('Sales of Food')
plt.title("Sales Data2")
plt.grid(color='blue',linestyle=':')
plt.show()


