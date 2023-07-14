# SQL Cheat sheet

### information extraction from [sqlbolt.com](http://sqlbolt.com/)

## SELECT queries
```
SELECT column, another_column, … 
FROM mytable;
```


## Queries with constraints
```
SELECT column, another_column, … 
FROM mytable 
WHERE condition AND/OR another_condition AND/OR … 
;
```
| Operator | Condition | SQL Example |
| --- | --- | --- |
| =, !=, < <=, >, >= | Standard numerical operators | col_name != 4 |
| BETWEEN … AND … | Number is within range of two values (inclusive) | col_name BETWEEN 1.5 AND 10.5 |
| NOT BETWEEN … AND … | Number is not within range of two values (inclusive) | col_name NOT BETWEEN 1 AND 10 |
| IN (…) | Number exists in a list | col_name IN (2, 4, 6) |
| NOT IN (…) | Number does not exist in a list | col_name NOT IN (1, 3, 5) |
| = | Case sensitive exact string comparison (notice the single equals) | col_name = "abc" |
| != or <> | Case sensitive exact string inequality comparison | col_name != "abcd" |
| LIKE | Case insensitive exact string comparison | col_name LIKE "ABC" |
| NOT LIKE | Case insensitive exact string inequality comparison | col_name NOT LIKE "ABCD" |
| % | Used anywhere in a string to match a sequence of zero or more characters (only with LIKE or NOT LIKE) | col_name LIKE "%AT%"(matches "AT", "ATTIC", "CAT" or even "BATS") |
| _ | Used anywhere in a string to match a single character (only with LIKE or NOT LIKE) | col_name LIKE "AN_"(matches "AND", but not "AN") |
| IN (…) | String exists in a list | col_name IN ("A", "B", "C") |
| NOT IN (…) | String does not exist in a list | col_name NOT IN ("D", "E", "F") |



## Filtering and sorting Query results
```
discard rows that have a duplicate column:
SELECT DISTINCT column, another_column, …
FROM mytable
WHERE condition(s);
```
```
ordering results:
SELECT column, another_column, …
FROM mytable
WHERE conditions(s)
ORDER BY column ASC/DESC;
```
```
limiting results to a subset:
SELECT column, another_column, …
FROM mytable
WHERE conditions(s)
ORDER BY column ASC/DESC
LIMIT num_limit OFFSET num_offset;
```


## Multi-table queries with JOINs
```
SELECT column, another_table_column, …
FROM mytable
INNER JOIN another_table
    ON mytable.id = another_table.id
WHERE condition(s)
ORDER BY colymn, … ASC/DESC
LIMIT num_limit OFFSET num_offset; 
```


## OUTER JOINs
```
SELECT column, another_column, …
FROM mytable
INNER/LEFT/RIGHT/FULL JOIN another_table
    ON mytable.id = another_table.matching_id
WHERE condition(s)
ORDER BY column, … ASC/DESC
LIMIT num_limit OFFSET num_offset;
```


## NULLS
```
SELECT column, another_column, …
FROM mytable
WHERE column IS/IS NOT NULL
AND/OR another_condition
AND/OR …;
```


## Queries with expressions
```
SELECT col_expression AS expr_description, …
FROM mytable;
```
```
SELECT column AS better_column_name, …
FROM a_long_widgets_table_name AS mywidgets
INNER JOIN widget_sales
   ON mywidgets.id = widget_sales.widget_id;
```

## Queries with aggregates
```
SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
FROM mytable
WHERE constraint_expression;
```

| Function | Description |
| --- | --- |
| COUNT(*), COUNT(column) | A common function used to counts the number of rows in the group if no column name is specified. Otherwise, count the number of rows in the group with non-NULL values in the specified column. |
| MIN(column) | Finds the smallest numerical value in the specified column for all rows in the group. |
| MAX(column) | Finds the largest numerical value in the specified column for all rows in the group. |
| AVG(column) | Finds the average numerical value in the specified column for all rows in the group. |
| SUM(column) | Finds the sum of all numerical values in the specified column for the rows in the group. |

```
Grouped aggregate functions 
SELECT AGG_FUNC (column_or_expression) AS aggregate_description, … 
FROM mytable 
WHERE constraint_expression 
GROUP BY column 
HAVING group_condition;
```
## Order of execution of a Query
```
1.FROM AND JOINS 
2.WHERE 
3.GROUP BY 
4.HAVING 
5.SELECT 
6.DISTINCT 
7.ORDER BY 
8.LIMIT/OFFSET 
```


## Inserting rows
```
INSERT INTO mytable 
**(column, another_column, …)** 
VALUES (value_or_expr, another_value_or_expr, …), 
      (value_or_expr_2, another_value_or_expr_2, …), 
      …;
```


## Updating rows
```
UPDATE mytable
SET column = value_or_expr,
   other_column = another_value_or_expr,
   …
WHERE condition;
```
## Deleting rows
```
DELETE FROM mytable 
WHERE condition;
```
## Creating tables
```
CREATE TABLE IF NOT EXISTS mytable (
    column DataType TableConstraint DEFAULT default_value,
    another_column DataType TableConstrain DEFAULT default_value,
    … \
);
```

| Data type | Description |
| --- | --- |
| INTEGER, BOOLEAN | The integer datatypes can store whole integer values like the count of a number or an age. In some implementations, the boolean value is just represented as an integer value of just 0 or 1. |
| FLOAT, DOUBLE, REAL | The floating point datatypes can store more precise numerical data like measurements or fractional values. Different types can be used depending on the floating point precision required for that value. |
| CHARACTER(num_chars), VARCHAR(num_chars), TEXT | The text based datatypes can store strings and text in all sorts of locales. The distinction between the various types generally amount to underlaying efficiency of the database when working with these columns. Both the CHARACTER and VARCHAR (variable character) types are specified with the max number of characters that they can store (longer values may be truncated), so can be more efficient to store and query with big tables. |
| DATE, DATETIME | SQL can also store date and time stamps to keep track of time series and event data. They can be tricky to work with especially when manipulating data across timezones. |
| BLOB | Finally, SQL can store binary data in blobs right in the database. These values are often opaque to the database, so you usually have to store them with the right metadata to requery them. |

| Constraint | Description |
| --- | --- |
| PRIMARY KEY | This means that the values in this column are unique, and each value can be used to identify a single row in this table. |
| AUTOINCREMENT | For integer values, this means that the value is automatically filled in and incremented with each row insertion. Not supported in all databases. |
| UNIQUE | This means that the values in this column have to be unique, so you can't insert another row with the same value in this column as another row in the table. Differs from the `PRIMARY KEY` in that it doesn't have to be a key for a row in the table. |
| NOT NULL | This means that the inserted value can not be `NULL`. |
| CHECK (expression) | This allows you to run a more complex expression to test whether the values inserted are valid. For example, you can check that values are positive, or greater than a specific size, or start with a certain prefix, etc. |
| FOREIGN KEY | This is a consistency check which ensures that each value in this column corresponds to another value in a column in another table.For example, if there are two tables, one listing all Employees by ID, and another listing their payroll information, the `FOREIGN KEY` can ensure that every row in the payroll table corresponds to a valid employee in the master Employee list. |



## Altering tables
```
Adding columns
ALTER TABLE mytable
ADD column DataType OptionalTableConstraint
   DEFAULT default_value;
```
```
Removing columns
ALTER TABLE mytable
DROP column_to_be_deleted;
```
```
Renaming the table
ALTER TABLE mytable
RENAME TO new_table_name;
```
## Dropping tables
```
DROP TABLE IF EXISTS mytable;
```