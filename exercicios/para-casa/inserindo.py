import sqlite3

conn = sqlite3.connect('livros.db')
cursor = conn.cursor()


cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES ('A Culpa é das Estrelas', 'John Green', 2012, 29.90)")
cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES ('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 1943, 19.99)")
cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES ('Dom Quixote', 'Miguel de Cervantes', 1605, 39.50)")
cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES ('Harry Potter e a Pedra Filosofal', 'J.K. Rowling', 1997, 34.80)")
cursor.execute("INSERT INTO livros (titulo, autor, ano, preco) VALUES ('É assim que acaba', 'Colleen Hoover', 2018, 45.00)")


conn.commit()
cursor.close()
conn.close()
