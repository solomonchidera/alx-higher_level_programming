-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT Ts.title
FROM tv_genres Tg, tv_show_genres Tsg, tv_shows Ts
WHERE Tg.name = 'Comedy'
AND Tg.id = Tsg.genre_id
AND Tsg.show_id = Ts.id
ORDER BY Ts.title;