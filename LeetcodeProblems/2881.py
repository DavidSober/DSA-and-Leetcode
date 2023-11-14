import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    ans = employees.loc[:, 'salary'] * 2 # gets the rows under the salary column name x2 values and stores in ans
    employees['bonus'] = ans # similar syntax to a dict. we add a col name by direct assignment and add the relevant rows
    return employees