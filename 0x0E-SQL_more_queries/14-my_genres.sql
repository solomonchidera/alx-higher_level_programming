-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT Tg.name
FROM tv_genres Tg, tv_show_genres Tsg, tv_shows Ts
WHERE Tg.id = Tsg.genre_id
AND Tsg.show_id = Ts.id
AND Ts.title = 'Dexter'
ORDER BY Tg.name;