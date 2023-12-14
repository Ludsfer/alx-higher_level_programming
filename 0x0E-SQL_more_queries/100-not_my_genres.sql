-- A script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
SELECT DISTINCT
	name
FROM
	tv_genres
	INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
	INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE
	tv_genres.name NOT IN (
		SELECT
			name
		FROM
			tv_genres
			INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
			INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
		WHERE
			title = 'Dexter'
	)
ORDER BY
	name ASC;
