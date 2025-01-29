
def detect_anomalies(user_data):
    anomalies = []
    for data in user_data:
        if data["activity_level"] > 100:
            anomalies.append(data["user_id"])
    return anomalies

if __name__ == "__main__":
    sample_data = [{"user_id": "user1", "activity_level": 120}, {"user_id": "user2", "activity_level": 80}]
    anomalies = detect_anomalies(sample_data)
    print(f"Anomalies Detected: {anomalies}")
