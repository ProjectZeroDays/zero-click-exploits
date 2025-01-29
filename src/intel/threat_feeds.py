
import requests

def fetch_threat_intelligence():
    response = requests.get("https://threat-intel-feed.example.com/api")
    if response.status_code == 200:
        return response.json()
    return []

if __name__ == "__main__":
    threat_data = fetch_threat_intelligence()
    print(f"Threat Data: {threat_data}")
