from math import ceil
import duckdb
import time
import pandas as pd
import os

# Nome do arquivo da Database
database_name = "database_pi"
database_directory = "./data_analysis/database/"
# Ano que começou a base
database_year = 2013

print(f"{database_directory}{database_name}.db")

print("Criação dos Indexes na base para uma Consulta mais rápida (ISSO FARÁ COM QUE A BASE DE DADOS SEJA INUTILIZAVEL PARA A TRANSAÇÃO DE DADOS)")
database = duckdb.connect(f"{database_directory}{database_name}.db") 

date_data = []

months = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

for year in range(database_year, time.localtime(time.time()).tm_year):
    for month in months:
        quarter = (1 if month in ["Janeiro","Fevereiro","Março","Abril","Maio","Junho"] else 2)
        date_data.append((f"{year}{(months.index(month)+1):02}", year, months.index(month)+1 ,quarter ,month))

date_dataframe = pd.DataFrame(date_data, columns=["special_key","ano","mes","semestre","nome_do_mes"])
database.sql("DROP TABLE IF EXISTS Tempo;")
database.sql("CREATE TABLE Tempo AS SELECT * FROM date_dataframe;")
database.sql("INSERT INTO Tempo SELECT * FROM date_dataframe;")

ages_data = []

ages = ["Criança","Adolescente","Adulto","Idoso"]
for age in range(0, 100):
    age_type = ages[0] if age < 12 else ages[1] if age < 18 else ages[2] if age < 60 else ages[3]
    age_period = ceil(age / 10) * 10
    age = f"{age:02}"
    ages_data.append((age, age_type, age_period))
age_dataframe = pd.DataFrame(ages_data, columns=["idade","faixa_etaria","periodo"])
database.sql("DROP TABLE IF EXISTS faixa_etarias;")
database.sql("CREATE TABLE faixa_etarias AS SELECT * FROM age_dataframe;")
database.sql("INSERT INTO faixa_etarias SELECT * FROM age_dataframe;")
database.close()