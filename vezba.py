# Vezba 1 -> Napraviti folder "data" unutar koga cemo imati "user.json" i "products.json"
# Vezba 2 -> Napraviti listu products u fajlu products i ucitati je u vezba
# Vezba 3 -> Napraviti funkciju load_file koja ce da ucita fajl i koja ce da nam izbaci sta taj fajl sadrzi
# Vezba 4 -> U methods fajlu napravi funkciju koja ce da cuva podatke u fajlu

# Iz methods ucitaj funkciju load_file
from methods import load_file, save_file

data = load_file("data/products.json")
users = load_file("data/products.json")
print(data, users)

save = save_file("fajl1.json", users)


