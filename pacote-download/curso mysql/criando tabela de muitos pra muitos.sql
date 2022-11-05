create table g_assiste_c (
id int not null auto_increment,
data date,
idgafanhoto int,
idcurso int,
primary key (id),
foreign key	(idgafanhoto) references gafanhotos(id),
foreign key	(idcurso) references cursos(idcurso)
) default charset = utf8;

insert into g_assiste_c values
(default, '2014-03-01', '1', '2');

select * from g_assiste_c;

select g.nome, c.nome from gafanhotos g
join g_assiste_c a
on g.id = a.idgafanhoto
join cursos c
on c.idcurso = a.idcurso
order by g.nome;
