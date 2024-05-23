import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()
nome = input("nome:")
idade = input("idade:")
id = input("id:")

cursor.execute("UPDATE estudantes SET idade = ?, nome = ? WHERE id = ?", (idade, nome, id))

# cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (20, 'Bob'))

conn.commit()
cursor.close()
conn.close()