# SQL_more_queries

More SQL with MySQL: users and privileges, constraints, keys, foreign keys,
subqueries, joins and aggregates.

Run a script like this (the database name is passed as an argument when needed):

```
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
```

Tasks 10 to 16 need the `hbtn_0d_tvshows` database dump imported first.

| File | Description |
|------|-------------|
| 0-privileges.sql | Lists the privileges of `user_0d_1` and `user_0d_2` (localhost) |
| 1-create_user.sql | Creates `user_0d_1` with all privileges and the password `user_0d_1_pwd` |
| 2-create_read_user.sql | Creates `hbtn_0d_2` and `user_0d_2` with only `SELECT` on it |
| 3-force_name.sql | Creates `force_name` (`name` can not be null) |
| 4-never_empty.sql | Creates `id_not_null` (`id` defaults to 1) |
| 5-unique_id.sql | Creates `unique_id` (`id` unique, defaults to 1) |
| 6-states.sql | Creates `hbtn_0d_usa` and the table `states` |
| 7-cities.sql | Creates the table `cities` with a foreign key to `states` |
| 8-cities_of_california_subquery.sql | Lists the cities of California, using a subquery |
| 9-cities_by_state_join.sql | Lists all cities with the name of their state |
| 10-genre_id_by_show.sql | Lists the shows that have at least one genre |
| 11-genre_id_all_shows.sql | Lists all shows, with `NULL` for a missing genre |
| 12-no_genre.sql | Lists the shows without a genre |
| 13-count_shows_by_genre.sql | Counts the shows linked to each genre |
| 14-my_genres.sql | Lists the genres of the show Dexter |
| 15-comedy_only.sql | Lists all Comedy shows |
| 16-shows_by_genre.sql | Lists all shows and their genres, with `NULL` when missing |
