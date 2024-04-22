# Re-run this cell
# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

crimes = pd.read_csv("crimes.csv", parse_dates=["Date Rptd", "DATE OCC"], dtype={"TIME OCC": str})
print(crimes.head())

# Ex. 1
crimes["hour"] = crimes['TIME OCC']

crimes["hour"] = crimes['TIME OCC'].str[:2].astype(int)

count_by_hour = crimes["hour"].value_counts()

peak_crime_hour = count_by_hour[count_by_hour.max() == count_by_hour].index[0]
print(peak_crime_hour)


# Ex. 2
night_crimes = crimes[(crimes["hour"] >= 22) | (crimes["hour"] < 4)]

count_by_location = night_crimes["AREA NAME"].value_counts()

peak_night_crime_location = count_by_location[count_by_location.max() == count_by_location].index[0]

print(peak_night_crime_location)


# Ex. 3
def count_by_age(df, column, age1, age2):
    df_age_group = df[(df[column] >= age1) & (df[column] <= age2)]
    amount = df_age_group[column].count()
    return amount


a1 = count_by_age(crimes, "Vict Age", 0, 17)
a2 = count_by_age(crimes, "Vict Age", 18, 25)
a3 = count_by_age(crimes, "Vict Age", 26, 34)
a4 = count_by_age(crimes, "Vict Age", 35, 44)
a5 = count_by_age(crimes, "Vict Age", 45, 54)
a6 = count_by_age(crimes, "Vict Age", 55, 64)
a7 = count_by_age(crimes, "Vict Age", 65, np.inf)

victim_ages = pd.Series([a1, a2, a3, a4, a5, a6, a7])

print(victim_ages)
