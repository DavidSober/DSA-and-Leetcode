# this is the scalable right way to do it 
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(
        columns = {
            'id': 'student_id', 'first':'first_name', 'last':'last_name', 'age':'age_in_years'
            }
        )

# this is the knee jerk reaction way i did it first
# works only if you need to relabel all columns at once. if you need to relabel
# only a few among many. this will not work
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.columns = ['student_id', 'first_name', 'last_name', 'age_in_years']
    return students