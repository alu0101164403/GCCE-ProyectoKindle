import random
from faker import Faker
import pandas as pd
import datetime
import time
import csv

fake = Faker()
last_generated_id_filename = 'last_generated_id.txt'

def load_last_generated_id():
    try:
        with open(last_generated_id_filename, 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 133103

def save_last_generated_id(last_id):
    with open(last_generated_id_filename, 'w') as file:
        file.write(str(last_id))

def generate_synthetic_data(num_records):
    data = []
    last_generated_id = load_last_generated_id()
    categorias     = [1,    2,    3,    4,    5,    6,    7,    8,    9,    10,   11,   12,   13,   14,   15,   16,   17,   18,   19,   20,   21,   22,   23,   24,   25,   26,   27,   28,   29,   30,   31]
    probabilidades = [0.12, 0.18, 0.12, 0.21, 0.18, 0.12, 0.21, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.18, 0.12, 0.21, 0.12, 0.12, 0.12, 0.12, 0.27, 0.12, 0.27, 0.12, 0.27, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12]

    for _ in range(num_records):
        id = last_generated_id + 1
        last_generated_id += 1
        asin = fake.unique.uuid4()
        title = fake.sentence(nb_words=5)
        author = fake.name()
        soldBy = ' '
        imgUrl = ' '
        productURL = ' '
        stars = round(random.uniform(1, 5), 1)
        reviews = random.randint(0, 1000)
        price = round(random.uniform(1, 60), 2)
        isKindleUnlimited = random.choice([True, False])
        category_id = random.choices(categorias, weights=probabilidades)[0]
        isBestSeller = random.choice([True, False])
        isEditorPick = random.choice([True, False])
        isGoodReadsChoice = random.choice([True, False])
        publishedDate = fake.date_this_decade()

        category_names = {
            1: "Arts & Photography",
            2: "Comics",
            3: "Education & Teaching",
            4: "History",
            5: "Literature & Fiction",
            6: "Parenting & Relationships",
            7: "Romance",
            8: "Sports & Outdoors",
            9: "Biographies & Memoirs",
            10: "Computers & Technology",
            11: "Engineering & Transportation",
            12: "Humor & Entertainment",
            13: "Medical",
            14: "Politics & Social Sciences",
            15: "Science & Math",
            16: "Teen & Young Adult",
            17: "Business & Money",
            18: "Cookbooks, Food & Wine",
            19: "Foreign Language",
            20: "Law",
            21: "Mystery, Thriller & Suspense",
            22: "Reference",
            23: "Science Fiction & Fantasy",
            24: "Travel",
            25: "Children's eBooks",
            26: "Crafts, Hobbies & Home",
            27: "Health, Fitness & Dieting",
            28: "LGBTQ+ eBooks",
            29: "Nonfiction",
            30: "Religion & Spirituality",
            31: "Self-Help"
        }

        category_name = category_names.get(category_id, 'Unknown')
        num_pages = random.randint(50, 1000)
        popularity = round(10 * (stars * reviews) / 1000 + 1)
        sales = popularity * random.randint(500, 10000)
        num_wish_lists = round(sales / random.randint(50, 10000))
        if not isKindleUnlimited:
            unlimited_dowload =  0
        else:
            unlimited_dowload =  round(popularity * random.randint(500, 10000))

        data.append([id, asin, title, author, soldBy, imgUrl, productURL, stars, reviews, price, 
                    isKindleUnlimited, category_id, isBestSeller, isEditorPick,
                    isGoodReadsChoice, publishedDate, category_name, num_pages, popularity, sales, num_wish_lists, unlimited_dowload])
    save_last_generated_id(last_generated_id)
    return data


num_records = 5  # Cantidad de registros a generar
data = generate_synthetic_data(num_records)

""" # Convierte los datos en un DataFrame de pandas
df = pd.DataFrame(data, columns=['id', 'asin', 'title', 'author', 'soldBy', 'imgUrl', 'productURL', 'stars', 'reviews', 'price', 'isKindleUnlimited',
                                 'category_id', 'isBestSeller', 'isEditorPick', 'isGoodReadsChoice', 'publishedDate', 'category_name'])
 """
# Guarda los datos en un archivo CSV
def save_to_csv(data, filename):
    # Abre el archivo en modo 'a' para añadir (append)
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

save_to_csv(data, 'kindle_db.csv')