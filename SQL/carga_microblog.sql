INSERT INTO users
(login, password)
VALUES('Login1', 'Pass1');

INSERT INTO users
(login, password)
VALUES('Login2', 'Pass2');

INSERT INTO post
(text, user_id)
VALUES('Texto1', 1);

INSERT INTO post
(text, user_id)
VALUES('Texto2', 1);

INSERT INTO post
(text, user_id)
VALUES('Texto3', 2);

INSERT INTO post
(text, user_id)
VALUES('Texto4', 2);

insert into user_follow 
(user_id_follower, user_id_following)
values (1, 2);