class Mahasiswa:
    def __init__(self, nama, nim, kelompok_kkm):
        self.nama = nama
        self.nim = nim
        self.kelompok_kkm = kelompok_kkm

    def display_info(self):
        print(f"Nama: {self.nama}")
        print(f"NIM: {self.nim}")
        print(f"Kelompok KKM: {self.kelompok_kkm.get_nama()}")

class KelompokKKM:
    def __init__(self, nama, tahun_ajaran):
        self.nama = nama
        self.tahun_ajaran = tahun_ajaran
        self.mahasiswa_list = []

    def tambah_mahasiswa(self, mahasiswa):
        self.mahasiswa_list.append(mahasiswa)

    def get_nama(self):
        return self.nama

    def display_info(self):
        print(f"Nama Kelompok: {self.nama}")
        print(f"Tahun Ajaran: {self.tahun_ajaran}")
        print("Daftar Anggota:")
        for mahasiswa in self.mahasiswa_list:
            mahasiswa.display_info()

# Contoh penggunaan
kelompok_1 = KelompokKKM("Kelompok 1", "2022/2023")

mahasiswa_1 = Mahasiswa("Rhein Sullivan", "66613456", kelompok_1)
kelompok_1.tambah_mahasiswa(mahasiswa_1)

mahasiswa_2 = Mahasiswa("Synyster Gates", "666167884", kelompok_1)
kelompok_1.tambah_mahasiswa(mahasiswa_2)

kelompok_1.display_info()