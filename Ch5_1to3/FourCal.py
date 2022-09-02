class FourCal:
    def __init__(self, int1 = None, int2 = None):
        self.int1 = int1
        self.int2 = int2

    def set_data(self, int1, int2):
        self.int1 = int1
        self.int2 = int2

    def add(self):
        result = self.int1 + self.int2
        return result

    def minus(self):
        result = self.int1 - self.int2
        return result

    def mul(self):
        result = self.int1 * self.int2
        return result

    def div(self):
        result = self.int1 / self.int2
        return result


if __name__ == "__main__":
    a = FourCal()
    
    a.set_data(1, 5)
    print(a.int1)
    print(type(a.int1))
    print(id(a.int1))
    print(a.int2)
    print(type(a.int2))
    print(id(a.int2))

    a.set_data("a", "b")
    print(a.int1)
    print(type(a.int1))
    print(id(a.int1))
    print(a.int2)
    print(type(a.int2))
    print(id(a.int2))
