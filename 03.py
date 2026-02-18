import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,4*np.pi,1000)
y = np.sin(x)
y2= np.cos(x)

plt.figure(figsize=(10,6))
plt.plot(x,y,'b-',label='sin(x)')
plt.plot(x,y2,'g--',label='cos(x)')


plt.title("Sine Wave function")
plt.xlabel("Angle(Radius)")
plt.ylabel("Aplitude")
plt.grid(True ,linestyle="--",alpha=0.7)
plt.axhline(0,color='black',linewidth=1)
plt.legend()
plt.savefig("fig1.pdf")

plt.show()