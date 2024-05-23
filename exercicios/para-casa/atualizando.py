import sqlite3


conn = sqlite3.connect('livros.db')
cursor = conn.cursor()


livro_id = 1
novo_preco = 29.99
cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, livro_id))


conn.commit()
cursor.close()
conn.close()
