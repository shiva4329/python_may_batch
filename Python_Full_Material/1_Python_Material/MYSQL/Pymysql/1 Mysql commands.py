mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mydb1              |
| mysql              |
| performance_schema |
| sakila             |
| sys                |
| world              |
+--------------------+
7 rows in set (1.41 sec)

mysql> create database mydb2;
Query OK, 1 row affected (0.27 sec)

mysql> use mydb2;
Database changed


I) Creating a table:
mysql> create table emp(eid int,ename varchar(10),sal int,sex varchar(1),dno int,city varchar(10));
Query OK, 0 rows affected (1.35 sec)
---------------------------------------------------------------------------------------------
II)inserting data into the table
mysql> insert into emp values(101,'Miller',10000,'m',11,'hyd'),
    -> (102,'Blake',20000,'m',12,'pune'),
    -> (103,'Sony',30000,'f',11,'hyd'),
    -> (104,'Sita',40000,'f',12,'pune'),
    -> (105,'John',50000,'m',13,'hyd');
----------------------------------------------------------------------------------------------
III)a)Retrieving data(all columns) from the table
mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  102 | Blake  | 20000 | m    |   12 | pune |
|  103 | Sony   | 30000 | f    |   11 | hyd  |
|  104 | Sita   | 40000 | f    |   12 | pune |
|  105 | John   | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+

b)Retrieving selected columns(ename,sal)
mysql> select ename,sal from emp;
+--------+-------+
| ename  | sal   |
+--------+-------+
| Miller | 10000 |
| Blake  | 20000 |
| Sony   | 30000 |
| Sita   | 40000 |
| John   | 50000 |
+--------+-------+
5 rows in set (0.00 sec)

-----------------------------------------------------------------------------------------------
IV)updating a record:
mysql> update emp set sal=sal+5000 where eid=102;
Query OK, 1 row affected (0.12 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  102 | Blake  | 25000 | m    |   12 | pune |
|  103 | Sony   | 30000 | f    |   11 | hyd  |
|  104 | Sita   | 40000 | f    |   12 | pune |
|  105 | John   | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+
-----------------------------------------------------------------------------------------------
V)Filtering data:  using where class
a)I want only those  emps who belongs to the city "hyd"

mysql> select * from emp where city="hyd";
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  103 | Sony   | 30000 | f    |   11 | hyd  |
|  105 | John   | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+
3 rows in set (0.00 sec)

b)I want those emps whose sal>30000 
 mysql> select * from emp where sal>30000;
+------+-------+-------+------+------+------+
| eid  | ename | sal   | sex  | dno  | city |
+------+-------+-------+------+------+------+
|  104 | Sita  | 40000 | f    |   12 | pune |
|  105 | John  | 50000 | m    |   13 | hyd  |
+------+-------+-------+------+------+------+
2 rows in set (0.00 sec)

c)I want those emps who belongs to city "hyd" and dno==11

mysql> select * from emp where city="hyd" and dno=11;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  103 | Sony   | 30000 | f    |   11 | hyd  |
+------+--------+-------+------+------+------+
2 rows in set (0.00 sec)

-----------------------------------------------------------------------------------------------
6)Deleting a record:
mysql> delete from emp where ename="Blake";
Query OK, 1 row affected (0.10 sec)

mysql> select * from emp;
+------+--------+-------+------+------+------+
| eid  | ename  | sal   | sex  | dno  | city |
+------+--------+-------+------+------+------+
|  101 | Miller | 10000 | m    |   11 | hyd  |
|  103 | Sony   | 30000 | f    |   11 | hyd  |
|  104 | Sita   | 40000 | f    |   12 | pune |
|  105 | John   | 50000 | m    |   13 | hyd  |
+------+--------+-------+------+------+------+







