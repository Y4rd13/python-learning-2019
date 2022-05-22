import pandas as pd
from .module1 import FOO, BOO


def f1():
    s = (FOO.hello.x).replace('Hello', 'Hey')
    x = s + '!'
    print(f'{x}')


def f2():
    df = BOO().boo2()
    print(df.head())
