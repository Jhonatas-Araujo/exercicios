create database cadastro
default character set utf8
default collate utf8_general_ci;

create table pessoas (
id int not null auto_increment,
nome varchar(30) not null,
nascimento date, 
sexo enum ('M','F'),
peso decimal(5,2),
altura decimal (3,2),
nacionalidade varchar(20) default 'Brasil',
primary key (id)
) default charset = utf8;

insert into pessoas values
(default, 'Jhon', '2000-08-01', 'M', '70.8', '1.73', 'Brasil'),
(default, 'Guilherme', '1997-10-02', 'M', '73.5', '1.72', default),
(default, 'Bia', '1994-11-28', 'F', '64.7', '1.68', default),
(default, 'Amy', '2019-12-15', 'F', '18.7', '0.90', default);
select * from pessoas

