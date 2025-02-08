import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AlertsNotifications:
    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def send_email(self, recipient, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.smtp_user
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_user, self.smtp_password)
                server.sendmail(self.smtp_user, recipient, msg.as_string())
                print(f"Email sent to {recipient}")
        except Exception as e:
            print(f"Failed to send email: {e}")

    def send_alert(self, alert_type, alert_details):
        subject = f"Alert: {alert_type}"
        body = f"Details: {alert_details}"
        self.send_email("admin@example.com", subject, body)

    def notify_device_connection(self, device_id):
        subject = "Device Connected"
        body = f"Device {device_id} has been connected."
        self.send_email("admin@example.com", subject, body)

    def notify_device_disconnection(self, device_id):
        subject = "Device Disconnected"
        body = f"Device {device_id} has been disconnected."
        self.send_email("admin@example.com", subject, body)
