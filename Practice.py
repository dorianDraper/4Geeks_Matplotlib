import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

# Exercise 01 -  Create a scatter plot from the following vectors: x = [1, 2, 3, 4] and y = [1, 2, 0, 0.5]
print("Exercise 01 -  Create a scatter plot from the following vectors: x = [1, 2, 3, 4] and y = [1, 2, 0, 0.5]")
x = [1, 2, 3, 4]
y = [1, 2, 0, 0.5]

plt.figure(figsize=(10, 5))
plt.scatter(x, y)

plt.title('Scatter plot')
plt.show()

# Exercise 02 - Create a line plot from the following vectors: x = [1, 2, 3, 4] and y = [1, 2, 0, 0.5]
print("Exercise 02 - Create a line plot from the following vectors: x = [1, 2, 3, 4] and y = [1, 2, 0, 0.5]")
plt.figure(figsize=(10, 5))
plt.plot(x, y)

plt.title('Line plot')
plt.show()

# Exercise 03 - Create a histogram from a random array following a normal distribution N(2, 1.5)
print("Exercise 03 - Create a histogram from a random array following a normal distribution N(2, 1.5)")
np.random.seed(42) # Set the seed to 42 to get the same random numbers every time we run the code  
data = np.random.normal(2, 1.5, 1000) # Generate 1000 random numbers with mean 2 and standard deviation 1.5

plt.figure(figsize=(10, 5))

plt.hist(data, bins=30)
plt.title('Histogram')
plt.show()

# Exercise 04 - Create a DataFrame from the https://raw.githubusercontent.com/cvazquezlos/machine-learning-prework/main/04-matplotlib/assets/titanic_train.csv 
# and display the distribution of age and amount of tickets 
print("Exercise 04 - Create a DataFrame from the https://raw.githubusercontent.com/cvazquezlos/machine-learning-prework/main/04-matplotlib/assets/titanic_train.csv")
df = pd.read_csv('https://raw.githubusercontent.com/cvazquezlos/machine-learning-prework/main/04-matplotlib/assets/titanic_train.csv')
print(df)
fig, axis = plt.subplots(2, 1, figsize=(10, 10)) # Create a figure with 2 subplots (2 rows and 1 column) 
axis[0].hist(df['Age'], bins=30) # Plot the histogram of the 'Age' column in the first subplot 
axis[0].set_title('Age') # Set the title of the first subplot
axis[1].hist(df['Fare'], bins=15) # Plot the histogram of the 'Fare' column in the second subplot
axis[1].set_title('Fare') # Set the title of the second subplot

plt.tight_layout() # To avoid overlapping between subplots 
plt.show()