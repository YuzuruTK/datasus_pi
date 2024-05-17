import csv
import os
import duckdb
import time
from dbfread import DBF

# Diretório dos arquivos em DBF
dbf_directory = "./output_dbf/"
# Diretório onde vai ficar a base de dados
output_directory = "./database/"
# Nome da tabela principal
table_name = "psicossocial"
# Nome do arquivo da Database
database_name = "database_pi"

# Caso o arquivo exista, deleta ele
if os.path.exists(f"{output_directory}/{database_name}.db"):
    os.remove(f"{output_directory}/{database_name}.db")
# caso o diretório nao exista, cria ele
if not os.path.exists(output_directory):
    os.mkdir(output_directory) 

# Cria a base de dados
database = duckdb.connect(f"{output_directory}/{database_name}.db") 

# Lista o nome dos arquivos DBF na pasta
dbf_db_files = [f for f in os.listdir(dbf_directory) if f.endswith('.dbf')]
# Lista o nome dos arquivos CSV na pasta auxiliar
aux_db_files = [f for f in os.listdir(dbf_directory+"/aux") if f.endswith('.csv')]

# Itera por todos os arquivos CSV
for csv_name in aux_db_files:
    # pega o nome do arquivo sem extensão
    name = csv_name[:-4]
    # cria a tabela para o cnv que é um csv agora, e coloca o Código como chave primária
    database.sql(f"CREATE TABLE {name.lower()} (ID integer, descricao TEXT, Codigo Text, Primary Key (Codigo));")
    # Importa os dados pra dentro da tabela
    database.sql(f"INSERT INTO {name.lower()} SELECT * FROM read_csv('{dbf_directory}aux/{csv_name}');")

# Abre o arquivo SQL da criação da tabela principal dos DBFs
fd = open('database_creation.sql', 'r')
# Cospe todo o arquivo na variavel
sqlFile = fd.read()
# fecha o arquivo ufa
fd.close()

# Cria a base no banco
database.execute(sqlFile)

# Contador pra ver quantos arquivos foram convertidos
counter = 0
# Tempo inicial para pegar o tempo total que ficou convertendo e importando
total_time = time.time()
for dbf_name in dbf_db_files:
    counter += 1
    # Abre o DBF e joga pra um arquivo
    table = DBF(f'{dbf_directory}/{dbf_name}', 'latin-1')
    csv_path = f"{output_directory}/{table.name}.csv"
    # Abre um CSV e joga todo as coisas do DBF para o CSV
    with open(csv_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(table.field_names)
        for record in table:
            writer.writerow(list(record.values()))
    # Retorna as colunas da tabela no banco de dados
    columns = database.query(f"PRAGMA table_info({table_name});").fetchall()
    # Cria uma String com os nomes das colunas para a inserção no banco de dados
    columns = ", ".join([i[1] for i in columns])
    # Insere os dados no banco de dados, utilizando somente as colunas listadas
    database.sql(f"INSERT INTO {table_name}({columns}) SELECT {columns} FROM read_csv('{output_directory}/{table.name}.csv');")
    # Deleta o arquivo CSV criado
    os.remove(csv_path)
    # Mostra o progresso
    print(f"\r{counter}/{len(dbf_db_files)} {round((counter/len(dbf_db_files))*100, 2)}%",end="",)
# Adicionado todos os DBFs na tabela
database.close()
# Mostra o tempo total de importação
print(f"\nTempo total para inserção de todas os dados no BD {round(time.time() - total_time, 2)} segundos")
