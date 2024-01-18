-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT Ts.title, Tsg.genre_id
FROM tv_shows Ts LEFT JOIN tv_show_genres Tsg
ON Ts.id = Tsg.show_id
WHERE Tsg.show_id IS NULL
ORDER BY Ts.title, Tsg.genre_id;