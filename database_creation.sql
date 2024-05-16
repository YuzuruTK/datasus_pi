CREATE TABLE psicossocial(
  cnes_exec  char(7), -- cnescrs(Codigo)
  gestao     char(6), -- rs_municip(Codigo)
  condic     char(2), -- tp_gestao(Codigo)
  ufmun      char(6), -- rs_municip(Codigo)
  tpups      char(2), -- tp_estab(Codigo)
  tippre     char(2), -- tipopres(Codigo)
  mn_ind     char(1), -- mant_ind(Codigo)
  cnpjcpf    char(14),
  cnpjmnt    char(14),
  dt_process char(6),
  dt_atend   char(6),
  cns_pac    char(15), -- CARTEIRA DO CARA
  dtnasc     char(8),
  --tpidadepac char(1),
  idadepac   char(2),
  --nacion_pac char(2),
  sexopac    char(1), -- sexo(Codigo)
  racacor    char(2), -- raca_cor(Codigo)
  etnia      char(2), -- etnia(Codigo)
  munpac     char(6), -- rs_municip(Codigo)
  mot_cob    char(2), -- motsaipe(Codigo)
  dt_motcob  char(8),
  catend     char(2), -- carat_at(Codigo)
  cidpri     char(4), -- cid(Codigo)
  cidassoc   char(4), -- cid(Codigo)    
  origem_pac char(2), -- origem(Codigo)
  dt_inicio  char(8),
  dt_fim     char(8),
  cob_esf    char(1), -- S ou N
  cnes_esf   char(7), -- cnescrs(Codigo)
  destinopac char(2), -- destino(Codigo)
--   pa_proc_id char(10),
--   pa_qtdpro  char(11),
--   pa_qtdapr  char(11),
--   pa_srv     char(3),
--   pa_class_s char(3),
  sit_rua    char(3), -- S ou N
  tp_droga   char(3), -- tp_droga(Codigo)
  loc_realiz char(1), -- loc_realiz(Codigo)
  inicio     char(8),
  fim        char(8),
  permanen   char(4),
  qtdate     char(4), -- QT de atendimentos
  qtdpcn     char(4), -- QT de pacientes
  -- Foreign Key (cnes_exec) references cnescrs(Codigo)
  Foreign Key (gestao) references rs_municip(Codigo),
  Foreign Key (ufmun) references rs_municip(Codigo),
  Foreign Key (tpups) references tp_estab(Codigo),
  Foreign Key (tippre) references tipopres(Codigo),
  Foreign Key (mn_ind) references mant_ind(Codigo),
  Foreign Key (sexopac) references sexo(Codigo),
  Foreign Key (racacor) references raca_cor(Codigo),
  Foreign Key (etnia) references etnia(Codigo),
  Foreign Key (munpac) references rs_municip(Codigo),
  Foreign Key (mot_cob) references motsaipe(Codigo),
  Foreign Key (catend) references carat_at(Codigo),
  Foreign Key (cidpri) references cid(Codigo),
  Foreign Key (cidassoc) references cid(Codigo),
  Foreign Key (origem_pac) references origem(Codigo),
  Foreign Key (destinopac) references destino(Codigo),
  Foreign Key (tp_droga) references tp_droga(Codigo),
  Foreign Key (loc_realiz) references loc_realiz(Codigo),
  --Foreign Key (cnes_esf) references cnescrs(Codigo)
);
