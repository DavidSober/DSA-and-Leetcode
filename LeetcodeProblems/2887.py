# sure enough here is the built in method
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'].fillna(0, inplace=True)
    return products


# this is my first crack at it. im sure there is some built in method for this too 
import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = [0 if pd.isna(quant) else quant for quant in products['quantity']]
    return products