# SQL_introduction

Introduction to SQL with MySQL: databases, tables, inserting, querying, updating and aggregating.

Run a script like this (the database name is passed as an argument when needed):

```
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

| File | Description |
|------|-------------|
| 0-list_databases.sql | Lists all databases of the MySQL server |
| 1-create_database_if_missing.sql | Creates the database `hbtn_0c_0` if it does not exist |
| 2-remove_database.sql | Deletes the database `hbtn_0c_0` if it exists |
| 3-list_tables.sql | Lists all the tables of a database |
| 4-first_table.sql | Creates the table `first_table` (`id INT`, `name VARCHAR(256)`) |
| 5-full_table.sql | Prints the full definition of `first_table` |
| 6-list_values.sql | Lists all rows of `first_table` |
| 7-insert_value.sql | Inserts the row `89`, `Best School` in `first_table` |
| 8-count_89.sql | Counts the records with `id = 89` in `first_table` |
| 9-full_creation.sql | Creates `second_table` and adds 4 rows |
| 10-top_score.sql | Lists `score` and `name` ordered by score, top first |
| 11-best_score.sql | Lists the records with a score >= 10, top first |
| 12-no_cheating.sql | Updates the score of Bob to 10 |
| 13-change_class.sql | Removes all records with a score <= 5 |
| 14-average.sql | Computes the score average (column `average`) |
| 15-groups.sql | Counts the records per score (column `number`), most first |
| 16-no_link.sql | Lists the records that have a name, by descending score |
