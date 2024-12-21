# Import the necessary modules 
import matplotlib.pyplot as plt
import pandas as pd

# Load the data from CSV
data = pd.read_csv('superstore.csv')

# Check the first few rows of the dataframe to see what columns you have
print(data.head())

# Assuming you want to plot the sales or any other numerical data over categories (like 'Category' or 'Region')
# Example of selecting a category and its corresponding numerical data for the plot

# Let's assume 'Category' is in the first column and 'Sales' is in the second column.
# Modify this according to your actual CSV content.
X = list(data['Category'])  # Change 'Category' to whatever column you want for the X axis
Y = data.groupby('Category')['Sales'].sum()  # Summing sales by category, you can adjust this

# Plotting the data
plt.bar(Y.index, Y.values, color='g')
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

# Show the plot
plt.xticks(rotation=45)  # Rotate labels to avoid overlap if necessary
plt.show()


