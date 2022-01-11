create table tb_students(
id serial primary key,
name varchar(30),
age integer,
fp_language varchar(30),
sp_language varchar(30)
)
insert into tb_students values(1,'Bakyt',23,'Python','C++')
insert into tb_students values(2,'Aygul',46,'Python','Java')
insert into tb_students values(3,'Jika',13,'C','Ruby_On_Rails')
insert into tb_students values(4,'Ermek',16,'Java','C')
insert into tb_students values(5,'Artem',55,'C#','Java')
insert into tb_students values(6,'Roma',31,'Pascal','C')
insert into tb_students values(7,'Beka',25,'C#','Javascript')

select s.name,
       s.fp_language,
       s.sp_language
from tb_students as s;

select name
from tb_students
where age > 30;

select from tb_students
where fp_language = 'Python' or fp_language = 'C#';

delete from tb_students
where id = 1 and id = 3 and id = 5 and id = 7;

select min(age), 
       name ,
       sp_language,
       fp_language
       
from tb_students  
where fp_language ='Java' or sp_language ='Java'
group by name, sp_language, fp_language
order by min(age) ask;

select min(age), 
       name 
from tb_students  
group by name
order by min(age) ask;

drop table tb_students;

DROP DATABASE programmers


