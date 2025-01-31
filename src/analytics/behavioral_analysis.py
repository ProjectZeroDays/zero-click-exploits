import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(user_data):
    anomalies = []
    for data in user_data:
        if data["activity_level"] > 100:
            anomalies.append(data["user_id"])
    return anomalies

def advanced_ai_driven_anomaly_detection(user_data):
    model = IsolationForest(contamination=0.1)
    activity_levels = np.array([data["activity_level"] for data in user_data]).reshape(-1, 1)
    model.fit(activity_levels)
    predictions = model.predict(activity_levels)
    anomalies = [user_data[i]["user_id"] for i in range(len(predictions)) if predictions[i] == -1]
    return anomalies

if __name__ == "__main__":
    sample_data = [{"user_id": "user1", "activity_level": 120}, {"user_id": "user2", "activity_level": 80}]
    anomalies = detect_anomalies(sample_data)
    print(f"Anomalies Detected: {anomalies}")

    advanced_anomalies = advanced_ai_driven_anomaly_detection(sample_data)
    print(f"Advanced Anomalies Detected: {advanced_anomalies}")
