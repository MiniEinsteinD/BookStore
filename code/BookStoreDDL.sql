create table IF NOT EXISTS User(
    username    varchar(15)     UNIQUE  NOT NULL,
    first_name  varchar(15)     NOT NULL,
    last_name  varchar(15)     NOT NULL,
    password    varchar(15)     NOT NULL, /* change it to char with limited chars maybe!!*/
    primary key (username)
)

create table IF NOT EXISTS Owner(
    username    varchar(15)     UNIQUE  NOT NULL,
    first_name  varchar(15)     NOT NULL,
    last_name  varchar(15)     NOT NULL,
    primary key (username)
)

create table IF NOT EXISTS Publisher(
    email_address
)