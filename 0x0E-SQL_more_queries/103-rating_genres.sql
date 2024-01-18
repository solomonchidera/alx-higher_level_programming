-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT Tg.name, SUM(rate) rating
FROM tv_genres Tg, tv_show_ratings Tsr, tv_show_genres Tsg
WHERE Tg.id = Tsg.genre_id
AND Tsg.show_id = Tsr.show_id
GROUP BY Tg.name
ORDER BY rating DESC;