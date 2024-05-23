import sqlite3

# criando a tabela;

# conexão
conn = sqlite3.connect("exemplo.db")
# criar o cursor para o uso so sql
cursor = conn.cursor()
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
     )
    """)
# adicionando informaçoes(dados) a tabela 
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('João', 43)")
cursor.execute("INSERT INTO usuarios (nome, idade) VALUES ('kiko', 89)")

cursor.execute("SELECT * FROM usuarios")
registros = cursor.fetchall()

# Dando um print para salvar as informaçoes de select 
for registro in registros:
    print(registro)

# commit a informação
conn.commit()
# para fechar a conexão iniciada
cursor.close()
conn.close()
