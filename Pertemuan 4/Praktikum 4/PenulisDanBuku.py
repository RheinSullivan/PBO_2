class Penulis:
    def __init__(self, nama_penulis):
        self.nama_penulis = nama_penulis
        self.karyas = []

    def tambah_karya(self, judul, tahun_terbit):
        karya = Buku(judul, tahun_terbit)
        self.karyas.append(karya)

class Buku:
    def __init__(self, judul, tahun_terbit):
        self.judul = judul
        self.tahun_terbit = tahun_terbit

# membuat objek penulis
synyster_gates = Penulis("Synyster Gates")

# menambahkan buku ke daftar karya penulis
synyster_gates.tambah_karya("City of Evil", 2003)
synyster_gates.tambah_karya("Sounding The Sevent Trumpet", 1999)

# mencetak informasi karya penulis
for karya in synyster_gates.karyas:
    print(karya.judul, karya.tahun_terbit)