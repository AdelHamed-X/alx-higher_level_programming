-- A script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT tv_shows.title, COALESCE(tv_show_genres.genre_id, NULL) AS genre_id
FROM tv_show_genres
RIGHT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, COALESCE(tv_show_genres.genre_id, NULL) ASC;