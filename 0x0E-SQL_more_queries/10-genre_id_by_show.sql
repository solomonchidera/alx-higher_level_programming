-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
SELECT Ts.title, Tsg.genre_id
FROM tv_shows Ts, tv_show_genres Tsg
Where Ts.id = Tsg.show_id
ORDER BY Ts.title, Tsg.genre_id;