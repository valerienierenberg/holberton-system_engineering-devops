# 0x14-mysql

## Learning Objectives
    - What is the main role of a database
    - What is a database replica
    - What is the purpose of a database replica
    - Why database backups need to be stored in different physical locations
    - What operation should you regularly perform to make sure that your database backup strategy actually works

## Task Descriptions

- Task 0 - get MySQL installed on both web-01 and web-02 servers.
- Task 1 - create a user and password for both MySQL databases which will allow the checker access to them.
- Task 2 - Create a database named tyrell_corp.
    - Within the tyrell_corp database create a table named nexus6 and add at least one entry to it.
    - Make sure that holberton_user has SELECT permissions on your table so that we can check that the table exists and is not empty.
- Task 3 - On your primary MySQL server (web-01), create a new user for the replica server.
    - The name of the new user should be replica_user, with the host name set to %, and can have whatever password you’d like.
    - replica_user must have the appropriate permissions to replicate your primary MySQL server.
    - holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.
- 4-mysql_configuration_primary - MySQL primary configuration as answer file(my.cnf or mysqld.cnf)
- 4-mysql_configuration_replica - MySQL replica configuration as an answer file
- 5-mysql_backup - Bash script that generates a MySQL dump and creates a compressed archive out of it.
    - Requirements:
        - The MySQL dump must contain all your MySQL databases
        - The MySQL dump must be named backup.sql
        - The MySQL dump file has to be compressed to a tar.gz archive
        - This archive must have the following name format: day-month-year.tar.gz
        - The user to connect to the MySQL database must be root
        - The Bash script accepts one argument that is the password used to connect to the MySQL database
