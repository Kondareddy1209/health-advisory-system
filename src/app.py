import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from src.anomaly_detection import detect_anomalies
from src.parallel_processing import process_row

# Load the dataset
file_path = 'https://raw.githubusercontent.com/Kondareddy1209/health-advisory-system/main/health_fitness_dataset.csv'
data = pd.read_csv(file_path)

# Basic information
print("Dataset Overview:")
print(data.info())
print("\nFirst Few Rows:")
print(data.head())

# Subset for faster processing
subset_data = data.sample(n=1000, random_state=42)

# Visualize average heart rate
if 'avg_heart_rate' in subset_data.columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(subset_data['avg_heart_rate'], kde=True, bins=30, color='blue')
    plt.title('Average Heart Rate Distribution')
    plt.xlabel('Average Heart Rate')
    plt.ylabel('Frequency')
    plt.show()

# Simulate real-time streaming
def simulate_stream(data, delay=1):
    for index, row in data.iterrows():
        print(row.to_dict())
        time.sleep(delay)

simulate_stream(subset_data.head(5))
