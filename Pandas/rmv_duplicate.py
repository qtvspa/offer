# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np


if __name__ == '__main__':

    # data = pd.DataFrame(np.ones((3,4)) * 1, columns=['a', 'b', 'c', 'd'], index=[1, 2, 3])
    df1 = pd.read_excel('a.xls', sheet_name='Sheet1', index_col=0)
    df2 = pd.read_excel('a.xls', sheet_name='Sheet2', index_col=0)

    df3 = pd.concat([df1, df2], ignore_index=True)
    print(df3)
    df3.drop_duplicates(subset=['a'], keep='first', inplace=True)
    df3.rename(columns={'d':'D'}, inplace=True)
    print(df3)