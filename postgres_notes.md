# PostreSQL database notes

## Commands

### Connecting to postgres server

`psql -h <host> -p <port> -U <user> -d <database>` connect to the server

### Once connected to the server

#### Databses

`\l` list databases
`\c <db_name>` connect to desired db
`\dn` list schemas
`CREATE DATABASE <db_name>;`
`DROP DATABASE <db_name>;`

#### Tables

`\dt` list tables in current db
`\dt+` more info about tables in current db
`\d+ <table_name>` more info about specific table
`DROP TABLE <table_name>` delete specific table

#### Users

PostgreSQL uses the roles concept to manage database access permissions. A role can be a user or a group,
depending on how you setup the role. A role that has login right is called user. A role may be a member of other
roles, which are known as groups.
`\du` list users
`CREATE ROLE <role_name>` create role
`CREATE ROLE <username> NOINHERIT LOGIN PASSWORD '<password>';` create role with credentials. Password must be in single
quotes
`SET ROLE <role_name>` change role for the current session. User will then have privilages only set for that role
`RESET ROLE` restores the original role
`GRANT <role_name> TO <role_name>` allow role 1 to set its role as role 2
`REVOKE <role_name> TO <role_name>` remove role 1 from role 2

## Various notes

If postgres i used via HELM and peristent volume is used, credentials will be remembered from the first install until
the persistant volume claim is deleted
