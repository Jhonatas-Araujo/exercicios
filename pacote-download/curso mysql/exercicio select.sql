#1) Uma lista com o nome de todos os gafanhotos Mulheres.
#2) Uma lista com os dados de todos aqueles que nasceram entre 1/Jan/2000 e 31/Dez/2015.
#3) Uma lista com o nome de todos os homens que trabalham como programadores.
#4) Uma lista com os dados de todas as mulheres que nasceram no Brasil e que têm seu nome iniciando com a letra J.
#5) Uma lista com o nome e nacionalidade de todos os homens que têm Silva no nome, não nasceram no Brasil e pesam menos de 100 Kg.
#6) Qual é a maior altura entre gafanhotos Homens que moram no Brasil?
#7) Qual é a média de peso dos gafanhotos cadastrados?
#8) Qual é o menor peso entre os gafanhotos Mulheres que nasceram fora do Brasil e entre 01/Jan/1990 e 31/Dez/2000?
#9) Quantas gafanhotos Mulheres tem mais de 1.90cm de altura?

#exercio 1
select nome from gafanhotos
where sexo = 'F';

#exercio 2
select * from gafanhotos
where nascimento between '2000-01-01' and '2015-12-31';

#exercio 3
select nome from gafanhotos
where profissao = 'programador' and sexo = 'M';

#exercio 4
select * from gafanhotos
where nacionalidade = 'brasil' and sexo = 'F' and nome like 'j%';

#exercio 5
select nome, nacionalidade from gafanhotos
where sexo = 'M' and nome like '%silva%' and nacionalidade != 'brasil' and peso < '100';

#exercio 6
select nome, max(altura) from gafanhotos
where sexo = 'M' and nacionalidade = 'brasil';

#exercio 7
select avg(peso) from gafanhotos;

#exercio 8
select min(peso) from gafanhotos
where sexo = 'F' and nacionalidade != 'brasil' and nascimento between '1990-01-01' and '2000-12-31';

#exercio 9
select count(altura) from gafanhotos
where sexo = 'F' and altura > '1.90';





