create table clientID (
    clientID int primary key,
    cpf int(12),
    tel varchar(15),
    view enum('0','1'),
    public enum('0','1')
);

create table vendas (
    clientID int,
    produtoID int,
    price float
);