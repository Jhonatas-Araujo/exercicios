select nome, ano from cursos
where ano between 2014 and 2016
order by ano desc, nome asc;

select nome, descricao, ano from cursos
where ano in (2014, 2015, 2016)
order by ano;

select nome, carga, totaulas from cursos
where carga > 35 and totaulas < 30;

select * from cursos
where nome like '%A';

select * from cursos
where nome like 'P%';

select * from cursos
where nome like '%A%';

select * from cursos
where nome not like '%A%';

select * from cursos
where nome like 'ph%p_';

update cursos
set nome = 'Photoshop' 
where idcurso = '3';

select distinct nacionalidade from gafanhotos;

select count(*) from gafanhotos;

select count(*) from cursos;

select max(carga) from cursos;

select max(totaulas) from cursos where ano = '2016';

select nome, min(totaulas) from cursos where ano = '2016';

select sum(totaulas) from cursos where ano = '2016';
#sum = soma
select avg(totaulas) from cursos where ano = '2016';
#avg = média
