create table IF NOT EXISTS User(
    username    varchar(15)     UNIQUE  NOT NULL,/* Add to decision/discuss 15 length*/
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
    email_address   varchar(15)     UNIQUE  NOT NULL,
    first_name  varchar(15)     NOT NULL,
    last_name  varchar(15)     NOT NULL,
    primary key (email_address)
)

create table IF NOT EXISTS Book(

)
/*Disscus not null*/
create table IF NOT EXISTS Address(
    postal_code     varchar(6)      UNIQUE  NOT NULL,
    unit_num    INT,
    street_name     varchar(30),
    city        varchar(15),
    province    char(2),
    country     varchar(15),
    primary key(postal_code)
)

create table IF NOT EXISTS Bank(

)

create table IF NOT EXISTS Order(

)

create table IF NOT EXISTS Collecion(

)

create table IF NOT EXISTS Phone(

)

create table IF NOT EXISTS Is_Author(

)

create table IF NOT EXISTS Is_Genre(

)

create table IF NOT EXISTS Lives_At(
    resident    varchar(15)    UNIQUE  NOT NULL,
    post_code  varchar(6)     UNIQUE  NOT NULL,
    primary key (resident),
    primary key (post_code),
    foreign key (resident) references User (email_address),
    foreign key (post_code) references Address (postal_code) 
)

create table IF NOT EXISTS Works_At(
    publisher    varchar(15)    UNIQUE  NOT NULL,
    post_code  varchar(6)     UNIQUE  NOT NULL,
    primary key (publisher),
    primary key (post_code),
    foreign key (publisher) references Publisher (email_address),
    foreign key (post_code) references Address (postal_code) 
)

create table IF NOT EXISTS User_Banking(
    user    varchar(15)    UNIQUE  NOT NULL,
    account_number  INT     UNIQUE  NOT NULL,
    primary key(user),
    foreign key (user) references User (username) 
)

create table IF NOT EXISTS Owner_Banking(
    owner    varchar(15)    UNIQUE  NOT NULL,
    account_number  INT     UNIQUE  NOT NULL,
    primary key(owner),
    foreign key (owner) references Owner (username) 
)

create table IF NOT EXISTS Publisher_Banking(
    publisher    varchar(15)    UNIQUE  NOT NULL,
    account_number  INT     UNIQUE  NOT NULL,
    primary key(publisher),
    foreign key (publisher) references Publisher (email_address) 
)