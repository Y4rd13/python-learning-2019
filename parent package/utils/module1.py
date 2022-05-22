import pandas as pd


class FOO:
    class hello:
        x = 'Hello World'


class BOO:
    def __init__(self) -> None:
        pass

    def boo1(self):
        print('Foo!')

    def boo2(self):
        print('Pandita!')
        return pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
