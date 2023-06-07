use db;

create table contatos(
	email varchar(60) not null unique,
    assunto varchar(60) not null,
    descricao varchar(255) not null
);

select * from contatos;