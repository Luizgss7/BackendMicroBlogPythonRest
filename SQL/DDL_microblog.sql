DROP TABLE user_follow;
drop table post;
drop table users;

create table users (
	id serial primary key,
	login varchar (50) not null unique,
	password varchar (100) not null,
	create_date timestamp not null default now()
);

create table post (
	id serial primary key,
	text varchar (200) not null,
	user_id integer not null references users(id),
	create_date timestamp not null default now()	
);

create table user_follow (
    user_id_follower integer not null references users(id),
    user_id_following integer not null references users(id),
    create_date timestamp not null default now(),
    PRIMARY KEY (user_id_follower, user_id_following)
);



ALTER TABLE user_follow 
ADD CONSTRAINT check_self_follow 
CHECK (user_id_follower <> user_id_following);

