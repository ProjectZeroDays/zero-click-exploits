import os

def analyze_memory_dump(dump_path):
    if not os.path.exists(dump_path):
        print(f"Error: Memory dump not found at {dump_path}")
        return

    try:
        with open(dump_path, 'r') as dump:
            suspicious_strings = [line for line in dump if "suspicious" in line]
    except IOError as e:
        print(f"Error reading memory dump: {e}")
        return

    if suspicious_strings:
        print("Suspicious data found:")
        for s in suspicious_strings:
            print(s)
    else:
        print("No suspicious data detected.")

if __name__ == "__main__":
    analyze_memory_dump("memory_dump.txt")
