# This file is used to try/test code 
import pandas as pd
import numpy as np

# Code to read the manifest file into a dataframe
'''df = pd.read_csv('ShipCase1.txt', sep=',', header=None, 
                     names=['X', 'Y', 'Weight', 'Info'])
manif = pd.read_csv('ShipCase1.txt', sep=',', header=None, 
                     names=['X', 'Y', 'Weight', 'Info'])
print(df)'''

# Code to remove curly braces from the weight column
'''df["Weight"] = df['Weight'].str.replace(r'{|}', '')'''

# Code to append backets to the weight column
'''df['Weight'] = df['Weight'].astype("string")
df['Weight'] = '{' + df['Weight'] + '}'''

 # Code to remove square brackets from data column
'''df["X"] = df['X'].str.replace(r'[', '', regex=True)
df["Y"] = df['Y'].str.replace(r']', '', regex=True)'''

# Code to update/create a manifest file
'''manif.to_csv('name', header=None, index=False)'''

# Code to swap two rows in the manifest file
'''manif.iloc[0], manif.iloc[1] = manif.iloc[1].copy(), manif.iloc[0].copy()'''

# Code to pass by reference, use a list  to pass by reference
'''def main():
    var = [1]
    sup(var)
    for i in var:
        print(i)

def sup(var : int) -> None:
    var[0] = 2
    
main()'''