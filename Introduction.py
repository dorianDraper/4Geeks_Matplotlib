import numpy as np
import matplotlib.pyplot as plt

# Example 1 - Line plot 1
x = np.linspace(0, 10, 100) # 100 evenly-spaced values from 0 to 10 (inclusive) 
plt.plot(x, np.sin(x)) # Plot the sine of each x point 
plt.plot(x, np.cos(x)) # Plot the cosine of each x point
plt.show() # Display the plot
# Example 2 - Line plot 2
X = np.linspace(0, 10, 100)
y = np.sin(X) # Sine of X
z = np.cos(X) # Cosine of X 

plt.figure(figsize=(10, 5)) # Set the size of the figure to 10 inches wide by 5 inches tall 
plt.plot(X, y, label='Sen X') # Plot the sine of each X point 
plt.plot(X, z, label='Cos X') # Plot the cosine of each X point
plt.title('Line plot') # Add a title to the plot
plt.legend() # Add a legend
plt.show() # Display the plot

# Example 3 - Scatter plot
plt.figure(figsize=(10, 5)) 
plt.scatter(X, y, label='Sen X')  # Plot the sine of each X point

plt.title('Scatter plot') 
plt.legend() 
plt.show()

# Example 4 - Histogram
data = np.random.randn(1000) # Generate 1000 random numbers

plt.figure(figsize=(10, 5))

plt.hist(data, bins=30) # Plot a histogram with 30 bins 
plt.title('Histogram')
plt.show()

# Example 5 - Bar plot
labels = ['A', 'B', 'C', 'D', 'E'] # Labels for each bar
values = [10, 20, 15, 30, 40] # Values for each bar

plt.figure(figsize=(10, 5))

plt.bar(labels, values) # Plot the values as a bar chart
plt.title('Bar plot')
plt.show()

# Example 6 - Pie chart
labels = ['A', 'B', 'C', 'D', 'E'] # Labels for each slice
sizes = [10, 20, 15, 30, 40] # Values for each slice

plt.figure(figsize=(7, 7)) 
plt.pie(sizes, labels=labels) # Plot the values as a pie chart
plt.title('Pie chart')
plt.show()

# Example 7 - Box plot
data = np.random.randn(1000) # Generate 1000 random numbers

plt.figure(figsize=(10, 5))

plt.boxplot(data) # Plot the values as a box plot
plt.title('Box plot')
plt.show()


