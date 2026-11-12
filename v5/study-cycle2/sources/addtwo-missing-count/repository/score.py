import json
with open("tasks.json") as f:
    data = json.load(f)
print(sum(a == p for a, p in zip(data["answers"], data["predictions"])) / len(data["answers"]))
