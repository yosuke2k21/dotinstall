drop table if exists users;

-- テーブルの作成
create table users (
  id int unsigned primary key auto_increment,
  name varchar(20),
  score float not null
);

-- レコードを挿入
insert into users (name, score) values
  ('taguchi', 5.8),
  ('fkoji', 8.2),
  ('dotinstall', 6.1),
  ('yamada', null);

select * from users;


-- select * from users where score >= 6.0;
-- select * from users where score >= 3.0 and score <= 6.0;
-- select * from users where score between 3.0 and 6.0;
-- select * from users where name = 'taguchi' or name = 'fkoji';
-- select * from users where name in ('taguchi', 'fkoji');


-- select * from users where name like 't%'; 
-- select * from users where name like '%a%';
-- select * from users where name like '%a';
-- select * from users where name like 'T%';
-- select * from users where name like binary 'T%';
-- select * from users where name like '______';
-- select * from users where name like '_a%';


-- select * from users order by score;
-- select * from users where score is not null order by score desc;
-- select * from users limit 3;
-- select * from users limit 3 offset 3;
-- select * from users order by score desc limit 3;


-- update users set score = 5.9;
-- update users set score = 5.9 where id = 1;
-- update users set name = 'sasaki', score = 2.9 where name = 'tanaka';

-- delete from users;
-- delete from users where score < 5.0;


-- update users set score = score * 1.2 where id % 2 = 0;
-- select * from users;
-- select round(5.355); -- 5
-- select round(5.355, 1); -- 5.4
-- select floor(5.833); -- 5
-- select ceil(5.238); -- 6
-- select rand();



























