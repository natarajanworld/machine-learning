# A Pandas Series is like a column in a table.

# It is a one-dimensional array holding data of any type.

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
