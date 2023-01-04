print("Amrutha Biju")
print("21mca003")
import matplotlib.pyplot as plt
import numpy as np
data={'Walking': 29,'Cycling': 15,'Car':35,'Bus':18,'Train':3}
transport=list(data.keys())
frequency = list(data.values())

fig = plt.figure(figsize = (10, 5))
plt.bar(transport, frequency, color ='green', width = 0.1)
plt.xlabel("Mode of Transport")
plt.ylabel("Frequency")
plt.title("Transport Facilities")
plt.show()
