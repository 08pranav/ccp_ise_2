import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

class BoxPlot:
    def __init__(self, csv_path):
        """
        Initialize with path to CSV file containing House Type and Price columns
        """
        self.data = pd.read_csv(csv_path)
        
        # Verify the required columns exist
        required_columns = {'House Type', 'Price'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"CSV file missing required columns: {missing}")
    
    def plot_price_distribution(self, figsize=(12, 6), palette='Set2'):
        """
        Create a box plot showing price distribution by house type
        
        Parameters:
        figsize: tuple of (width, height) for the plot
        palette: color palette for different house types
        """
        plt.figure(figsize=figsize)
        
        # Create the box plot
        ax = sns.boxplot(x='House Type', 
                        y='Price',
                        data=self.data,
                        palette=palette)
        
        # Customize the plot
        plt.title('Price Distribution by House Type', pad=20)
        plt.xlabel('House Type')
        plt.ylabel('Price')
        
        # Rotate x-axis labels if there are many house types
        if len(self.data['House Type'].unique()) > 4:
            plt.xticks(rotation=45)
        
        # Add price statistics as text
        stats_text = self.get_statistics_text()
        plt.figtext(1.02, 0.5, stats_text, 
                   bbox=dict(facecolor='white', alpha=0.8),
                   fontsize=9, va='center')
        
        plt.tight_layout()
        return plt.gcf()
    
    def get_statistics_text(self):
        """
        Generate statistical summary for each house type
        """
        stats_text = "Price Statistics:\n\n"
        
        for house_type in sorted(self.data['House Type'].unique()):
            prices = self.data[self.data['House Type'] == house_type]['Price']
            stats_text += f"{house_type}:\n"
            stats_text += f"Median: ${prices.median():,.0f}\n"
            stats_text += f"Mean: ${prices.mean():,.0f}\n"
            stats_text += f"Std Dev: ${prices.std():,.0f}\n"
            
            # Calculate outliers
            Q1 = prices.quantile(0.25)
            Q3 = prices.quantile(0.75)
            IQR = Q3 - Q1
            outliers = prices[(prices < (Q1 - 1.5 * IQR)) | (prices > (Q3 + 1.5 * IQR))]
            stats_text += f"Outliers: {len(outliers)}\n\n"
        
        return stats_text
    
    def perform_anova(self):
        """
        Perform one-way ANOVA test to compare price distributions
        """
        house_types = self.data['House Type'].unique()
        price_groups = [self.data[self.data['House Type'] == ht]['Price'] 
                       for ht in house_types]
        
        f_statistic, p_value = stats.f_oneway(*price_groups)
        return {
            'f_statistic': f_statistic,
            'p_value': p_value
        }

# Example usage
if __name__ == "__main__":
    # Create and display the box plot
    plot = BoxPlot('house_prices.csv')
    
    # Create the visualization
    fig = plot.plot_price_distribution()
    
    # Perform statistical analysis
    anova_results = plot.perform_anova()
    print("\nOne-way ANOVA Test Results:")
    print(f"F-statistic: {anova_results['f_statistic']:.2f}")
    print(f"P-value: {anova_results['p_value']:.4f}")
    
    plt.show()