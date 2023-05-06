class Pekerja:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
class Perusahaan:
    def __init__(self, nama, pekerja):
        self.nama = nama
        self.pekerja = pekerja
    def daftar_pekerja(self):
        for pekerja in self.pekerja:
            print(pekerja.nama, pekerja.umur)
pekerja1 = Pekerja("Zacky", 25)
pekerja2 = Pekerja("John", 25)
perusahaan = Perusahaan("Avenged Sevenfold", [pekerja1, pekerja2])
perusahaan.daftar_pekerja()
