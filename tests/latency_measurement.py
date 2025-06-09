import time
import requests
import urllib3
urllib3.disable_warnings()

start = time.time()
requests.post(
    "https://control_server:5000/login",
    data={'username':'admin','password':'admin'},
    verify=False
)
end = time.time()
print(f"Request latency: {(end-start)*1000:.2f} ms")
