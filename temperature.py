import pandas as pd
import matplotlib.pyplot as plt

class LineChart:
    def __init__(self, csv_path):
        """Read data from CSV file"""
        self.data = pd.read_csv(csv_path)
    
    def plot_temperature(self):
        """Create a line chart of temperature over days"""
        # Create the plot
        plt.figure(figsize=(10, 6))
        
        # Plot temperature line
        plt.plot(self.data['Day'], 
                self.data['Temperature'], 
                color='blue',
                marker='o',
                linestyle='-')
        
        # Add labels and title
        plt.title('Temperature Trend')
        plt.xlabel('Days')
        plt.ylabel('Temperature')
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        
        # Add grid
        plt.grid(True)
        
        # Adjust layout
        plt.tight_layout()
        
        # Show the plot
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create chart object
    chart = LineChart('temperature_data.csv')
    
    # Display the chart
    chart.plot_temperature()