import matplotlib.pyplot as plt

plt.xlabel("Number of iterations")
plt.ylabel(" Number of cities")
y_values = [10,35,210,431]
x_values=[10,15,20,25]
plt.title("Number of iterations vs Number of cities")
plt.plot(x_values,y_values)
plt.show()