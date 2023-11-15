# 0x0D. SQL - Introduction

# General
* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does `DDL` and `DML` stand for
* How to `CREATE` or `ALTER` a table
* How to `SELECT` data from a table
* How to `INSERT`, `UPDATE` or `DELETE` data
* What are `subqueries`
* How to use MySQL functions

## Tasks:
+ Task 0. **List databases:**
  * SQL script that lists all databases of your MySQL server.
    ```sql
    SHOW DATABASES
    ```
  * File: `0-list_databases.sql`

+ Task 1. **Create a database**
  * SQL script that creates the database `hbtn_0c_0` in your MySQL server.
    ```sql
    CREATE DATABASE IF NOT EXISTS hbtn_0c_0
    ```
  * File: `1-create_database_if_missing.sql`

+ Task 2. **Delete a database**
  * SQL script that deletes the database `hbtn_0c_0` in your MySQL server.
  * File: `2-remove_database.sql`

+ Task 3. **List tables**
  * SQL script that lists all the tables of a database in your MySQL server.
    ```sql
    cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
    ```
  * File: `3-list_tables.sql`

