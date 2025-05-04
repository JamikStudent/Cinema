from sqlalchemy import create_engine, text
from urllib.parse import quote_plus

password = quote_plus("1234")  # Ваш пароль
engine = create_engine(f'postgresql://postgres:{password}@localhost:5432/Cinema?client_encoding=UTF8')

with engine.connect() as connection:
    result = connection.execute(text('SELECT name, genre FROM "Film"'))
    for row in result:
        print(row)