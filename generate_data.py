import time
import json
import random

golden_notes = [
    "Lorem ipsum",
    "Good to go",
    "Hello world",
    "It's okay",
    "Need improvement",
    "Could be better next time",
    "This is gold",
    "Mantap djiwa",
    "Cool",
    "Tjakep",
]

data = {}
data["timestamp"] = int(round(time.time()))
data["note"] = random.choice(golden_notes)

print(json.dumps(data), end = '')