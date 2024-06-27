#!/usr/bin/env fish

# Verifique se o diretório "output" existe; caso contrário, crie-o
if not test -d output
    mkdir output
end

# Loop através de todos os arquivos PNG no diretório atual
for img in *.png
    convert "$img" -trim "output/$img"
end
