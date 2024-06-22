-- Quantidade de atendimentos por doença e por sexo -- CID, SEXO, PRINCIPAL -> count nos registros, agrupar por doença e por sexo
SELECT  COUNT(*) AS quantidade_atendimentos, sexo.descricao AS sexo, cid.CD_DESCR AS doença
FROM main.psicossocial AS p
INNER JOIN main.s_cid AS cid ON cid.CD_COD = p.cidpri
INNER JOIN main.sexo AS sexo on sexo.Codigo = p.sexopac
WHERE p.ufmun = '431020'
GROUP BY cid.CD_DESCR, cid.CD_COD, sexo.descricao
ORDER BY cid.CD_COD,quantidade_atendimentos

-- Suicidio não foi possivel obter dados
-- Quantidade de Casos de Depressão e seus Destinos-- CID, PRINCIPAL, -> FAZER VIEW DE SUICIDIO
SELECT Count(*) AS Atendimentos, ANY_VALUE(saidaperm.descricao) AS Destino_paciente
FROM main.psicossocial AS p
INNER JOIN main.s_cid AS cid ON p.cidpri = cid.CD_COD 
INNER JOIN main.motsaipe as saidaperm on saidaperm.Codigo = p.mot_cob
WHERE p.ufmun = '431020'
AND (p.cidpri LIKE 'F32%' OR p.cidpri LIKE 'F33%')
GROUP BY saidaperm.Codigo  

-- Quantidade de Estabelecimentos por município -- MUNICIPIO, ESTABELECIMENTOS NO RS --> contar a quantidade de estabelecimentos, agrupando por municipio
SELECT COUNT(*) AS quantidade_caps, view_bizarra.municipio FROM (
SELECT ANY_VALUE(cg.FANTASIA) AS estabelecimento, ANY_VALUE(mun.descricao) AS municipio  FROM main.psicossocial p
INNER JOIN main.cadgerrs cg ON cg.CNES = p.cnes_exec
INNER JOIN main.rs_municip mun ON mun.Codigo = p.ufmun
GROUP BY p.cnes_exec
) AS view_bizarra
GROUP BY view_bizarra.municipio
ORDER BY view_bizarra.municipio

-- Quantidades de Atendimentos por Estabelecimento de Ijui
SELECT COUNT(*) AS atendimentos, ANY_VALUE(cg.FANTASIA) AS estabelecimento, FROM main.psicossocial p
INNER JOIN main.cadgerrs cg ON cg.CNES = p.cnes_exec
WHERE p.ufmun = '431020'
GROUP BY p.cnes_exec

-- Qual a Doença mais frequente em cada Idade -- CID, IDADE --> agrupar por idade e pegar a doença mais frequente 
SELECT Count(*) AS Atendimentos, p.idadepac AS Idade_paciente, Any_value(cid.CD_DESCR) AS doença
FROM main.psicossocial AS p
INNER JOIN main.s_cid AS cid ON cid.CD_COD = p.cidpri 
WHERE p.ufmun = '431020'
GROUP BY p.idadepac, p.cidpri 
ORDER BY p.idadepac, Atendimentos
desc

-- Qual a doença mais frequente nas faixas etarias -- CID, IDADE -> Fazer View de Faixa Etaria
SELECT fe.faixa_etaria AS Faixa_Etaria ,m.doença AS Doença, Count(*) AS Casos
FROM MAIN.ATENDIMENTOS_EM_IJUI AS m
INNER JOIN main.faixa_etarias AS fe ON fe.idade = m.idadePaciente 
GROUP BY fe.faixa_etaria, m.doença
ORDER BY Faixa_Etaria asc, Casos desc
-- TEMPO MÉDIO DE PERMANENCIA POR DOENÇA
SELECT m.doença, avg(CAST(m.Tempo_permanencia AS INT)) AS tempo_permanencia
FROM main.atendimentos_em_ijui AS m
GROUP BY m.doença 
ORDER BY tempo_permanencia desc
-- Quantidade de Casos por Faixa Etária -- CID, IDADE
SELECT fe.faixa_etaria AS Faixa_Etaria , Count(*) AS Casos
FROM MAIN.ATENDIMENTOS_EM_IJUI AS m
INNER JOIN main.faixa_etarias AS fe ON fe.idade = m.idadePaciente 
GROUP BY fe.faixa_etaria;
-- Tempo médio de permanencia por doença -- CID, PRINCIPAL -> tempo de entrada - tempo de saida dps fazer a media disso por doença

-- Qual é a doença com maior indice de motivos de Saida ou de Permanencia -- CID, PRINCIPAL, MOTIVO SAIDA PERMANENCIA -> Agrupar por motivos de saida e permanencia, e linkar a doença com maior indice nelas
SELECT ANY_VALUE(atd.Motivo_saida_permanencia) AS Motivo, ANY_VALUE(atd.doença) AS Doença, Count(*) AS Casos
FROM main.atendimentos_em_ijui AS atd
GROUP BY atd.Motivo_saida_permanencia, atd.doença
ORDER BY Motivo asc, Casos desc

-- Atendimentos Relacionados a Depressão
SELECT *
FROM main.atendimentos_em_ijui AS m
WHERE m.cidpri LIKE 'F32%' OR m.cidpri LIKE 'F33%'
-- Depressão por sexo 
SELECT m.sexo, count(*) AS Casos
FROM main.atendimentos_em_ijui AS m
WHERE m.cidpri LIKE 'F32%' OR m.cidpri LIKE 'F33%'
GROUP BY sexo
-- Depressão por racacor
SELECT racacor, count(*) AS Casos
FROM main.atendimentos_em_ijui AS m
WHERE m.cidpri LIKE 'F32%' OR m.cidpri LIKE 'F33%'
GROUP BY racacor
-- Depressão por Idade
SELECT idadePaciente , count(*) AS Casos
FROM main.atendimentos_em_ijui AS m
WHERE m.cidpri LIKE 'F32%' OR m.cidpri LIKE 'F33%'
GROUP BY idadePaciente
-- Depressão por faixa Etária
SELECT fe.faixa_etaria , count(*) AS Casos
FROM main.atendimentos_em_ijui AS m
INNER JOIN main.faixa_etarias AS fe ON fe.idade = m.idadePaciente
WHERE m.cidpri LIKE 'F32%' OR m.cidpri LIKE 'F33%'
GROUP BY fe.faixa_etaria 
-- Ações mais usadas por doença -- CID, AÇÕES, PRINCIPAL --> pegar as ações com mais uso agrupando as doenças


-- Pesquisa bala geral  caps    
SELECT a.sexo ,fe.faixa_etaria ,a.doença ,count(*) AS casos
FROM MAIN.ATENDIMENTOS_EM_IJUI AS a
INNER JOIN main.doencas_mais_caps dmc ON a.cidpri = dmc.cid
INNER JOIN main.faixa_etarias fe ON a.idadePaciente = fe.idade
GROUP BY a.sexo, fe.faixa_etaria, a.doença
ORDER BY doença, faixa_etaria, sexo, casos desc
