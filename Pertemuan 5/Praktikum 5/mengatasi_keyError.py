data = {"Serigala": 15, "Harimau": 20, "Singa": 33}
try:
    value = data["Kucing"]
except KeyError:
    print("Key yang dicari tidak ditemukan pada data!")