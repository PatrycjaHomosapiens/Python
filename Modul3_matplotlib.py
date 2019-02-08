import matplotlib.pyplot as plt

dane = [12, 20,30,40,30,20,100,80,90,11,22,55,44,33,88]
dane2 = [1,2,3,4,3,2,10,8,110,220,505,440,330,808]

plt.plot(dane, label="Dane testowe 1")
plt.plot(dane2, label="Dane testowe 2")
plt.grid(color='lightblue', linestyle='-.', linewidth=0.6)
plt.legend()
plt.savefig('output.png', dpi=300)
plt.show()


