import csv
import os
import duckdb
import time
from dbfread import DBF

dbf_directory = "./output_dbf"
output_directory = "./database"
table_name = "psicossocial"
database_name = "database_pi"

if os.path.exists(f"{output_directory}/{database_name}.db"):
    os.remove(f"{output_directory}/{database_name}.db")
if not os.path.exists(output_directory):
    os.mkdir(output_directory) 

database = duckdb.connect(f"{output_directory}/{database_name}.db")

dbf_db_files = [f for f in os.listdir(dbf_directory) if f.endswith('.dbf')]
# aux_db_files = [f for f in os.listdir(dbf_directory+"/aux") if f.endswith('.csv')]


## IGNORA ESSA PARADA DE MACACO FOI LITERAL PRA TESTE OK
## O BANCO JA VAI TA GERADO, DPS TENHO Q VER COMO EU PASSO UM ARQUIVO SQL PRA RODAR
database.execute(
    f"""
CREATE TABLE {table_name}(
  cnes_exec  char(7),
  gestao     char(6),
  condic     char(2),
  ufmun      char(6),
  tpups      char(2),
  tippre     char(2),
  mn_ind     char(1),
  cnpjcpf    char(14),
  cnpjmnt    char(14),
  dt_process char(6),
  dt_atend   char(6),
  cns_pac    char(15),
  dtnasc     char(8),
  tpidadepac char(1),
  idadepac   char(2),
  nacion_pac char(2),
  sexopac    char(1),
  racacor    char(2),
  etnia      char(2),
  munpac     char(6),
  mot_cob    char(2),
  dt_motcob  char(8),
  catend     char(2),
  cidpri     char(4),
  cidassoc   char(4),
  origem_pac char(2),
  dt_inicio  char(8),
  dt_fim     char(8),
  cob_esf    char(1),
  cnes_esf   char(7),
  destinopac char(2),
  pa_proc_id char(10),
  pa_qtdpro  char(11),
  pa_qtdapr  char(11),
  pa_srv     char(3),
  pa_class_s char(3),
  sit_rua    char(3),
  tp_droga   char(3),
  loc_realiz char(1),
  inicio     char(8),
  fim        char(8),
  permanen   char(4),
  qtdate     char(4),
  qtdpcn     char(4),
  nat_jur    char(4)
  );
"""
)
counter = 0
total_time = time.time()
for dbf_name in dbf_db_files:
    table = DBF(f'{dbf_directory}/{dbf_name}', 'latin-1')
    # DBF TO CSV
    start_time = time.time()
    csv_path = f"{output_directory}/{table.name}.csv"
    with open(csv_path, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(table.field_names)
        for record in table:
            writer.writerow(list(record.values()))
    end_time = time.time()
    elapsed_time = end_time - start_time
    start_time = time.time()
    columns = ""
    for i in range(len(table.field_names)):
        if (i+1) != len(table.field_names):
            columns += table.field_names[i] + ", "
        else:
            columns += table.field_names[i]
    database.sql(f"INSERT INTO {table_name}({columns}) SELECT * FROM read_csv('{output_directory}/{table.name}.csv');")
    os.remove(csv_path)
    end_time = time.time()
    elapsed_time = end_time - start_time    
    counter += 1
    print(f"\r{counter}/{len(dbf_db_files)} {round((counter/len(dbf_db_files))*100, 2)}%",end="",)
print(f"\nTempo total para inserção de todas os dados no BD {round(time.time() - total_time, 2)} segundos")

# for csv_name in aux_db_files:
#     # with open(f'{dbf_directory}/aux/{csv_name}', 'r+',encoding="ISO 8859-1") as file:
#         # line = ['sequencial', 'descricao', 'codigos']
#         # print(f"abrindo {csv_name}")
#         # csvreader = csv.writer(file)
#         # csvreader.writerow(line)
#     csv_to_database(csv_name)
