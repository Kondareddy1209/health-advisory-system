import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from anomaly_detection import detect_anomalies
from parallel_processing import process_row

# Load the CSV file
file_path = 'C:\Users\Konda Reddy\Desktop\heart\health_fitness_dataset.csv'  # Update with the actual file path
data = pd.read_csv(file_path)

# Display basic information about the dataset
print("Dataset Overview:")
print(data.info())
print("\nFirst Few Rows:")
print(data.head())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Remove duplicates
data = data.drop_duplicates()

# Fill missing values
data = data.ffill()  # Forward fill

# Use a subset of the dataset for faster analysis and simulation
subset_data = data.sample(n=1000, random_state=42)

# Visualize average heart rate distribution
if 'avg_heart_rate' in subset_data.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(subset_data['avg_heart_rate'], kde=True, bins=30, color='blue')
    plt.title('Average Heart Rate Distribution')
    plt.xlabel('Average Heart Rate')
    plt.ylabel('Frequency')
    plt.show()

# Filter numeric columns for correlation
numeric_cols = subset_data.select_dtypes(include=['float64', 'int64'])
if not numeric_cols.empty:
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm')
    plt.title('Feature Correlation')
    plt.show()

# Simulate real-time data streaming
def simulate_stream(data, delay=1):
    for index, row in data.iterrows():
        print(row.to_dict())
        time.sleep(delay)

simulate_stream(subset_data.head(5))  # Test with the first 5 rows

# Parallel processing using multiprocessing
from multiprocessing import Pool

with Pool(processes=4) as pool:
    results = pool.map(process_row, [row for _, row in subset_data.iterrows()])

print("\nProcessed Results (First 10):")
print(results[:10])
