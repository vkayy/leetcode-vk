import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    eb = pd.merge(employee, bonus, on="empId", how="left")[["name", "bonus"]]
    return eb[(eb["bonus"] < 1000) | (eb["bonus"].isnull())]

# first, we merge employee and bonus on empId
# then, we select the name and bonus columns
# finally, we return the rows where bonus is less than 1000 or bonus is null