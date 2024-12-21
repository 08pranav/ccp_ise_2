import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class Heatmap:
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path)

    def plot_correlation(self):
        plt.figure(figsize=(10, 8))
        sns.heatmap(self.data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Heatmap')
        plt.show()

# Example usage for Heatmap
file_path = r'results.csv'  # Adjust the file name as needed
heatmap = Heatmap(file_path)
heatmap.plot_correlation()
