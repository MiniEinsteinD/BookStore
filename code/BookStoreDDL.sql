create table IF NOT EXISTS User
    (
    username    varchar(15)     UNIQUE  NOT NULL,/* Add to decision/discuss 15 length*/
    first_name  varchar(15)     NOT NULL,
    last_name  varchar(15)     NOT NULL,
    password    varchar(15)     NOT NULL, /* change it to char with limited chars maybe!!*/
    primary key (username)
    );

create table IF NOT EXISTS Owner
    (
    username    varchar(15)     UNIQUE  NOT NULL,
    first_name  varchar(15)     NOT NULL,
    last_name  varchar(15)     NOT NULL,
    password    varchar(15)     NOT NULL,
    balance     float       NOT NULL,
    primary key (username)
    );

create table IF NOT EXISTS Publisher
    (
    email_address   varchar(15)     UNIQUE  NOT NULL,
    first_name  varchar(15)     NOT NULL,
    last_name  varchar(15)     NOT NULL,
    password    varchar(15)     NOT NULL,
    balance     float       NOT NULL,
    primary key (email_address)
    );

create table IF NOT EXISTS Book
    (
    ISBN   INT      UNIQUE  NOT NULL, 
    name    varchar(50)     NOT NULL,
    page_num    INT     NOT NULL,
    price   float     NOT NULL, /*float might not work*/ 
    publisher_percentage    float    NOT NULL,
    publisher       varchar(15)     UNIQUE  NOT NULL,
    primary key (ISBN),
    foreign key (publisher) references Publisher (email_address)
    );

/*Disscus not null*/
create table IF NOT EXISTS Address
    (
    postal_code     varchar(6)      UNIQUE  NOT NULL,
    unit_num    INT     NOT NULL,
    street_name     varchar(30)     NOT NULL,
    city        varchar(15)     NOT NULL,
    province    char(2)     NOT NULL,
    country     varchar(15)     NOT NULL,
    primary key(postal_code)
    );

create table IF NOT EXISTS Bank
    (
    account_number     INT      UNIQUE  NOT NULL,
    password    varchar(15)     NOT NULL,
    balance     float       NOT NULL,
    primary key (account_number)
    );

create table IF NOT EXISTS Orders
    (
    username    varchar(15)     UNIQUE  NOT NULL,
    postal_code     varchar(6)      UNIQUE  NOT NULL,
    order_num    INT     NOT NULL, /*not sure*/
    traking_info    varchar(50)     NOT NULL,
    order_date      DATE    NOT NULL,
    total_price   float     NOT NULL,
    primary key (username),
    foreign key (username) references User (username),
    foreign key (postal_code) references Address (postal_code) 
    );

create table IF NOT EXISTS Collecion
    (
    owner   varchar(15)     UNIQUE  NOT NULL,
    ISBN   INT      UNIQUE  NOT NULL,
    quantity    INT     NOT NULL,
    primary key (owner),
    foreign key (owner) references Owner (username),
    foreign key (ISBN) references Book (ISBN) 
    );

create table IF NOT EXISTS Phone
    (
    publisher    varchar(15)    UNIQUE  NOT NULL,
    phone  varchar(10)      NOT NULL,
    primary key (publisher),
    foreign key (publisher) references Publisher (email_address)
    );

create table IF NOT EXISTS Is_Author
    (
    ISBN   INT      UNIQUE  NOT NULL,
    first_name  varchar(15)     NOT NULL,
    last_name  varchar(15)     NOT NULL,
    primary key (ISBN),
    foreign key (ISBN) references Book (ISBN) 
    );

create table IF NOT EXISTS Is_Genre
    (
    ISBN   INT      UNIQUE  NOT NULL,
    genre    varchar(15)     NOT NULL,
    primary key (ISBN),
    foreign key (ISBN) references Book (ISBN) 
    );

create table IF NOT EXISTS Lives_At
    (
    resident    varchar(15)    UNIQUE  NOT NULL,
    post_code  varchar(6)     UNIQUE  NOT NULL,
    primary key (resident),
    foreign key (resident) references User (email_address),
    foreign key (post_code) references Address (postal_code) 
    );

create table IF NOT EXISTS Works_At
    (
    publisher    varchar(15)    UNIQUE  NOT NULL,
    post_code  varchar(6)     UNIQUE  NOT NULL,
    primary key (publisher),
    foreign key (publisher) references Publisher (email_address),
    foreign key (post_code) references Address (postal_code) 
    );

create table IF NOT EXISTS User_Banking
    (
    account_holder  varchar(15)   UNIQUE  NOT NULL,
    account_number  INT UNIQUE  NOT NULL,
    primary key (account_number),
    foreign key (account_holder) references User (username)
    );