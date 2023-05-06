class Peneliti:
    def __init__(self, nama, bidang):
        self.nama = nama
        self.bidang = bidang
        
class Jurnal:
    def __init__(self, judul, peneliti):
        self.judul = judul
        self.peneliti = peneliti
        
    def daftar_peneliti(self):
        for peneliti in self.peneliti:
            print(peneliti.nama, peneliti.bidang)
            
peneliti1 = Peneliti("The Rev", "Fisika")
peneliti2 = Peneliti("Brooks", "Biologi")
jurnal = Jurnal("Jurnal Sains", [peneliti1, peneliti2])
jurnal.daftar_peneliti()