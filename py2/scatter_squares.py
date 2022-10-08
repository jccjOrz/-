import matplotlib.pyplot as plt

plt.scatter(2, 4)
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
#plt.scatter(x_values, y_values, s=40)
plt.scatter(x_values, y_values, c=y_values,
            cmap=plt.cm.Blues, edgecolors='none', s=10)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
#plt.scatter(x_values, y_values, edgecolors='none', s=40)
#plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)
plt.savefig('square_plot.png', bbox_inches='tight')
plt.axes([0, 1100, 0, 1100000])
plt.show()
