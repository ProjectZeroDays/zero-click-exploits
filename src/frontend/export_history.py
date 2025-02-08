
import json
import csv

def export_chat_history(chat_history, file_format="json", file_name="chat_history"):
    if file_format == "json":
        with open(f"{file_name}.json", "w") as file:
            json.dump(chat_history, file)
    elif file_format == "csv":
        with open(f"{file_name}.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Prompt", "Response"])
            writer.writerows(chat_history)

# Example Usage
history = [("Hello", "Hi!"), ("How are you?", "I'm fine, thank you.")]
export_chat_history(history, file_format="csv")
