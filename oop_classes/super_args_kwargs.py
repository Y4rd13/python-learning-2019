# The super() function is used to give access to methods and properties of a parent or sibling class. 
# The super() function returns an object that represents the parent class.
class Parent:
    def __init__(self, a, b):
        self.a = a + 2
        self.b = b
    
    def methodparent1(self):
        print(f'methodparent1 args: {self.a, self.b}')
        return 'methodparent1: ' + str(self.a + self.b)

class Child1(Parent):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a, b)

    def method1(self, d=0):
        print(f'method1 args: {self.a, self.b, self.c, d}')
        return 'method1: ' + str((self.a + self.b + self.c) * d)

class ChildArgsKwargs(Parent):
    def __init__(self, z, *args, **kwargs):
        print(f'z: {z}')
        if args:
            self.x, self.y = args
        self.a, self.b = kwargs['a'], kwargs['b']
        super().__init__(**kwargs)

    def methodparent(self):
        print('methodparent')
        return super().methodparent1()

    def methodArgsKwargs(self, a: str, b=0):
        print(f'methodArgsKwargs args: {self.x, self.y, b, a}')
        return str((self.x + self.y) * b) + a
    
    def methodKwargs(self):
        print('methodKwargs')
        return self.a + self.b


if __name__ == '__main__':
    p = Parent(a=2, b=2)
    print(p.methodparent1())
    print()

    c1 = Child1(a=1, b=1, c=1)
    print(c1.method1(d=2))
    print()

    c2 = ChildArgsKwargs(1, *(2, 3), **{'a':2, 'b':2})
    print(c2.methodparent())
    print()

    print(c2.methodArgsKwargs(a=' returned!', b=2))
    print()

    c2 = ChildArgsKwargs(z=3, a=2, b=2)
    print(c2.methodKwargs())