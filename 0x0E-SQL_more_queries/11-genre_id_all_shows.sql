-- script that  lists all shows contained in the database hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL
SELECT Ts.title, Tsg.genre_id
FROM tv_shows Ts LEFT OUTER JOIN tv_show_genres Tsg
ON Ts.id = Tsg.show_id
ORDER BY Ts.title, Tsg.genre_id;