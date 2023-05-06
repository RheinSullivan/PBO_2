class Mesin:
    def __init__(self, jenis, tenaga):
        self.jenis = jenis
        self.tenaga = tenaga

    def hidupkan(self):
        print(f"Mesin {self.jenis} dengan tenaga {self.tenaga} dinyalakan")

    def matikan(self):
        print(f"Mesin {self.jenis} dimatikan")

class Mobil:
    def __init__(self, merk, model, mesin):
        self.merk = merk
        self.model = model
        self.mesin = mesin

    def nyalakan(self):
        print(f"Mobil {self.merk} {self.model} dinyalakan")
        self.mesin.hidupkan()

    def matikan(self):
        print(f"Mobil {self.merk} {self.model} dimatikan")
        self.mesin.matikan()


mesin = Mesin("Bensin", "770 HP")
mobil = Mobil("Lamborghini", "Aventador", mesin)

mobil.nyalakan()
mobil.matikan() 