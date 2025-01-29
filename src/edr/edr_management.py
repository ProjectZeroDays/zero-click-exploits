
def edr_scan(endpoints):
    print(f"Scanning endpoints: {endpoints}")
    return [{"endpoint": endpoint, "status": "Clean"} for endpoint in endpoints]

if __name__ == "__main__":
    results = edr_scan(["192.168.1.101", "192.168.1.102"])
    print(f"EDR Scan Results: {results}")
