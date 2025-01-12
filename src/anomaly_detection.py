def detect_anomalies(row):
    anomalies = []
    if row['avg_heart_rate'] > 100:
        anomalies.append("High Heart Rate")
    if row['hydration_level'] < 1.5:
        anomalies.append("Low Hydration")
    if row['stress_level'] > 7:
        anomalies.append("High Stress Level")
    return anomalies
