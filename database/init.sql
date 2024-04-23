-- Check if the database exists
SELECT IF( EXISTS (SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'mydatabase'), 'Database exists', 'Database does not exist') AS db_exist;

-- If the database does not exist, create it
CREATE DATABASE IF NOT EXISTS mydatabase;

-- Switch to the newly created database
USE mydatabase;

-- Continue with the rest of your script...


-- Switch to the newly created database
create table inventory(
product_id int auto_increment,
product_name varchar(40),
quantity int,
unit_price float,
location varchar(50),
primary key(product_id,location)
);

insert into inventory values (1,'sdf',10,1,'kle');
insert into inventory values (4,'tyu',100,1,'kle');
insert into inventory values (5,'iop',100,1,'ke');
select * from inventory;

create table users(
id int primary key auto_increment,
name varchar(50),
password varchar(50)
);
insert users values(1,'abc',123);


select * from users;

create table orders(
	order_id int auto_increment primary key,
	userid int ,
    productname varchar(40),
    quantity int,
    price float,
    stats varchar(50) not null,
    FOREIGN KEY(userid) REFERENCES users(id) on delete cascade
    
);

create table health(
	containername varchar(60) primary key,
    stat varchar(20) not null
    );


insert into health values('itemcreation','u');
insert into health values('stockmanagement','u');
insert into health values('orderprocessing','u');


create table admins(
	id int auto_increment primary key ,
    name varchar(50),
    password varchar(50)
    );
    
insert admins values(1,'admin',123);
