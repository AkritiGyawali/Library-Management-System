create database library;
use library;
create table book(
 book_name varchar(50),
 book_id int primary key,
 no_of_book int
);
create table login(
username varchar(100) primary key,
password varchar(255) not null
);
create table student(

student_name varchar(50),
student_id int primary key
);
alter table student 
add column email varchar(100),
add column phone_number varchar(50);

create table book_issued(

student_id int ,
book_id int ,
issued_date date,
due_date date,
return_date date,
foreign key (student_id) references student(student_id),
foreign key (book_id) references book(book_id)
);
drop table book_issued;

insert into book
(book_name,book_id,no_of_book)
values
("karnali blues",101,3);

insert into student
(student_name,student_id)
values
("Akriti Gyawali",1001);

select * from book 
where book_id=101 AND no_of_book>0;

insert into book_issued
(student_id,book_id,issued_date,due_date)
values
(1001,101,'2008-2-5','2008-5-5');
SET SQL_SAFE_UPDATES=0;
update book
set no_of_book=no_of_book-1
where book_id=101;
select * from book;
select* from book_issued;

select *
from book_issued
where student_id=1001;

update book_issued
set return_date=curdate()
where student_id=1001 and return_date is null;

SELECT s.student_name, b.book_name, i.issued_date, i.due_date, i.return_date
FROM book_issued i
inner JOIN student s ON i.student_id = s.student_id
 inner JOIN book b ON i.book_id = b.book_id;
 
 select * from student;
 

