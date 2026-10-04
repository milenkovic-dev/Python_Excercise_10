# Iz ovog fajla mozemo da koristimo funkcije koje smo ovde napravili

import json

def load_file(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        return data

# save_file, file_name, data

def save_file(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)