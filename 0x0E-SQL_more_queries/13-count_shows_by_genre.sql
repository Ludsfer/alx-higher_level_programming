-- A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT
	name AS "genre",
	COUNT("show_id") AS "number_of_shows"
FROM
	tv_show_genres
	INNER JOIN tv_genres ON id = genre_id
GROUP BY
	name
ORDER BY
	number_of_shows DESC
