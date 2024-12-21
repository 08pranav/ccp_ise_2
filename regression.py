import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class RegressionPlot:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)
        print("Dataset Columns:", self.data.columns)
        print(self.data.head())  # Inspect the first few rows to verify column names

    def plot_price_prediction(self):
        plt.figure(figsize=(10, 8))
        sns.set(style="whitegrid")  # Set Seaborn style for better aesthetics
        try:
            sns.regplot(x='SquareFeet', y='Price', data=self.data, color='blue', line_kws={'color': 'red', 'linewidth': 2})
            plt.xlabel('Square Feet', fontsize=14)
            plt.ylabel('Price', fontsize=14)
            plt.title('Regression Plot of Price vs Square Feet', fontsize=16)
            plt.show()
        except ValueError as e:
            print(f"Error: {e}")
            print("Please check that 'SquareFeet' and 'Price' are valid column names in your dataset.")

# Example usage for RegressionPlot
file_path_regression = r'housing_price_dataset.csv'  # Adjust the file name as needed
regression_plot = RegressionPlot(file_path_regression)
regression_plot.plot_price_prediction()
