import pandas as pd
import matplotlib.pyplot as plt

class StackedBarChart:
    def __init__(self, csv_path):
        """
        Initialize with path to CSV file containing Region, Category, and Sales columns
        """
        self.data = pd.read_csv(csv_path)
        
        # Verify the required columns exist
        required_columns = {'Region', 'Category', 'Sales'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"CSV file missing required columns: {missing}")
    
    def plot_sales_by_category(self, figsize=(10, 6), colors=None):
        """
        Create a stacked bar chart showing sales by category for each region
        
        Parameters:
        figsize: tuple of (width, height) for the plot
        colors: optional list of colors for different categories
        """
        # Pivot the data to get it in the right format for stacking
        pivoted_data = self.data.pivot(index='Region', columns='Category', values='Sales')
        
        # Create the stacked bar chart
        ax = pivoted_data.plot(
            kind='bar', 
            stacked=True, 
            figsize=figsize,
            color=colors
        )
        
        # Customize the chart
        plt.title('Sales by Region and Category')
        plt.xlabel('Region')
        plt.ylabel('Sales')
        plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        
        # Add value labels on the bars
        for c in ax.containers:
            ax.bar_label(c, label_type='center')
            
        return plt.gcf()
    
    def get_summary_stats(self):
        """
        Return summary statistics of the sales data
        """
        summary = {
            'total_sales': self.data['Sales'].sum(),
            'sales_by_region': self.data.groupby('Region')['Sales'].sum(),
            'sales_by_category': self.data.groupby('Category')['Sales'].sum()
        }
        return summary

# Example usage
if __name__ == "__main__":
    # Create chart from CSV
    chart = StackedBarChart('sales_data.csv')
    
    # Optional: customize colors
    custom_colors = ['#FF9999', '#66B2FF', '#99FF99']
    
    # Create and display the chart
    fig = chart.plot_sales_by_category(colors=custom_colors)
    plt.show()
    
    # Print summary statistics
    stats = chart.get_summary_stats()
    print("\nSummary Statistics:")
    print(f"Total Sales: {stats['total_sales']:,.2f}")
    print("\nSales by Region:")
    print(stats['sales_by_region'])
    print("\nSales by Category:")
    print(stats['sales_by_category'])