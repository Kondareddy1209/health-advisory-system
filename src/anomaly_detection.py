def detect_anomalies(row):
    """
    Detect anomalies in a row of health data.
    - High Heart Rate: avg_heart_rate > 100
    - Low Hydration: hydration_level < 1.5
    - High Stress: stress_level > 7
    """
    anomalies = []
    if 'avg_heart_rate' in row and row['avg_heart_rate'] > 100:
        anomalies.append("High Heart Rate")
    if 'hydration_level' in row and row['hydration_level'] < 1.5:
        anomalies.append("Low Hydration")
    if 'stress_level' in row and row['stress_level'] > 7:
        anomalies.append("High Stress Level")
    return anomalies
