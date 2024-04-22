# We've loaded your first package for you! You can add as many cells as you need.
import numpy as np

# Begin coding here ...
import pandas as pd
airbnb_price = pd.read_csv('data/airbnb_price.csv')
airbnb_room_type = pd.read_excel('data/airbnb_room_type.xlsx')
airbnb_last_review = pd.read_csv('data/airbnb_last_review.tsv', sep='\t')

# Join the three data frames together into one
df = pd.merge(airbnb_price, airbnb_room_type, on='listing_id')
df = pd.merge(df, airbnb_last_review, on='listing_id')

# What are the dates of the earliest and most recent reviews? Store these values as two separate variables with your preferred names.
df['last_review_date'] = pd.to_datetime(df['last_review'], format='%B %d %Y')

first_reviewed = df["last_review_date"].min()
last_reviewed = df["last_review_date"].max()
#most_recent_data = df["last_review_date"].value_counts().index[0]

# How many of the listings are private rooms? Save this into any variable.
df['room_type'] = df['room_type'].str.lower()
number_of_private_rooms = len(df[df["room_type"] == "private room"])

# What is the average listing price? Round to the nearest penny and save into a variable.
df["price"] = df["price"].str.replace(" dollars", "")
df["price"] = df["price"].astype("float")

average_price = round(df["price"].mean(), 2)

# Combine the new variables into one DataFrame called review_dates with four columns in the following order: first_reviewed, last_reviewed, nb_private_rooms, and avg_price. The DataFrame should only contain one row of values.
summary_dict = {"first_reviewed": [first_reviewed], "last_reviewed": [last_reviewed], "nb_private_rooms": [number_of_private_rooms], "avg_price": [average_price]}
review_dates = pd.DataFrame.from_dict(summary_dict)

print(review_dates)
print(df.columns)