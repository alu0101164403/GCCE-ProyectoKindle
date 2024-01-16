import pandas as pd
from faker import Faker
import random

df_original = pd.read_csv('kindle_db.csv')

autores_unicos = df_original['author'].unique()

datos_autores = []
num_filas = len(autores_unicos)
faker = Faker()


for nombre_autor in autores_unicos:
    biografia = faker.text()
    fecha_nacimiento = faker.date_of_birth(minimum_age=18, maximum_age=80)
    nacionalidad = faker.country()
    idioma_literatura = 'English'
    premios = faker.sentence()

    datos_autores.append({
        'author_name': nombre_autor,
        'biography': biografia,
        'birth_date': fecha_nacimiento,
        'nationality': nacionalidad,
        'language_literature': idioma_literatura,
        'awards': premios
    })


df_autores_sinteticos = pd.DataFrame(datos_autores)

# Guardar el DataFrame en un nuevo archivo CSV
df_autores_sinteticos.to_csv('authors_info.csv', index=False)