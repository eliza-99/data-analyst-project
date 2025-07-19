create table game_details(
	user_id bigint ,
	date date,
	slot varchar(100),
	total_games bigint,
	total_deposit numeric(10,2),
	deposit_count bigint,
	total_withdrawl numeric(10,2),
	withdrawl_count bigint
)
select * from game_details limit 10;
alter table game_details
add column difference_count bigint;
update  game_details
set difference_count= 
case when (deposit_count-withdrawl_count)>0 then (deposit_count-withdrawl_count)
else 0
end ;
alter table game_details
add column loyalty_point numeric(10,2);
update game_details
set loyalty_point=(0.01*total_deposit)+(0.005*total_withdrawl)+(0.001*difference_count)+(0.2*total_games);


create table playerwise_loyalty_point_2nd_oct_slot1 as
select user_id,date,slot,loyalty_point
from game_details
where date='2022-10-02' and slot='slot1';
select * from playerwise_loyalty_point_2nd_oct_slot1;

create table playerwise_loyalty_point_16th_oct_slot2 as
select user_id,date,slot,loyalty_point
from game_details
where date='2022-10-16' and slot='slot2';
select * from playerwise_loyalty_point_16th_oct_slot2;

create table playerwise_loyalty_point_18th_oct_slot1 as
select user_id,date,slot,loyalty_point
from game_details
where date='2022-10-18' and slot='slot1';
select * from playerwise_loyalty_point_18th_oct_slot1;

create table playerwise_loyalty_point_26th_oct_slot2 as
select user_id,date,slot,loyalty_point
from game_details
where date='2022-10-26' and slot='slot2';
select * from playerwise_loyalty_point_26th_oct_slot2;

create table avg_deposit as
select avg(total_deposit) as average_deposit
from game_details;
select * from avg_deposit;

create table avg_deposit_per_user AS
SELECT user_id, AVG(total_deposit) AS average_deposit
FROM game_details
WHERE total_deposit > 0
GROUP BY user_id;
SELECT * FROM avg_deposit_per_user;

create table avg_game_played_per_user as
SELECT user_id, AVG(total_games) AS average_game_played
FROM game_details
WHERE total_games > 0
GROUP BY user_id;
select * from avg_game_played_per_user;

create table top_players as
select user_id,sum(loyalty_point) as total_loyalty_point 
from game_details
 group by user_id
 order by total_loyalty_point desc ;
 

 select *from top_players limit 50;



