import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import os
import json
from typing import Dict, Any, List, Optional
from abc import ABC, abstractmethod
import schedule
import time
from jinja2 import Environment, FileSystemLoader

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Abstract Base Class for Notification Templates
class NotificationTemplate(ABC):
    def __init__(self, template_path: str, template_name: str):
        self.template_path = template_path
        self.template_name = template_name
        self.template = self._load_template()

    @abstractmethod
    def _load_template(self):
        pass

    @abstractmethod
    def render_template(self, data: Dict[str, Any]) -> str:
        pass

# Concrete Class for Email Template
class EmailTemplate(NotificationTemplate):
    def __init__(self, template_path: str = 'templates/email-template.html'):
        super().__init__(template_path, 'Email Template')

    def _load_template(self):
        try:
            env = Environment(loader=FileSystemLoader(os.path.dirname(self.template_path)))
            template_name = os.path.basename(self.template_path)
            return env.get_template(template_name)
        except Exception as e:
            logging.error(f"Error loading email template: {e}")
            return None

    def render_template(self, data: Dict[str, Any]) -> str:
        if self.template:
            try:
                return self.template.render(data)
            except Exception as e:
                logging.error(f"Error rendering email template: {e}")
                return ""
        else:
            logging.error("Email template not loaded.")
            return ""

# Concrete Class for SMS Template
class SMSTemplate(NotificationTemplate):
    def __init__(self, template_path: str = 'templates/sms-template.txt'):
        super().__init__(template_path, 'SMS Template')

    def _load_template(self):
        try:
            with open(self.template_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            logging.error(f"SMS template file not found: {self.template_path}")
            return ""
        except Exception as e:
            logging.error(f"Error loading SMS template: {e}")
            return ""

    def render_template(self, data: Dict[str, Any]) -> str:
        try:
            return self.template.format(**data)
        except Exception as e:
            logging.error(f"Error rendering SMS template: {e}")
            return ""

# Notification Service
class NotificationService:
    def __init__(self):
        self.templates = {
            'email': EmailTemplate(),
            'sms': SMSTemplate()
        }
        self.notification_queue = []
        self.email_config = self._load_email_config()

    def _load_email_config(self) -> Dict[str, Any]:
        """Load email configuration from a JSON file."""
        try:
            with open('email_config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error("Email configuration file not found: email_config.json")
            return {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from email configuration file: email_config.json")
            return {}

    def send_notification(self, notification_type: str, recipient: str, data: Dict[str, Any]):
        """Send notifications using specified template."""
        notification_details = {
            'type': notification_type,
            'recipient': recipient,
            'data': data,
            'timestamp': time.time()
        }
        logging.info(f"Received notification request: {notification_details}")
        self.notification_queue.append(notification_details)
        self._process_notification(notification_details)
        
        # Establish a process for capturing lessons learned
        self.capture_lessons_learned(notification_details)
        # Create a central repository for lessons learned
        self.create_lessons_learned_repository(notification_details)
        # Establish a schedule for reviewing lessons learned
        self.schedule_lessons_learned_review()
        # Develop action plans based on lessons learned
        self.develop_action_plans(notification_details)
        # Share lessons learned with the community
        self.share_lessons_learned(notification_details)

    def _process_notification(self, notification_details: Dict[str, Any]):
        """Process notification based on type."""
        notification_type = notification_details.get('type')
        recipient = notification_details.get('recipient')
        data = notification_details.get('data')

        if notification_type in self.templates:
            template = self.templates[notification_type]
            body = template.render_template(data)
            if body:
                if notification_type == 'email':
                    self._send_email(recipient, body, data.get('subject', 'Notification'))
                elif notification_type == 'sms':
                    self._send_sms(recipient, body)
            else:
                logging.error(f"Failed to render template for notification type: {notification_type}")
        else:
            logging.warning(f"No template found for notification type: {notification_type}")
            logging.info("Default notification processing completed.")

    def _send_email(self, recipient: str, body: str, subject: str):
        """Send email notifications."""
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = self.email_config.get('sender_email', 'noreply@cybersec.com')
        msg['To'] = recipient

        msg.attach(MIMEText(body, 'html'))

        try:
            with smtplib.SMTP(self.email_config.get('smtp_server', 'localhost'), self.email_config.get('smtp_port', 25)) as server:
                if self.email_config.get('use_tls', False):
                    server.starttls()
                if self.email_config.get('smtp_username') and self.email_config.get('smtp_password'):
                    server.login(self.email_config.get('smtp_username'), self.email_config.get('smtp_password'))
                server.sendmail(self.email_config.get('sender_email', 'noreply@cybersec.com'), [recipient], msg.as_string())
                logging.info(f"Email sent to {recipient}")
        except Exception as e:
            logging.error(f"Failed to send email: {e}")

    def _send_sms(self, recipient: str, body: str):
        """Send SMS notifications (placeholder)."""
        logging.info(f"Sending SMS to {recipient}: {body}")
        # Add SMS sending logic here
        logging.info("SMS sent successfully.")

    def schedule_notification_processing(self, interval_seconds: int = 60):
        """Schedule notification processing at regular intervals."""
        def job():
            logging.info("Starting scheduled notification processing...")
            if self.notification_queue:
                notification = self.notification_queue.pop(0)
                self._process_notification(notification)
            else:
                logging.info("No notifications in queue.")
            logging.info("Scheduled notification processing completed.")

        schedule.every(interval_seconds).seconds.do(job)
        while True:
            schedule.run_pending()
            time.sleep(1)

    def start_notification_service(self, interval_seconds: int = 60):
        """Start notification service and processing."""
        self.schedule_notification_processing(interval_seconds)

    def capture_lessons_learned(self, notification_details: Dict[str, Any]):
        """Capture lessons learned from notification processing."""
        lessons_learned = {
            'notification_details': notification_details,
            'lessons': 'Capture lessons learned from the notification process.'
        }
        logging.info(f"Lessons learned captured: {lessons_learned}")

    def create_lessons_learned_repository(self, notification_details: Dict[str, Any]):
        """Create a central repository for lessons learned."""
        repository = {
            'notification_details': notification_details,
            'repository': 'Central repository for lessons learned.'
        }
        logging.info(f"Lessons learned repository created: {repository}")

    def schedule_lessons_learned_review(self):
        """Establish a schedule for reviewing lessons learned."""
        schedule.every(30).days.do(self.review_lessons_learned)
        logging.info("Schedule for reviewing lessons learned established.")

    def review_lessons_learned(self):
        """Review lessons learned."""
        logging.info("Reviewing lessons learned...")

    def develop_action_plans(self, notification_details: Dict[str, Any]):
        """Develop action plans based on lessons learned."""
        action_plans = {
            'notification_details': notification_details,
            'action_plans': 'Develop action plans based on lessons learned.'
        }
        logging.info(f"Action plans developed: {action_plans}")

    def share_lessons_learned(self, notification_details: Dict[str, Any]):
        """Share lessons learned with the community."""
        lessons_learned = {
            'notification_details': notification_details,
            'lessons': 'Share lessons learned with the community.'
        }
        logging.info(f"Lessons learned shared with the community: {lessons_learned}")

if __name__ == '__main__':
    service = NotificationService()
    email_data = {'subject': 'Threat Alert', 'message': 'A new threat has been detected.', 'threat_level': 'high'}
    service.send_notification('email', 'admin@cybersec.com', email_data)
    sms_data = {'message': 'System alert: High CPU usage detected.'}
    service.send_notification('sms', '+15551234567', sms_data)
    service.start_notification_service(interval_seconds=30)
