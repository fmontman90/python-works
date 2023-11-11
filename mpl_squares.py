import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5] #X value
squares = [1, 4, 9, 16, 25] #Y value
#addition of scatterpoints on graph
plt.scatter(2, 4, s=200)
plt.scatter(3, 9, s=200)
plt.scatter(5, 25, s=200)
plt.plot(input_values, squares, linewidth=5)

#Set the chart and label axes
#setting the plot name and font size
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of the Value", fontsize=12)

#Set the size of tick labels
plt.tick_params(axis='both', labelsize=12)

plt.show()
