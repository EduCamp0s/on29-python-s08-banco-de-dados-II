import sqlite3

conn = sqlite3.connect('livros.db')
cursor = conn.cursor()

livro_id = 2
cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))

conn.commit()
cursor.close()
conn.close()