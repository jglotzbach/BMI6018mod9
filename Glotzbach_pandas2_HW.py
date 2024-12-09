import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10,9, 8, 7, 6, 5, 4, 3, 2, 1])

print('Jason Glotzbach Pandas Assignment 2-1')
print("\n")

#Question 1:
euc_dist = ((p - q)**2).sum()**0.5
print('Question 1:')
print(euc_dist)
print("\n")

#Question 2:
df = pd.DataFrame(np.arange(20).reshape(-1,5),columns=list('abcde'))
df = df[['c','b','a','d','e']]
print('Question 2:')
print(df)
print("\n")

#Question 3:
print('Question 3:')
print('switching columns b & d:')
df = pd.DataFrame(np.arange(20).reshape(-1,5),columns=list('abcde'))
def col_switch(df,c1,c2):
    cols = list(df.columns)
    idx1, idx2 = cols.index(c1), cols.index(c2)
    cols[idx1], cols[idx2] = cols[idx2], cols[idx1]
    new_df = df[cols]
    return new_df
col_switch(df,'b','d')