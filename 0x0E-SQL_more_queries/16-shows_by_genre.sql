-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT Ts.title, Tg.name
FROM tv_shows Ts
LEFT JOIN tv_show_genres Tsg
ON Ts.id = Tsg.show_id
LEFT JOIN tv_genres Tg
ON Tsg.genre_id = Tg.id
ORDER BY Ts.title, Tg.name;