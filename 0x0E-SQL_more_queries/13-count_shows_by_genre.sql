-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT Tg.name genre, count(*) number_of_shows
FROM tv_genres Tg, tv_show_genres Tsg
WHERE Tg.id = Tsg.genre_id
GROUP BY Tg.name
ORDER BY number_of_shows DESC;