create table tb_outter_flights(
id serial primary key,
from_country varchar(30),
to_country varchar(30),
flight_type varchar(30),
company varchar(30),
neighbors integer
);


insert into tb_outter_flights values(1,'USA','Germany','passenger','American Express',5)
insert into tb_outter_flights values(2,'Turkey','Germany','ship','Pegasus',3)
insert into tb_outter_flights values(3,'Kazakhstan','Turkey','pleasure','Turkish Airlines',2)
insert into tb_outter_flights values(4,'Russia','OAE','VIP','Dubai airlines',1)
insert into tb_outter_flights values(5,'USA','Germany','other','American Express',4)
insert into tb_outter_flights values(6,'France','Japan','passenger','France airlines',2)
insert into tb_outter_flights values(7,'China','Germany','ship','China airlines',7)
insert into tb_outter_flights values(8,'Italy','Germany','passenger','Das airlines',5)
insert into tb_outter_flights values(9,'China','USA','business','American Express',4)
insert into tb_outter_flights values(10,'Canada','Mexica','ship','Canadian Express',5)
insert into tb_outter_flights values(11,'Brazil','England','business','British airlines',3)
insert into tb_outter_flights values(12,'Costa-Rica','Turkey','tourism','American Express',5)
insert into tb_outter_flights values(13,'Australia','Nigeria','tourism','Australian airlines',2)
insert into tb_outter_flights values(14,'Uzbekistan','Russia','ship','Ural airlines',7)
insert into tb_outter_flights values(15,'Japan','Indonesia','tourism','Tokio airliens',3)
select *from tb_outter_flights

create table tb_inner_flights(
id serial primary key,
from_region varchar(30),
to_destination varchar(30),
company varchar(30),
quantity integer
);

insert into tb_inner_flights values(1,'Osh','Bishkek','Aviatraffic',71)
insert into tb_inner_flights values(2,'Osh','Bishkek','Aviatraffic',120)
insert into tb_inner_flights values(3,'Bishkek','Osh','Pegasus',200)
insert into tb_inner_flights values(4,'Bishkek','Osh','Pegasus',158)
insert into tb_inner_flights values(5,'Bishkek','Osh','Pegasus',179)
insert into tb_inner_flights values(6,'Bishkek','Tamga','Aviatraffic',166)
insert into tb_inner_flights values(7,'Bishkek','Tamga','Aviatraffic',138)
insert into tb_inner_flights values(8,'Bishkek','Tamga','Aviatraffic',191)
insert into tb_inner_flights values(9,'Osh','Tamga','Kyrgyzconcept',141)
insert into tb_inner_flights values(10,'Osh','Tamga','Kyrgyzconcept',120)
insert into tb_inner_flights values(11,'Osh','Tamga','Kyrgyzconcept',180)
insert into tb_inner_flights values(12,'Bishkek','Batken','Pegasus',190)
insert into tb_inner_flights values(13,'Bishkek','Batken','Pegasus',190)
insert into tb_inner_flights values(14,'Bishkek','Batken','Pegasus',190))
insert into tb_inner_flights values(15,'Batken','Bishkek','Aviatraffic',180)

select *from tb_inner_flights;

select *from tb_inner_flights where id > 10;

select *from tb_inner_flights 
where to_destination = 'Osh' or to_destination = 'Bishkek';

select *from tb_inner_flights where quantity > 150;

select *from tb_outter_flights
where flight_type = 'ship';

select *from tb_outter_flights
where neighbors > 3;

select *from tb_outter_flights
where neighbors <3 and flight_type = 'passenger';

select  o.company,
        o.to_country
from tb_outter_flights as o;

