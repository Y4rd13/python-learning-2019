class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property
    def fsum(self, z=2):
        return str(self.x + self.y + z) + ' string'
    
    @fsum.setter
    def fsum(self, value):
        self.x, self.y = value

if __name__ == '__main__':
    c = MyClass(2, 2)
    print(c.fsum)
    c.fsum = (1, 1)
    print(c.fsum)