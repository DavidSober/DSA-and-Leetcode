# here is the method chaining method
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    ans = animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]
    return ans 

# here is the expanded version
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    condition = animals['weight'] > 100
    ans = animals[condition]
    ans.sort_values(by='weight', ascending=False, inplace=True)
    ans = ans.drop(columns=['species', 'age', 'weight'])
    return ans 