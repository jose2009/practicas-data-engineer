create database desastres;
go

use desastres
go

create table clima
(
    año int not null primary key,
    Temperatura float not null,
    Oxigeno float not null);
go

INSERT INTO clima VALUES (2023, 22.5,230);
INSERT INTO clima VALUES (2024, 22.7,228.6);
INSERT INTO clima VALUES (2025, 22.9,227.5);
INSERT INTO clima VALUES (2026, 23.1,226.7);
INSERT INTO clima VALUES (2027, 23.2,226.4);
INSERT INTO clima VALUES (2028, 23.4,226.2);
INSERT INTO clima VALUES (2029, 23.6,226.1);
INSERT INTO clima VALUES (2030, 23.8,225.1);

create table desastres
(
    año int not null primary key,
    Tsunamis int not null,
    Olas_Calor int not null,
    Terremotos int not null,
    Erupciones int not null,
    Incendios int not null);
go

INSERT INTO desastres VALUES (2023, 2,15, 6,7,50);
INSERT INTO desastres VALUES (2024, 1,12, 8,9,46);
INSERT INTO desastres VALUES (2025, 3,16, 5,6,47);
INSERT INTO desastres VALUES (2026, 4,12, 10,13,52);
INSERT INTO desastres VALUES (2027, 5,12, 6,5,41);
INSERT INTO desastres VALUES (2028, 4,18, 3,2,39);
INSERT INTO desastres VALUES (2029, 2,19, 5,6,49);
INSERT INTO desastres VALUES (2030, 4,20, 6,7,50);

create table muertes
(
    año int not null primary key,
    R_menor15 int not null,
    R_15_a_30 int not null,
    R_30_a_45 int not null,
    R_45_a_60 int not null,
    R_M_a_60 int not null);
go
INSERT INTO muertes VALUES (2023, 1000,1300, 1200,1150,1500);
INSERT INTO muertes VALUES (2024, 1200,1250, 1260,1678,1940);
INSERT INTO muertes VALUES (2025, 987,1130, 1160,1245,1200);
INSERT INTO muertes VALUES (2026, 1560,1578, 1856,1988,1245);
INSERT INTO muertes VALUES (2027, 1002,943, 1345,1232,986);
INSERT INTO muertes VALUES (2028, 957,987, 1856,1567,1756);
INSERT INTO muertes VALUES (2029, 1285,1376, 1465,1432,1236);
INSERT INTO muertes VALUES (2030, 1145,1456, 1345,1654,1877);

create database DESASTRES_BDE;
go
use DESASTRES_BDE
go

create table Desastre_final
(
    Cuatrenio varchar(20) not null primary key,
    Temp_AVG float not null, Oxi_AVG float not null,
    T_Tsunamis int not null, T_OlasCalor int not null,
    T_Terremotos int not null, T_Erupciones int not null,
    T_Incendios int not null, M_Jovenes_AVG float not null,
    M_Adultos_AVG float not null, M_Ancianos_AVG float not null);
go

use desastres
go

create procedure pETL_Desastres
as 
delete from DESASTRES_BDE.dbo.Desastre_final;
insert into DESASTRES_BDE.dbo.Desastre_final
select x.Cuatrenio, avg(x.Temperatura) as Temp_AVG, avg(x.NivelOxigeno)as Oxi_AVG,
sum(x.Tsunamis) as T_Tsunamis, sum(x.Olas_Calor) as T_OlasCalor, sum(x.Terremotos) as T_Terremotos,
sum(x.Erupciones) as T_Erupciones, sum(x.Incendios) as T_Incendios,
avg(x.Muertes_jovenes) as M_Jovenes_AVG, avg(x.Muertes_adultos) as M_Adultos_AVG, avg(x.Muertes_ancianos) as M_Ancianos_AVG,
from
(select case when c.año < 2026 then '2023-2026' else '2027-2030' end as Cuatrenio,
 Temperatura = c.Temperatura,
 NivelOxigeno = c.Oxigeno,
 Tsunamis = d.Tsunamis,
 Olas_Calor = d.Olas_Calor,
 Terremotos = d.Terremotos,
 Erupciones = d.Erupciones,
 Incendios = d.Incendios,
 Muertes_jovenes = m.R_menor15 + m.R_15_a_30,
 Muertes_adultos = m.R_30_a_45 + m.R_45_a_60,
 Muertes_ancianos = m.R_M_a_60
 from desastres.dbo.clima as c 
 join desastres.dbo.desastres as d on c.año = d.año
 join desastres.dbo.muertes as m on c.año = m.año) x
 group by x.Cuatrenio
 go 

 execute pETL_Desastres;
 go 

 use DESASTRES_BDE

 select * from dbo.Desastre_final
 go 