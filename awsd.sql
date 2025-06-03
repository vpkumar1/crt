create database student_management;
use student_management;
create table student(
     roll_no varchar(20) primary key,
     name varchar(100),
     class varchar(20),
     section varchar(5),
     password varchar