-- list records in specific format as shown in task 16 description
SELECT
	score,
	name
FROM
	third_table
WHERE
	name IS NOT NULL
ORDER BY
	score DESC;
