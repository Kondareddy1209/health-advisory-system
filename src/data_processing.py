import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    # Remove duplicates
    data = data.drop_duplicates()

    # Fill missing values with forward fill
    data = data.ffill()

    return data

def visualize_data(data):
    # Visualize the average heart rate distribution
    if 'avg_heart_rate' in data.columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(data['avg_heart_rate'], kde=True, bins=30, color='blue')
        plt.title('Average Heart Rate Distribution')
        plt.xlabel('Average Heart Rate')
        plt.ylabel('Frequency')
        plt.show()

    # Filter numeric columns for correlation
    numeric_cols = data.select_dtypes(include=['float64', 'int64'])
    if not numeric_cols.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
        plt.title('Feature Correlation')
        plt.show()

def summarize_data(data):
    # Summarize key statistics
    return data.describe()
