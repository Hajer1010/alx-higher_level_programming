-- A script that uses the hbtn_0d_tvshows database to list
SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.name NOT IN (
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;
