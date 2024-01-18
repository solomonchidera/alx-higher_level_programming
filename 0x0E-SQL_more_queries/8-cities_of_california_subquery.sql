-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT c.id, c.name 
FROM cities c, states s
where c.state_id = s.id
AND s.name = 'California'
ORDER BY c.id;