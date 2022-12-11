create table IF NOT EXISTS Users
    (
    username    varchar(15)     UNIQUE  NOT NULL,
    first_name  varchar(15)     NOT NULL,
    last_name  varchar(15)      NOT NULL,
    password    varchar(15)     NOT NULL, 
    balance     DECIMAL         NOT NULL,
    primary key (username)
    );

create table IF NOT EXISTS Owner
    (
    username    varchar(15)     UNIQUE  NOT NULL,
    first_name  varchar(15)     NOT NULL,
    last_name  varchar(15)      NOT NULL,
    password    varchar(15)     NOT NULL,
    balance     DECIMAL         NOT NULL,
    primary key (username)
    );

create table IF NOT EXISTS Publisher
    (
    email_address   varchar(15)     UNIQUE  NOT NULL,
    first_name      varchar(15)     NOT NULL,
    last_name       varchar(15)     NOT NULL,
    password        varchar(15)     NOT NULL,
    balance         DECIMAL         NOT NULL,
    primary key (email_address)
    );

create table IF NOT EXISTS Book
    (
    ISBN                    varchar(13)     UNIQUE  NOT NULL, 
    name                    varchar(50)     NOT NULL,
    page_num                INT             NOT NULL,
    price                   DECIMAL         NOT NULL,
    publisher_percentage    DECIMAL         NOT NULL,
    publisher               varchar(15)     NOT NULL,
    primary key (ISBN),
    foreign key (publisher) references Publisher (email_address)
    );

create table IF NOT EXISTS Address
    (
    postal_code     varchar(6)      UNIQUE  NOT NULL,
    unit_num        INT             NOT NULL,
    street_name     varchar(30)     NOT NULL,
    city            varchar(15)     NOT NULL,
    province        char(2)         NOT NULL,
    country         varchar(15)     NOT NULL,
    primary key(postal_code)
    );

create table IF NOT EXISTS Orders
    (
    username        varchar(15)     NOT NULL,
    postal_code     varchar(6)      NOT NULL,
    order_num       varchar(15)     NOT NULL, 
    traking_info    varchar(50)     NOT NULL,
    order_date      DATE            NOT NULL,
    total_price     DECIMAL         NOT NULL,
    from_owner      varchar(15)     NOT NULL,
    primary key (username, postal_code, order_num),
    foreign key (username) references Users (username),
    foreign key (postal_code) references Address (postal_code) 
    foreign key (from_owner) references Owner(username) 
    );

create table IF NOT EXISTS Collection
    (
    owner           varchar(15)      NOT NULL,
    ISBN            varchar(13)      NOT NULL,
    collection_name varchar(50)      UNIQUE  NOT NULL, 
    quantity        INT     NOT NULL,
    primary key (owner, ISBN, collection_name),
    foreign key (owner) references Owner (username),
    foreign key (ISBN) references Book (ISBN) 
    );

create table IF NOT EXISTS Phone
    (
    publisher    varchar(15)      NOT NULL,
    phone        varchar(10)      NOT NULL,
    primary key (publisher, phone),
    foreign key (publisher) references Publisher (email_address)
    );

create table IF NOT EXISTS Is_Author
    (
    ISBN        varchar(13)     NOT NULL,
    first_name  varchar(15)     NOT NULL,
    last_name   varchar(15)     NOT NULL,
    primary key (ISBN, first_name, last_name),
    foreign key (ISBN) references Book (ISBN) 
    );

create table IF NOT EXISTS Is_Genre
    (
    ISBN     varchar(13)     NOT NULL,
    genre    varchar(15)     NOT NULL,
    primary key (ISBN, genre),
    foreign key (ISBN) references Book (ISBN) 
    );

create table IF NOT EXISTS Lives_At
    (
    resident    varchar(15)    NOT NULL,
    postal_code   varchar(6)     NOT NULL,
    primary key (resident, postal_code),
    foreign key (resident) references Users (username),
    foreign key (postal_code) references Address (postal_code) 
    );

create table IF NOT EXISTS Works_At
    (
    publisher    varchar(15)    NOT NULL,
    postal_code    varchar(6)     NOT NULL,
    primary key (publisher, postal_code),
    foreign key (publisher) references Publisher (email_address),
    foreign key (postal_code) references Address (postal_code) 
    );

create table IF NOT EXISTS In_Order 
    (
    order_num    varchar(15)     NOT NULL, 
    ISBN         varchar(13)     NOT NULL, 
    quantity     INT             NOT NULL,
    primary key (order_num, ISBN),
    foreign key (order_num) references Orders (order_num),
    foreign key (ISBN) references Book (ISBN)
    );
