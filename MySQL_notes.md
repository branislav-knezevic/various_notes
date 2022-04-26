# MySQL commands

`SHOW databases;` shows all databases

USE database <db_name>;
SHOW tables;
DESCRIBE <db_name> <table_name>
EXPLAIN <table_name> -- same as above
SHOW FIELDS FROM <db_name>.<table_name>
DESCRIBE <table_name> <column_name>
SELECT * FROM <table_name> where... ;
limit <number> -- add to end to get only <number> results
select count(*) from <table_name>; -- row count
mysqldump -h <db_host> -u <user> -p<password> <db_name> <table_name> > <dump_path_name>
SELECT DISTINCT <column_name> from <table_name> -- returns all result types from of <column_name>
ALTER TABLE <tablename> MODIFY <columnname> INTEGER;
UPDATE <table_name> set <column_name>=<desired_value> where <condition>;
SELECT table_name, table_rows FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = '<db_name>'; -- Get row count in all tables
SHOW PROCESSLIST; -- shows all connections to the DB
CALL mysql.rds_kill(<id>); -- kills specific connectiong to RDS DB, id is from SHOW PROCESSLIST;
user which can grant permissions to other users must have " WITH GRANT OPTION" at the end of listed permissions
select concat('CALL mysql.rds_kill( ',id,');') from information_schema.processlist where db='tis_ios_live_test'; -- kill multiple processes
-- after this run each line from the output, best to edit in notepad and then run

## User management

`SELECT User FROM mysql.user;` shows DB users
`SHOW GRANTS FOR <username>;`  shows permissions
`GRANT ALL PRIVILEGES ON <db_name>.<table_name> TO '<user>'@'%';` grant permissions on a user to a database or table
`CREATE USER '<username>'@'%' IDENTIFIED BY '<PASSWORD>';` create user with privileges
`ALTER USER '<username>'@'%' IDENTIFIED BY '<PASSWORD>';` change password for user


select status from journey_activations where journey_id like "3c68524c%" -- example for milenko

UUID not as BINARY(255) -- problems in PPS with columns being to long, should be BINARY(16)
Pay attention if there is drop+create request instead of modify. Dropping deletes the data


mysql -u datadog -p -e "SELECT * FROM performance_schema.threads" && echo -e "\033[0;32mMySQL SELECT grant - OK\033[0m" || echo -e "\033[0;31mMissing SELECT grant\033[0m"

describe all tables from desired database

```mysql
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, COLUMN_TYPE, COLUMN_COMMENT, ORDINAL_POSITION FROM information_schema.columns WHERE table_schema = '<db_name>' ORDER BY TABLE_NAME, ORDINAL_POSITION;

```
