select carga, count(*) from cursos
group by carga;

select carga, count(*) from cursos
where totaulas = '30'
group by carga;

select ano, count(*) from cursos
group by ano
having count(ano) >= 5
order by count(*) desc;
#having só mostra pelo que tiver agrupado

select carga, count(*) from cursos
where ano > 2015 
group by carga
having carga > (select avg(carga) from cursos);
