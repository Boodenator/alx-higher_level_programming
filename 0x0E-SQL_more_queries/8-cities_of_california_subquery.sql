-- script for listing of all the cities of California which found in database hbtn_0d_usa

SELECT id,
	name
FROM cities
WHERE state_id = (
		SELECT id
		FROM states
		WHERE name = 'California'
	)
ORDER BY id;
