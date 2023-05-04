class KonversiSuhu :
    
    @staticmethod
    def celsius_ke_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def celsius_ke_reamur(celsius):
        return celsius * 4/5
    
    @staticmethod
    def celsius_ke_kelvin(celsius):
        return celsius + 273.15
    
celcius1 = 75
celcius2 = 60
celcius3 = 90

# Konversi suhu 75 derajat Celsius ke Fahrenheit
fahrenheit = KonversiSuhu.celsius_ke_fahrenheit(75)
print("konversi suhu",celcius1, "derajat celcius adalah ",fahrenheit, "derajat fahrenheit") # Output: 167.0

# Konversi suhu 60 derajat Celsius ke Reamur
reamur = KonversiSuhu.celsius_ke_reamur(60)
print("konversi suhu",celcius2, "derajat celcius adalah ",reamur, "derajat reamur") # Output: 48.0

# Konversi suhu 90 derajat Celsius ke Kelvin
kelvin = KonversiSuhu.celsius_ke_kelvin(90)
print("konversi suhu",celcius3, "derajat celcius adalah ",kelvin, "derajat kelvin") # Output: 363.15