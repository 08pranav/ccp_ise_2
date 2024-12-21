import pandas as pd
import matplotlib.pyplot as plt

class ExamScoreHistogram:
    def __init__(self, data):
        """
        Initialize the histogram with exam data
        
        Parameters:
        data (pandas.DataFrame): DataFrame containing exam score data
        """
        self.data = data
    
    def plot_scores_distribution(self, exam_subject, grade_column='Score'):
        """
        Create a histogram of exam scores for a specific subject
        
        Parameters:
        exam_subject (str): The specific exam subject to analyze
        grade_column (str, optional): The column containing scores. Defaults to 'Score'.
        """
        # Filter data for the specific exam subject
        subject_data = self.data[self.data['Exam Subject'] == exam_subject]
        
        # Remove 'All' and 'Average' rows
        subject_data = subject_data[~subject_data[grade_column].isin(['All', 'Average'])]
        
        # Convert scores to numeric, handling any potential string conversions
        subject_data[grade_column] = pd.to_numeric(subject_data[grade_column], errors='coerce')
        
        # Create the histogram
        plt.figure(figsize=(10, 6))
        plt.hist(subject_data[grade_column], bins=5, range=(1, 5), 
                 color='green', edgecolor='black')
        
        # Customize the plot
        plt.title(f'{exam_subject} Exam Scores Distribution')
        plt.xlabel('Scores (1-5)')
        plt.ylabel('Frequency')
        plt.xticks(range(1, 6))
        
        plt.tight_layout()
        plt.show()
    
    def analyze_exam_performance(self, exam_subject):
        """
        Provide a summary of exam performance for a specific subject
        
        Parameters:
        exam_subject (str): The specific exam subject to analyze
        
        Returns:
        dict: A summary of exam performance metrics
        """
        # Filter data for the specific exam subject
        subject_data = self.data[self.data['Exam Subject'] == exam_subject]
        
        # Remove 'All' and 'Average' rows
        subject_data = subject_data[~subject_data['Score'].isin(['All', 'Average'])]
        
        # Convert scores to numeric
        subject_data['Score'] = pd.to_numeric(subject_data['Score'], errors='coerce')
        
        # Calculate performance metrics
        performance_summary = {
            'Total Students': subject_data['Students (All Students (2016))'].sum(),
            'Score Distribution': subject_data.groupby('Score')['Students (All Students (2016))'].sum().to_dict(),
            'Pass Rate (Score 3+)': (subject_data[subject_data['Score'] >= 0]['Students (All Students (2016))'].sum() / 
                                     subject_data['Students (All Students (2016))'].sum() * 100)
        }
        
        return performance_summary

# Example usage
def main():
    # Read the CSV file
    df = pd.read_csv('exams.csv')
    
    # Create histogram object
    histogram = ExamScoreHistogram(df)
    
    # Plot scores distribution for a specific exam
    histogram.plot_scores_distribution('CALCULUS AB')
    
    # Analyze exam performance
    performance = histogram.analyze_exam_performance('CALCULUS AB')
    print(performance)

if __name__ == '__main__':
    main()