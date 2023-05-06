#Nama   : Moh. Rifki Ramadhan
#Nim    : 210511020
#Kelas  : Reguler 2

class BolaMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def luaspermukaan(cls, jari):
            return 4 * 3.14 * jari * jari
        cls.luaspermukaan = classmethod(luaspermukaan)

        def volume(cls, jari):
            return 4/3 * 3.14 * jari * jari * jari
        cls.volume = classmethod(volume)
class Luaspermukaandanvolume(metaclass=BolaMeta):
    pass
A = Luaspermukaandanvolume()
B = A.luaspermukaan(21)
C = A.volume(21)
print('Luas Permukaan Bola:',B)
print('Volume Bola:',C)
