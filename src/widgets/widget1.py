import tkinter as tk
from tkinter import ttk

class SystemStatusWidget(ttk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self, text="System Status")
        self.label.pack(pady=10)

        self.status_text = tk.Text(self, wrap="word", height=10, width=50)
        self.status_text.pack(pady=10)

        self.refresh_button = ttk.Button(self, text="Refresh", command=self.refresh_status)
        self.refresh_button.pack(pady=10)

    def refresh_status(self):
        # Placeholder for actual system status retrieval logic
        system_status = "System is running smoothly."
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, system_status)
