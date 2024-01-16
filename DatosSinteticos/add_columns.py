import pandas as pd
import random
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('kindle_db.csv')

genre_levels = {
    "Children's eBooks": 40,
    "Mystery, Thriller & Suspense": 40,
    "Science Fiction & Fantasy": 40,
    "Teen & Young Adult": 30,
    "History": 30,
    "Romance": 30,
    "Politics & Social Sciences": 25,
    "Humor & Entertainment": 25,
    "Literature & Fiction": 25,
    "Comics": 20,
}


min_num_pages = 50
max_num_pages = 1000
df["num_pages"]  = df.apply(lambda row: random.randint(min_num_pages, max_num_pages), axis=1)

df["popularity"] = df.apply(lambda row: round(genre_levels.get(row["category_name"], 10) * ((row["stars"] * row["reviews"]) / 10000) + 1), axis=1)


min_num_ventas = 500
max_num_ventas = 10000
df["sales"]  = df.apply(lambda row: round(row["popularity"] * random.randint(min_num_ventas, max_num_ventas)), axis=1)

df["num_wish_lists"] = df.apply(lambda row: round(row["sales"] / random.randint(50, 1000))  , axis=1)

def get_unlimited_amount(row):
    if not row["isKindleUnlimited"]:
        return 0
    else:
        return round(row["popularity"] * random.randint(min_num_ventas, max_num_ventas))
df["unlimited_dowload"] = df.apply(get_unlimited_amount, axis=1)

df.to_csv("kindle_db.csv", index=False)
