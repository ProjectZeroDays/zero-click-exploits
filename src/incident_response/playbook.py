
class IncidentResponsePlaybook:
    def __init__(self):
        self.playbooks = {
            "Unauthorized Access": ["Isolate System", "Notify Admin", "Log Incident"],
            "Malware Detected": ["Quarantine File", "Run Full Scan", "Update Definitions"],
        }

    def execute_playbook(self, incident_type):
        actions = self.playbooks.get(incident_type, ["No playbook available"])
        print(f"[INCIDENT RESPONSE] Executing playbook for {incident_type}:")
        for action in actions:
            print(f" - {action}")

if __name__ == "__main__":
    playbook = IncidentResponsePlaybook()
    playbook.execute_playbook("Unauthorized Access")
