import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class PairPlot:
    def __init__(self, dataset_path):
        """
        Initialize the PairPlot with a dataset path
        
        Parameters:
        -----------
        dataset_path : str
            Full path to the CSV file containing the Iris dataset
        """
        self.dataset = pd.read_csv(dataset_path)
    
    def plot_relationships(self, save_path=None):
        """
        Create a pairplot of the dataset, colored by species
        
        Parameters:
        -----------
        save_path : str, optional
            Full path where the plot should be saved
        """
        # Create the pairplot
        plt.figure(figsize=(12, 10))
        plot = sns.pairplot(self.dataset, hue='species', 
                            plot_kws={'alpha': 0.7},  # slight transparency
                            diag_kws={'alpha': 0.7},  # for histogram
                            height=2.5)  # size of each subplot
        
        # Set a title
        plot.fig.suptitle('Iris Dataset - Pairwise Relationships', y=1.02)
        
        # Adjust layout
        plt.tight_layout()
        
        # Save the plot if a path is provided
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        # Show the plot
        plt.show()

# Example usage
if __name__ == '__main__':
    # Replace with the actual path to your IRIS.csv file
    dataset_path = r'IRIS.csv'
    
    # Create PairPlot instance
    iris_plot = PairPlot(dataset_path)
    
    # Generate the pairplot
    iris_plot.plot_relationships(
        save_path=r'iris_pairplot.png'
    )