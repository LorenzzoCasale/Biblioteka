import sqlite3

def get_db():
    conn = sqlite3.connect('database.db')
    return conn

print("db conectado")

def close_db(conn):
    conn.close()

def create_user(cpf, name, tel):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO user (cpf, name, tel)
        VALUES (?, ?, ?)
    """, (cpf, name, tel))
    conn.commit()
    close_db(conn)

def get_user(cpf):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT cpf, name, tel
        FROM user
        WHERE cpf=?
    """, (cpf,))
    user = cursor.fetchone()
    close_db(conn)
    return user

def update_user(cpf, name=None, tel=None):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE user
        SET name=?, tel=?
        WHERE cpf=?
    """, (name, tel, cpf))
    conn.commit()
    close_db(conn)

def delete_user(cpf):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM user
        WHERE cpf=?
    """, (cpf,))
    conn.commit()
    close_db(conn)

print("tabela criada com sucesso")