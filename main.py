import csv
from numpy import product
import pandas as pd



product = pd.read_csv('dummyProduct.csv',index_col=0).transpose()
recipe = pd.read_csv('dummyRecipe.csv',index_col=0).transpose()
sold = pd.read_csv('dummySold.csv',index_col=0).transpose()
rec=list(recipe.columns)
prod=sold["burger"]
#recipe["burger"]*=prod[0]
used=pd.DataFrame()
for i in rec:
    prod=sold[i]
    used[i]=recipe[i]*prod[0]
used["sum"] = used.sum(axis=1)
print(used)


