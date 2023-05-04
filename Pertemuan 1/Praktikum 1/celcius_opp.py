class KonversiSuhu :

    def __init__(self, celcius):
        self.celcius = celcius

    def to_reamur(self):
        return (4/5) * self.celcius

    def to_kelvin(self):
        return self.celcius + 273.15
    def to_fahrenheit(self):
        return (9/5) * self.celcius + 32

suhu = KonversiSuhu(70)
reamur = suhu.to_reamur()
kelvin = suhu.to_kelvin()
fahrenheit = suhu.to_fahrenheit()

# Konversi suhu 70 derajat Celsius ke Reamur
print(f"Konversi suhu {suhu.celcius} derajat celsius adalah {reamur} derajat reamur") # Output: 56.0 

# Konversi suhu 70 derajat Celsius ke Kelvin
print(f"Konversi suhu {suhu.celcius} derajat celsius adalah {kelvin} derajat kelvin") # Output: 343.15

# Konversi suhu 70 derajat Celsius ke Fahrenheit
print(f"Konversi suhu {suhu.celcius} derajat celsius adalah {fahrenheit} derajat fahrenheit") # Output: 158.0