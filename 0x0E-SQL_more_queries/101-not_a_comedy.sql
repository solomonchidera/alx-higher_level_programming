-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT Ts.title
FROM tv_shows Ts
LEFT JOIN
( 	SELECT Ts1.id, Ts1.title
	From  tv_shows Ts1, tv_genres Tg, tv_show_genres Tsg
	WHERE Ts1.id = Tsg.show_id
	AND Tsg.genre_id = Tg.id
	AND Tg.name = 'Comedy'
) Comedy_shows
ON Comedy_shows.id = Ts.id
WHERE Comedy_shows.id IS NULL
ORDER BY Ts.title;