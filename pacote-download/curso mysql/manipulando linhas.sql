insert into cursos values
('1', 'html', 'Curso de HTML', '40', '37', '2014'),
('2', 'Algoritmos', 'Lógica de programção', '20', '15', '2014'),
('3', 'Photoshop', 'Dicas de photoshop CC', '10', '8', '2014'),
('4', 'PGP', 'Curso de PHP para iniciantes', '40', '20', '2010'),
('5', 'Jarva', 'Introdução a linguagem java', '10', '29', '2000'),
('6', 'MySQL', 'Banco de dados MySQL', '30', '15', '2016'),
('7', 'WORD', 'Curso completo de Word', '40', '30', '2016'),
('8', 'Sapateado', 'Danças rítmicas', '40', '30', '2018'),
('9', 'Cozinha Árabe', 'Aprenda a fazer kibe', '40', '30', '2018'),
('10', 'Youtuber', 'Gerar polêmica e ganhar inscritos', '5', '2', '2018');

update cursos
set nome = 'PHP', ano = '2015'
where idcurso = '4';

update cursos
set nome = 'JAVA', carga = '40', ano = '2015'
where idcurso = '5'
limit 1;
select * from cursos;
delete from cursos
where ano = '2018';

