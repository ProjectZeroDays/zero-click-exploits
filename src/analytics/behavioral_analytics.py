
def detect_behavioral_anomalies(user_data):
    print(f"Analyzing user behavior for anomalies: {user_data}")
    return {"anomalies_detected": True, "details": ["Unusual login times", "High data upload"]}

if __name__ == "__main__":
    anomalies = detect_behavioral_anomalies({"user": "john.doe", "activity": "login at 3 AM"})
    print(f"Anomalies: {anomalies}")
