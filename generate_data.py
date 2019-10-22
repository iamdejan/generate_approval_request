import time
import json

data = {}
data["timestamp"] = int(round(time.time()))
data["note"] = "Good to go"

print(json.dumps(data), end = '')