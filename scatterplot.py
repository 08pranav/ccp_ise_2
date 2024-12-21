import os
import pandas as pd
import matplotlib.pyplot as plt

class ScatterPlot:
    def __init__(self, csv_file):

        
        self.data = pd.read_csv(csv_file)
    
    def plot_scores(self, title='Study Hours vs Scores', 
                    x_label='Hours Studied', 
                    y_label='Scores Obtained',
                    color='red', 
                    marker='o'):

        plt.figure(figsize=(10, 6))
        
        
        plt.scatter(self.data['Hours'], self.data['Scores'], 
                    color=color, marker=marker)
        
        
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        
        plt.grid(True, linestyle='--', alpha=0.7)
        
        correlation = self.data['Hours'].corr(self.data['Scores'])
        
        plt.annotate(f'Correlation: {correlation:.2f}', 
                     xy=(0.05, 0.95), 
                     xycoords='axes fraction')

        plt.tight_layout()
        plt.show()
        return correlation


if __name__ == '__main__':
    
    file_path = r'Hours and Scores.csv'
    scatter = ScatterPlot(file_path)
    correlation = scatter.plot_scores()
    print(f"Correlation coefficient: {correlation}")