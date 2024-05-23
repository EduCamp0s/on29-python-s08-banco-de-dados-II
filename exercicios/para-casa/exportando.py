import csv
import sqlite3

conn = sqlite3.connect('livros.db')
cursor = conn.cursor()


cursor.execute("SELECT titulo, preco FROM livros")
dados = cursor.fetchall()

colunas = [description[0] for description in cursor.description]
arquivo_csv = 'exportados_livros.csv'


with open(arquivo_csv, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(colunas)
    writer.writerows(dados)


cursor.close()
conn.close()


