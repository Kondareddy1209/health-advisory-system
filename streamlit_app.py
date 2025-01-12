import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src.anomaly_detection import detect_anomalies

# Load the dataset from GitHub raw file URL
file_path = 'https://raw.githubusercontent.com/Kondareddy1209/health-advisory-system/main/health_fitness_dataset.csv'
data = pd.read_csv(file_path)

# Display the available columns in the dataset for debugging
st.write("Available Columns in Dataset:", list(data.columns))

# Check if 'activity_type' exists and handle accordingly
if 'activity_type' in data.columns:
    # Streamlit Sidebar for Filters
    st.sidebar.title("Filters")
    selected_activity = st.sidebar.selectbox(
        "Select Activity Type", 
        data['activity_type'].unique()
    )
    filtered_data = data[data['activity_type'] == selected_activity]
else:
    st.warning("The column 'activity_type' is missing from the dataset. Displaying entire dataset.")
    filtered_data = data

# Display Summary Statistics
st.title("Health Fitness Dashboard")
st.write("## Summary Statistics")
st.write(filtered_data.describe())

# Display Histogram for Average Heart Rate
if 'avg_heart_rate' in filtered_data.columns:
    st.write("## Average Heart Rate Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['avg_heart_rate'], kde=True, bins=30, ax=ax, color='blue')
    st.pyplot(fig)
else:
    st.warning("The column 'avg_heart_rate' is missing from the dataset. Cannot display distribution.")

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
if 'avg_heart_rate' in filtered_data.columns and 'hydration_level' in filtered_data.columns:
    st.write("## Real-Time Anomaly Detection")
    for index, row in filtered_data.head(10).iterrows():  # Limit to 10 rows for demo
        anomalies = detect_anomalies(row)
        st.write(f"Data: {row.to_dict()}")
        if anomalies:
            st.error(f"Anomalies Detected: {anomalies}")
else:
    st.warning("Required columns for anomaly detection ('avg_heart_rate', 'hydration_level') are missing.")

