import sqlite3

conn = sqlite3.connect('database.db')

print("database conectado")

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE user (
        cpf TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        tel TEXT NOT NULL
    )
""")
conn.commit()

print("tabela criada com sucesso")

conn.close()
