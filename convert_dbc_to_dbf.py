import os
import time

print()

data_directory = "raw_data/"
data_output = "output_dbf/"

total_time = time.time()
file_names = os.listdir(data_directory)
counter = 0
print("Convertendo os arquivos DBC para DBF")
for file_name in file_names:
    name = file_name[:-4]
    os.system(f"sudo ./tools/blast-dbf {data_directory+name}.dbc {data_output+name}.dbf")
    counter += 1
    print(f"\r{counter}/{len(file_names)} {round((counter/len(file_names))*100, 2)}%",end="",)
os.remove(data_output+".dbf")
print(f"\nTudo convertido em {round(time.time() - total_time, 2)} segundos")
