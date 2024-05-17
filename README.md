# First Commit

Este é o trabalho incrivel de PI trabalhando com o Datasus

Cada vez que voce tiver vontade de se matar mexendo na database, bom
aumente esse contador aqui em +1

> Vezes que quis me matar graças ao Datasus : 5


## Adquirindo os Dados Brutos
> **Requisitos:** python3, wget e unzip.

Começe criando dois diretórios para armazenar os arquivos que serão baixados do DataSus, um para as bases principais e outro para as bases auxiliares:
```sh
$ mkdir data
$ mkdir data/aux
```
Agora use o utilitário **susgrep.sh** para fazer o download de todas as bases de dados necessárias para o SusCube:
```sh
$ ./susgrep.sh data data/aux
```
> A conversão dos arquivos baixados para formatos úteis (como .dbc para .dbf e .cnv para .csv) será feita automaticamente durante a execução do script.

> **Erros comuns:**
> Pacote unzip não está instalado no sistema
> WSL não reconhece cnv2csv

**Correções:**

```bash
$ sudo apt install unzip
```

```bash
$ dos2unix cnv2csv
```
