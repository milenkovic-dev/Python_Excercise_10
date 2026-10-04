import json

# r -> read
with open("data/user.json", "r") as file:
    data = json.load(file)
    data.append({
        "name": "Petar Petrovic",
        "age": 35,
        "height": 190,
        "gender": "male"
    })
    print(data)

# w -> write

with open("data/user.json", "w") as file:
    json.dump(data, file, indent = 4)