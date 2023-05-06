class Matematika:
    def add(self, a, b):
        return a + b
    def add(self, a, b, c=0):
        return a + b + c
mat = Matematika()
B = mat.add(14, 9,3 )
print(B)
mut = Matematika()
C = mut.add(16,2)
print(C)
