create database prova;

use prova;

create table nomes (
id int primary key,
nome varchar(50) not null
);

create table enderecos (
id_nome int primary key foreign key references nomes(id),
endereco varchar(200) not null,
);

insert into nomes (id, nome)
values 
(1,'Ana'),
(2,'Beatriz'),
(3,'Caio'),
(4,'Bianca'),
(5,'Célia');

insert into enderecos (id_nome, endereco)
values
(1,'Rua 1'),
(2,'Rua 3'),
(4,'Rua 12'),
(3,'Rua Gaivota'),
(5,'Rua Barão');

SELECT * FROM nomes AS N
JOIN enderecos AS E ON N.id = E.id_nome
where nome like 'B%';