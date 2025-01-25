import tkinter as tk
from tkinter import ttk

class UserActivitiesWidget(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="User Activities")
        self.label.pack(pady=10)

        self.activities_text = tk.Text(self, wrap="word", height=10, width=50)
        self.activities_text.pack(pady=10)

        self.refresh_button = ttk.Button(self, text="Refresh", command=self.refresh_activities)
        self.refresh_button.pack(pady=10)

    def refresh_activities(self):
        # Placeholder for actual user activities retrieval logic
        user_activities = "Recent user activities will be displayed here."
        self.activities_text.delete(1.0, tk.END)
        self.activities_text.insert(tk.END, user_activities)
