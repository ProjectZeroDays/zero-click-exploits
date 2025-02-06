
import os

def cli_dashboard():
    secret_key = os.getenv("DASHBOARD_SECRET", "default_key")
    print(f"Using secret key: {secret_key}")
    print("CLI Dashboard Ready")

if __name__ == "__main__":
    cli_dashboard()
