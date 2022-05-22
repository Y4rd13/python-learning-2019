from pathlib import Path
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
path = " ".join(path.split()[:-1])
print(path)
sys.path.insert(0, path)

if __name__ == '__main__':
    from utils.module1 import FOO, BOO
    from utils.module2 import f1, f2
    import pandas as pd
    print('\nmodule1...')
    print(FOO.hello.x)
    print(BOO().boo1())
    df = BOO().boo2()
    print(df.head())

    print('\nmodule2...')
    f1()
    f2()

    print('\nPandas')
    print(pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}).head())
