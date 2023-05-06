#Nama   : Moh. Rifki Ramadhan
#Nim    : 210511020
#Kelas  : Reguler 2

class MenghitungBMIMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        def lelaki(cls, tinggi):
            return (tinggi - 100) - (tinggi - 100) * 10/100
        cls.lelaki = classmethod(lelaki)

        def perempuan(cls, tinggi):
            return (tinggi - 100) - (tinggi - 100) * 15/100
        cls.perempuan = classmethod(perempuan)
class Ideal(metaclass=MenghitungBMIMeta):
    pass
A = Ideal()
B = A.lelaki(180)
C = A.perempuan(150)
print('BMI Lelaki:',B)
print('BMI Perempuan:',C)
