/*
example to help create our ddl
*/
create table IF NOT EXISTS User   
    (   
        Fname  varchar(15)	NOT NULL,
        Minit   char(1),
        Lname    varchar(15)	NOT NULL,
        Ssn     char(9)	NOT NULL,
        Bdate   DATE,
        Address varchar(30),
        Sex     char(1),
        Salary  numeric(10, 2),
        Super_ssn   char(9),
        Dno     INT		NOT NULL,
        primary key (Ssn),
        foreign key (Super_ssn) references EMPLOYEE (Ssn)
    );

create table IF NOT EXISTS DEPARTMENT
    (   
        Dname		varchar(15)	UNIQUE	NOT NULL,
        Dnumber     INT	NOT NULL,
        Mgr_ssn     char(9),
        Mgr_start_date      DATE,
		primary key (Dnumber),
		foreign key (Mgr_ssn) references EMPLOYEE (Ssn)
	);

create table IF NOT EXISTS DEPT_LOCATIONS
    (   
        Dnumber     INT		NOT NULL,
        Dlocation     varchar(15)	NOT NULL,
		primary key (Dnumber, Dlocation),
		foreign key (Dnumber) references DEPARTMENT (Dnumber)
	);

create table IF NOT EXISTS PROJECT
    (   
        Pname     varchar(15)	UNIQUE	NOT NULL,
        Pnumber     INT,
        Plocation     varchar(15)	NOT NULL,
        Dnum        INT	NOT NULL,
        primary key (Pnumber),
        foreign key (Dnum) references DEPARTMENT (Dnumber)
	);

create table IF NOT EXISTS WORKS_ON
    (   
        Essn     char(9)	NOT NULL,
        Pno     INT	NOT NULL,
        Hours     numeric(3, 1)	NOT NULL,
        primary key (Essn, Pno),
		foreign key (Essn) references EMPLOYEE (Ssn),
		foreign key (Pno) references PROJECT (Pnumber)
	);

create table IF NOT EXISTS DEPENDENT
    (   
        Essn     char(9)	NOT NULL,
        Dependent_name  varchar(15)	NOT NULL,
        Sex     char(1),
		Bdate   DATE,
        Relationship varchar(8),
		primary key (Essn, Dependent_name),
		foreign key (Essn) references EMPLOYEE (Ssn)
	);

ALTER TABLE EMPLOYEE
	ADD foreign key (Dno) references DEPARTMENT (Dnumber);