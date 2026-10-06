import json

with open("tickets_invalid.json", "r", encoding="utf-8") as file:
    loaded_tickets = json.load(file)

print(loaded_tickets)
