# Write your MySQL query statement below
(select u.name as results
from users u right join MovieRating mr on 
u.user_id = mr.user_id
group by u.name
order by count(mr.user_id) desc, u.name asc
limit 1
)
union all
(select m.title as results
from movies m right join movierating mr on
m.movie_id = mr.movie_id
where mr.created_at between "2020-02-01" and "2020-02-29"
group by m.title
order by avg(rating) desc,m.title asc
limit 1)