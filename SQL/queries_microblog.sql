select * from post;

select * from users;

select p.id,
	   p.text,
	   u.login,
	   p.create_date
from post p
   join users u on p.user_id = u.id
where u.login = 'Login'
;

SELECT * FROM user_follow WHERE user_id_origin = user_id_destiny;

SELECT 
	p.id,	
    u.login,
    p.text,
    p.create_date
FROM user_follow f
JOIN post p ON f.user_id_following = p.user_id
JOIN "users" u ON p.user_id = u.id
WHERE f.user_id_follower = 1
ORDER BY p.create_date DESC;

SELECT 
	p.id,	
    u.login,
    p.text,
    p.create_date
from post p
join user_follow uf on p.user_id = uf.user_id_following
join users u on uf.user_id_follower = u.id
where uf.user_id_follower = 1
ORDER BY p.create_date DESC;