import requests
import time
import threading

def load_test(url, num_requests, concurrency):
    def send_request():
        try:
            response = requests.get(url)
            print(f"Response code: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")

    threads = []
    for _ in range(concurrency):
        for _ in range(num_requests // concurrency):
            thread = threading.Thread(target=send_request)
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    url = "http://localhost:5000"
    num_requests = 1000
    concurrency = 10

    start_time = time.time()
    load_test(url, num_requests, concurrency)
    end_time = time.time()

    print(f"Load test completed in {end_time - start_time} seconds")
