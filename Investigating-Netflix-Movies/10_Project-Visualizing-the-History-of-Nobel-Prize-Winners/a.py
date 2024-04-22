# Loading in required libraries
import pandas as pd
import seaborn as sns
import numpy as np

# Start coding here!
data = pd.read_csv("nobel.csv")

# What is the most commonly awarded gender and birth country?
top_gender = data["sex"].value_counts().index[0]
top_country = data["birth_country"].value_counts().index[0]

# Which decade had the highest ratio of US-born Nobel Prize winners to total winners in all categories?
a = data["year"]
data["decade"] = np.floor(data["year"] / 10) * 10
data_usa = data[data["birth_country"] == "United States of America"].groupby("decade")["birth_country"].count()

data_world = data.groupby("decade")["birth_country"].count()

result = data_usa / data_world
max_decade_usa_float = result[result.max() == result].index[0]
max_decade_usa = int(max_decade_usa_float)

# Which decade and Nobel Prize category combination had the highest proportion of female laureates?
data["decade"] = np.floor(data["year"] / 10) * 10
data_women = data[data["sex"] == "Female"].groupby("decade")["sex"].count()

data_world = data.groupby("decade")["sex"].count()

result = data_women / data_world
value = result.max()
key = result[result.max() == result].index[0]
max_female_dict = {key: value}

# Who was the first woman to receive a Nobel Prize, and in what category?
data_women = data[data["sex"] == "Female"]
data_women.sort_values("year")
first_woman = data_women.iloc[0]

first_woman_name = first_woman["full_name"]
first_woman_category = first_woman["category"]

# Which individuals or organizations have won more than one Nobel Prize throughout the years?
counts = data['full_name'].value_counts()
repeats = counts[counts >= 2].index
repeat_list = list(repeats)
