import sqlite3

conn = sqlite3.connect('livros.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM livros")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)
    
cursor.close()
conn.close()
