print("Amrutha Biju")
print("21mca003")

import matplotlib.pyplot as plt
x = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']
y = [173,153,195,147,120,144,148,109,174,130,172,131]
plt.title('Sales Data')
plt.xlabel('Month of Years',fontsize=18)
plt.scatter(x,y,color='pink')

x = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']
y = [189,189,105,112,173,109,151,197,174,145,177,161]
plt.scatter(x,y,color='yellow')

x = ['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sep','Oct','Nov','Dec']
y = [185,185,126,134,196,153,112,133,200,145,167,110]
plt.scatter(x,y,color='blue')
plt.show()






