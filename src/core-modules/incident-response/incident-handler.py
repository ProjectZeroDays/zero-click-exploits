import logging

class IncidentHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        handler = logging.FileHandler('incident_handler.log')
        handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def handle_incident(self, incident_type, severity, details):
        self.logger.info(f"Handling incident: {incident_type}, Severity: {severity}, Details: {details}")
        if severity == 'high':
            self.logger.info(f"High severity incident: {incident_type}")
            self.take_immediate_action(incident_type, details)
        elif severity == 'medium':
            self.logger.info(f"Medium severity incident: {incident_type}")
            self.take_moderate_action(incident_type, details)
        else:
            self.logger.info(f"Low severity incident: {incident_type}")
            self.take_low_priority_action(incident_type, details)

    def take_immediate_action(self, incident_type, details):
        self.logger.info(f"Taking immediate action for incident: {incident_type}, Details: {details}")
        # Placeholder for immediate action logic

    def take_moderate_action(self, incident_type, details):
        self.logger.info(f"Taking moderate action for incident: {incident_type}, Details: {details}")
        # Placeholder for moderate action logic

    def take_low_priority_action(self, incident_type, details):
        self.logger.info(f"Taking low priority action for incident: {incident_type}, Details: {details}")
        # Placeholder for low priority action logic

    def example_usage(self):
        simulated_incident_data = [
            {'incident_type': 'malware', 'severity': 'high', 'details': 'Ransomware detected on server'},
            {'incident_type': 'phishing', 'severity': 'medium', 'details': 'Phishing email reported by user'},
            {'incident_type': 'data_breach', 'severity': 'low', 'details': 'Suspicious login detected'}
        ]
        for incident in simulated_incident_data:
            self.handle_incident(incident['incident_type'], incident['severity'], incident['details'])

if __name__ == "__main__":
    handler = IncidentHandler()
    handler.example_usage()
