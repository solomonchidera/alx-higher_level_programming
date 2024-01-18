-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT Tg.name
FROM tv_genres Tg
LEFT JOIN (SELECT tg1.id, tg1.name 
		FROM tv_genres tg1, tv_show_genres Tsg, tv_shows Ts
		WHERE tg1.id = Tsg.genre_id
		AND Tsg.show_id = Ts.id
		AND Ts.title = 'Dexter'
) genre_Dexter
ON genre_Dexter.id = Tg.id
WHERE genre_Dexter.id IS NULL
ORDER BY Tg.name;