import json

class HomeFeed:
    def __init__(self, activities_file, notifications_file):
        self.activities_file = activities_file
        self.notifications_file = notifications_file
        self.activities = self.load_activities()
        self.notifications = self.load_notifications()

    def load_activities(self):
        try:
            with open(self.activities_file, 'r') as file:
                activities = json.load(file)
        except FileNotFoundError:
            activities = []
        return activities

    def load_notifications(self):
        try:
            with open(self.notifications_file, 'r') as file:
                notifications = json.load(file)
        except FileNotFoundError:
            notifications = []
        return notifications

    def render_home_feed(self):
        home_feed_data = {
            "activities": self.activities,
            "notifications": self.notifications
        }
        return home_feed_data

    def display_recent_activities(self):
        return self.activities

    def display_notifications(self):
        return self.notifications

    def add_activity(self, activity):
        self.activities.append(activity)
        self.save_activities()

    def add_notification(self, notification):
        self.notifications.append(notification)
        self.save_notifications()

    def save_activities(self):
        with open(self.activities_file, 'w') as file:
            json.dump(self.activities, file)

    def save_notifications(self):
        with open(self.notifications_file, 'w') as file:
            json.dump(self.notifications, file)

    def link_frontend_components(self, frontend_data):
        linked_data = {
            "frontend_activities": frontend_data.get("activities", []),
            "frontend_notifications": frontend_data.get("notifications", [])
        }
        return linked_data

    def verify_control_mechanisms(self, control_data):
        verified_data = {
            "control_activities": control_data.get("activities", []),
            "control_notifications": control_data.get("notifications", [])
        }
        return verified_data
