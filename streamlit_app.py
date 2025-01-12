import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src.anomaly_detection import detect_anomalies

# Load the dataset from GitHub raw file URL
file_path = r'https://github.com/Kondareddy1209/health-advisory-system/blob/main/health_fitness_dataset.csv'
data = pd.read_csv(file_path)

# Streamlit Sidebar for Filters
st.sidebar.title("Filters")
selected_activity = st.sidebar.selectbox(
    "Select Activity Type", 
    data['activity_type'].unique()
)
filtered_data = data[data['activity_type'] == selected_activity]

# Display Summary Statistics
st.title("Health Fitness Dashboard")
st.write("## Summary Statistics")
st.write(filtered_data.describe())

# Display Histogram for Average Heart Rate
st.write("## Average Heart Rate Distribution")
fig, ax = plt.subplots()
sns.histplot(filtered_data['avg_heart_rate'], kde=True, bins=30, ax=ax, color='blue')
st.pyplot(fig)

# Display Correlation Heatmap
st.write("## Correlation Heatmap")
numeric_cols = filtered_data.select_dtypes(include=['float64', 'int64'])
if not numeric_cols.empty:
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
else:
    st.warning("No numeric columns available for correlation analysis.")

# Real-Time Anomaly Detection
st.write("## Real-Time Anomaly Detection")
for index, row in filtered_data.head(10).iterrows():  # Limit to 10 rows for demo
    anomalies = detect_anomalies(row)
    st.write(f"Data: {row.to_dict()}")
    if anomalies:
        st.error(f"Anomalies Detected: {anomalies}")
