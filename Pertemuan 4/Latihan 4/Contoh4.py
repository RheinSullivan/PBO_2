class RAM:
    def __init__(self, capacity):
        self.capacity = capacity
class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
class Computer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage
ram = RAM(16)
storage = Storage(1000)
computer = Computer(ram, storage)
print(computer.ram.capacity) # output: 16
print(computer.storage.capacity) # output: 1000
