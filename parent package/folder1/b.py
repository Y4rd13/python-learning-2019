from pathlib import Path
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
print(path)
sys.path.insert(0, path)

if __name__ == '__main__':
    from utils.module1 import FOO, BOO
    from utils.module2 import f1, f2

    print('\nmodule1...')
    print(FOO.hello.x)
    print(BOO().boo1())
    df = BOO().boo2()
    print(df.head())

    print('\nmodule2...')
    f1()
    f2()
