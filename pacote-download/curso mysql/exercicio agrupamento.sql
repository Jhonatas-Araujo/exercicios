#exercicio 1
select profissao, count(*) from gafanhotos
group by profissao;

#exercicio 2
select nascimento, count(*) from gafanhotos
where nascimento > '2005-01-01' and sexo = 'F'
group by nascimento;

select sexo, count(*) from gafanhotos
where nascimento > '2005-01-01'
group by sexo;

#exercicio 3
select nacionalidade, count(*) from gafanhotos
where nacionalidade != 'brasil' 
group by nacionalidade
having count(*) > '3';

#exercicio 4
select altura, count(*) from gafanhotos
where peso > '100'
group by altura
having altura > (select avg(altura) from gafanhotos);
