import os
import logging
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from src.dashboard.dashboard import Dashboard
from src.backend.dashboard_update_manager import DashboardUpdateManager
from src.custom_dashboards import CustomDashboards
from src.chatbot.chatbot import chat, get_response
from src.utils.logging import setup_logging

# Initialize logging
setup_logging()

# Initialize rich console
console = Console()

def display_help():
    help_table = Table(title="CLI Dashboard Help")
    help_table.add_column("Command", style="bold magenta")
    help_table.add_column("Description", style="italic green")
    # Add new commands here
    help_table.add_row("start [module_name]", "Start a module")
    help_table.add_row("stop [module_name]", "Stop a module")
    help_table.add_row("expand [module_name]", "Expand module details")
    help_table.add_row("chat", "Start a chat session with the AI chatbot")
    help_table.add_row("imsi_catcher", "Control IMSI Catcher Dashboard")
    help_table.add_row("malware", "Control Malware Dashboard")
    help_table.add_row("spyware", "Control Spyware Dashboard")
    help_table.add_row("adware", "Control Adware Dashboard")
    help_table.add_row("virus", "Control Virus Dashboard")
    help_table.add_row("worm", "Control Worm Dashboard")
    help_table.add_row("botnet", "Control Botnet Dashboard")
    help_table.add_row("ddos", "Control DDoS Dashboard")
    help_table.add_row("rat", "Control RAT Dashboard")
    help_table.add_row("trojan", "Control Trojan Dashboard")
    help_table.add_row("zero_click_exploits", "Control Zero-Click Exploits Dashboard")
    help_table.add_row("email_server", "Control Email Server Dashboard")
    help_table.add_row("email_sms_spoofing", "Control Email/SMS Spoofing Dashboard")
    help_table.add_row("malicious_cookies", "Control Malicious Cookies Dashboard")
    help_table.add_row("exploitations", "Control Exploitations Dashboard")
    help_table.add_row("ai_training", "Control AI Training Dashboard")
    help_table.add_row("ai_trainer", "Control AI Trainer Dashboard")
    help_table.add_row("ai_models", "Control AI Models Dashboard")
    help_table.add_row("developer_mode", "Activate Developer Mode in Chat")
    help_table.add_row("red_team_mode", "Activate Red Team Mode Dashboard")
    help_table.add_row("blue_team_mode", "Activate Blue Team Mode Dashboard")
    help_table.add_row("purple_team_mode", "Activate Purple Team Mode Dashboard")
    help_table.add_row("log", "Display event log")
    help_table.add_row("config [key] [value]", "Update configuration")
    help_table.add_row("help", "Display this help message")
    help_table.add_row("exit", "Exit the CLI dashboard")
    console.print(help_table)

def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"An error occurred in {func.__name__}: {str(e)}")
            console.print(f"An error occurred: {str(e)}", style="bold red")
    return wrapper

@handle_error
def start_chat():
    chat()

# Add new control functions here with error handling and logging
@handle_error
def control_imsi_catcher():
    console.print("IMSI Catcher Dashboard Control", style="bold green")
    # Implement IMSI Catcher control logic here

@handle_error
def control_malware():
    console.print("Malware Dashboard Control", style="bold green")
    # Implement Malware control logic here

# Repeat similar functions for other controls (spyware, adware, etc.)

def cli_dashboard():
    secret_key = os.getenv("DASHBOARD_SECRET", "default_key")
    console.print(f"Using secret key: {secret_key}", style="bold yellow")
    
    dashboard = Dashboard()
    update_manager = DashboardUpdateManager(logger=dashboard.logger)
    custom_dashboards = CustomDashboards()
    
    # Register update callbacks
    update_manager.register_dashboard_update_callback(dashboard.display_dashboard)
    
    while True:
        try:
            dashboard.display_dashboard()
            command = Prompt.ask("Enter command").strip().lower()
            
            if command == "log":
                dashboard.display_event_log()
            elif command == "help":
                display_help()
            elif command == "chat":
                start_chat()
            elif command == "imsi_catcher":
                control_imsi_catcher()
            elif command == "malware":
                control_malware()
            # Add cases for other controls here
            elif command.startswith("config"):
                parts = command.split()
                if len(parts) == 3:
                    key, value = parts[1], parts[2]
                    # Update configuration logic here
                    console.print(f"Configuration updated: {key} = {value}", style="bold green")
                else:
                    console.print("Invalid config command. Use: config [key] [value]", style="bold red")
            elif command == "exit":
                break
            else:
                parts = command.split()
                if len(parts) >= 2:
                    module_name, action = parts[:2]
                    target = parts[2] if len(parts) > 2 else None
                    dashboard.control_module(module_name, action, target)
                else:
                    console.print("Invalid command. Type 'help' for available commands.", style="bold red")
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            console.print(f"An error occurred: {str(e)}", style="bold red")

    console.print("CLI Dashboard Ready", style="bold green")

if __name__ == "__main__":
    cli_dashboard()
