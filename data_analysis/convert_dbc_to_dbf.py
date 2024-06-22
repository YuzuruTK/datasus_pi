import os
import time

print()

data_directory = "data_analysis/raw_data/dbc/"
aux_directory = "data_analysis/raw_data/aux/"
data_output = "data_analysis/output_dbf/"
tools_directory = "data_analysis/tools/"

total_time = time.time()
dbf_names = []
dbf_names = [f for f in os.listdir(data_directory) if f.lower().endswith('.dbf')]

# dbf_names.remove("aux")
counter = 0
print("Convertendo os arquivos DBC para DBF")
for file_name in dbf_names:
    name = file_name[:-4]
    os.system(f"sudo ./{tools_directory}blast-dbf {data_directory+name}.dbc {data_output+name}.dbf")
    counter += 1
    print(f"\r{counter}/{len(dbf_names)} {round((counter/len(dbf_names))*100, 2)}%",end="",)
# os.remove(data_output+".dbf")
print(f"\nTodos os DBCs foram convertidos em {round(time.time() - total_time, 2)} segundos")

cnv_names = [f for f in os.listdir(aux_directory) if f.lower().endswith('.cnv')]

counter_cnv = 0
total_time = time.time()

print("Convertendo os arquivos CNV para CSV")

for file_name in cnv_names:
    name = file_name[:-4]
    os.system(f"sudo ./{tools_directory}cnv2csv {aux_directory}{file_name}")
    counter_cnv += 1
    print(f"\r{counter_cnv}/{len(cnv_names)} {round((counter_cnv/len(cnv_names))*100, 2)}%",end="",)
    os.rename(f"{aux_directory}{name}.csv", f"{data_output}aux/{name}.csv")
print(f"\nTodos os CNVs foram convertidos em {round(time.time() - total_time, 2)} segundos")