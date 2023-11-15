# 0x0E. SQL - More queries
`SQL` `MySQL`

## General
* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a `PRIMARY KEY`
* What’s a `FOREIGN KEY`
* How to use `NOT NULL` and `UNIQUE` constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are `JOIN` and `UNION`

### Tasks:
+ Task 0. **My privileges!**
  * SQL script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on server (in localhost).
  * File: `0-privileges.sql`

+ Task 1. **Root user**
  * SQL script that creates the MySQL server user `user_0d_1`.
  ```sql
  ~/$ cat 1-create_user.sql | mysql -hlocalhost -uroot -proot
  ~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -proot
  Grants for user_0d_1@localhost
  GRANT SELECT, INSERT..., DROP ROLE ON *.* TO `user_0d_1`@`localhost`
  GRANT APPLICATION_PASSWORD_ADMIN,...,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`
  ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
  ~/$ 
  ```
  * File: `1-create_user.sql`

+ Task 2. **Read user**
  * SQL script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
    * `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
    * The `user_0d_2` password should be set to `user_0d_2_pwd`
    * If the database `hbtn_0d_2` already exists, your script should not fail
    * If the user `user_0d_2` already exists, your script should not fail
  * File: `2-create_read_user.sql`

+ Task 3. **Always a name**
  * SQL script that creates the table `force_name` on your MySQL server.
    * `force_name` description:
      * `id` INT
      * `name` VARCHAR(256) can’t be null
    * The database name will be passed as an argument of the mysql command.
    * If the table `force_name` already exists, your script should not fail.
  * File: `3-force_name.sql`

+ Task 4. **ID can't be null**
  * SQL script that creates the table `id_not_null` on your MySQL server.
    * `id_not_null` description:
      * `id` INT with the default value `1`
      * `name` VARCHAR(256)
  * File: `4-never_empty.sql`

+ Task 5. **Unique ID**
  * SQL script that creates the table `unique_id` on your MySQL server.
    * `unique_id` description:
      * `id` INT with the default value `1` and must be unique
      * `name` VARCHAR(256)
  * File: `5-unique_id.sql`

