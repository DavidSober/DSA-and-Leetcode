# here is the 'oops I forgot the method name during an interview way'
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # there is a drop_duplicates method I could have used but for exercise purposes here is the "hard way"
    dupes = customers['email'].duplicated()
    idx = []
    for i in range(len(dupes)):
        if dupes[i] == True:
            idx.append(i)
    customers.drop(idx, inplace=True)
    return customers


# here is the real way
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    # here is the real way
    return customers.drop_duplicates(subset=['email'])