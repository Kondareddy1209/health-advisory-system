import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from src.anomaly_detection import detect_anomalies

# Load the dataset from GitHub raw file URL
file_path = "https://raw.githubusercontent.com/Kondareddy1209/health-advisory-system/main/health_fitness_dataset.csv"

# Load the dataset with error handling
try:
    data = pd.read_csv(file_path)
    st.success("Dataset loaded successfully!")
except Exception as e:
    st.error("Failed to load dataset. Please check the file path or format.")
    st.stop()

# Display the available columns in the dataset
st.write("### Available Columns in Dataset:", list(data.columns))

# Handle missing columns dynamically
if 'activity_type' in data.columns:
    st.sidebar.title("Filters")
    selected_activity = st.sidebar.selectbox(
        "Select Activity Type",
        data['activity_type'].unique()
    )
    filtered_data = data[data['activity_type'] == selected_activity]
else:
    st.warning("The column 'activity_type' is missing. Displaying the entire dataset.")
    filtered_data = data

# Display summary statistics
st.title("Health Fitness Dashboard")
st.write("## Summary Statistics")
st.write(filtered_data.describe())

# Visualize average heart rate distribution if the column exists
if 'avg_heart_rate' in filtered_data.columns:
    st.write("## Average Heart Rate Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['avg_heart_rate'], kde=True, bins=30, ax=ax, color='blue')
    plt.title("Average Heart Rate Distribution")
    st.pyplot(fig)
else:
    st.warning("The column 'avg_heart_rate' is missing. Cannot display distribution.")

# Display correlation heatmap if numeric columns exist
numeric_cols = filtered_data.select_dtypes(include=['float64', 'int64'])
if not numeric_cols.empty:
    st.write("## Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(numeric_cols.corr(), annot=True, cmap="coolwarm", ax=ax)
    plt.title("Feature Correlation Heatmap")
    st.pyplot(fig)
else:
    st.warning("No numeric columns available for correlation analysis.")

# Real-Time Anomaly Detection
st.write("## Real-Time Anomaly Detection")
if 'avg_heart_rate' in filtered_data.columns and 'hydration_level' in filtered_data.columns:
    for index, row in filtered_data.head(10).iterrows():  # Limit to 10 rows for demo
        anomalies = detect_anomalies(row)
        st.write(f"Data: {row.to_dict()}")
        if anomalies:
            st.error(f"Anomalies Detected: {anomalies}")
else:
    st.warning("Required columns for anomaly detection ('avg_heart_rate', 'hydration_level') are missing.")
