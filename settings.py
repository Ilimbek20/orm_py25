import peewee
from peewee import PostgresqlDatabase

db = PostgresqlDatabase(     # прописываем как приконнектится к нашему файлу 
    'orm_py25',
    user = 'ilim',
    password = '1',
    host = 'localhost',
    port = 5432
)