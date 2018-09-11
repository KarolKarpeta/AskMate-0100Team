-- TO CREATE NEW TABLE terminal -> psql [your database] -> \i askmatepart3-users-table.sql THX FOR READING


DROP TABLE IF EXISTS public.users;
create table users(
user_id serial unique primary key,
user_name text not null unique,
password text not null,
registration_date timestamp without time zone default now()
);