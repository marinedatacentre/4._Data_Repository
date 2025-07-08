# **PostgreSQL LEAD Function**

**Summary**: in this tutorial, you will learn how to use the PostgreSQL LEAD() function to access a row that follows the current row, at a specific physical offset.

## Introduction to PostgreSQL LEAD() function

PostgreSQL LEAD() function provide access to a row that follows the current row at a specified physical offset.

It means that from the current row, the LEAD() function can access data of the next row, the row after the next row, and so on.

The LEAD() function is very useful for comparing the value of the current row with the value of the row that following the current row.

The following illustrates the syntax of LEAD() function:

LEAD(expression \[,offset \[,default_value\]\])

OVER (

\[PARTITION BY partition_expression, ... \]

ORDER BY sort_expression \[ASC \| DESC\], ...

)

Code language: SQL (Structured Query Language) (sql)

In this syntax:

### expression

The expression is evaluated against the following row based on a specified offset from the current row. The expression can be a column, expression, [subquery](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-subquery/) that must evaluate to a single value. And it cannot be a [window function](https://www.postgresqltutorial.com/postgresql-window-function/).

### offset

The offset is a positive integer that specifies the number of rows forwarding from the current row from which to access data. The offset can be an expression, subquery, or column.

The offset defaults to 1 if you don’t specify it.

### default_value

The default_value is the return value if the offset goes beyond the scope of the partition. The default_value defaults to NULL if you omit it.

### PARTITION BY clause

The PARTITION BY clause divides rows into partitions to which the LEAD() function is applied.

By default, the whole result set is a single partition if you omit the PARTITION BY clause.

### ORDER BY clause

The ORDER BY clause specifies the sort order of the rows in each partition to which the LEAD() function is applied.

## PostgreSQL LEAD() function examples

Let’s set up a new table for the demonstration.

First, [create a new table](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-create-table/) named sales:

CREATE TABLE sales(

year SMALLINT CHECK(year \> 0),

group_id INT NOT NULL,

amount DECIMAL(10,2) NOT NULL,

PRIMARY KEY(year,group_id)

);

Code language: SQL (Structured Query Language) (sql)

Second, [insert](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-insert/) some rows into the sales table:

INSERT INTO

sales(year, group_id, amount)

VALUES

(2018,1,1474),

(2018,2,1787),

(2018,3,1760),

(2019,1,1915),

(2019,2,1911),

(2019,3,1118),

(2020,1,1646),

(2020,2,1975),

(2020,3,1516);

Code language: SQL (Structured Query Language) (sql)

Third, query data from the sales table:

SELECT \* FROM sales;

Code language: SQL (Structured Query Language) (sql)

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image1.png" style="width:3in;height:2.73958in" />

### 1) Using PostgreSQL LEAD() function over a result set examples

The following query returns the total sales amount by year:

SELECT

year,

SUM(amount)

FROM sales

GROUP BY year

ORDER BY year;

Code language: SQL (Structured Query Language) (sql)

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image2.png" style="width:1.83333in;height:1.16667in" />

This example uses the LEAD() function to return the sales amount of the current year and the next year:

WITH cte AS (

SELECT

year,

SUM(amount) amount

FROM sales

GROUP BY year

ORDER BY year

)

SELECT

year,

amount,

LEAD(amount,1) OVER (

ORDER BY year

) next_year_sales

FROM

cte;

Code language: SQL (Structured Query Language) (sql)

Here is the output:

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image3.png" style="width:3.0625in;height:1.17708in" />

In this example:

- First, the [CTE](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-cte/) returns the sales summarized by year.

- Then, the outer query uses the LEAD() function to return the sales of the following year for each row.

# **PostgreSQL ROW_NUMBER Function**

**Summary**: in this tutorial, you will learn how to use the PostgreSQL ROW_NUMBER() function to assign a unique integer value to each row in a result set.

## Introduction to the PostgreSQL ROW_NUMBER() function

The ROW_NUMBER() function is a [window function](https://www.postgresqltutorial.com/postgresql-window-function/) that assigns a sequential integer to each row in a result set. The following illustrates the syntax of the ROW_NUMBER() function:

ROW_NUMBER() OVER(

\[PARTITION BY column_1, column_2,…\]

\[ORDER BY column_3,column_4,…\]

)

Code language: SQL (Structured Query Language) (sql)

The set of rows on which the ROW_NUMBER() function operates is called a window.

The PARTITION BY clause divides the window into smaller sets or partitions. If you specify the PARTITION BY clause, the row number for each partition starts with one and increments by one.

Because the PARTITION BY clause is optional to the ROW_NUMBER() function, therefore you can omit it, and ROW_NUMBER() function will treat the whole window as a partition.

The ORDER BY clause inside the OVER clause determines the order in which the numbers are assigned.

## PostgreSQL ROW_NUMBER() function examples

We will use the products table created in the [PostgreSQL window function tutorial](https://www.postgresqltutorial.com/postgresql-window-function/) to demonstrate the functionality of the ROW_NUMBER() function.

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image4.png" style="width:5.625in;height:1.80208in" />

The following is the data in the products table:

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image5.png" style="width:3.65625in;height:2.21875in" />

See the following query.

SELECT

product_id,

product_name,

group_id,

ROW_NUMBER () OVER (ORDER BY product_id)

FROM

products;

Code language: SQL (Structured Query Language) (sql)

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image6.png" style="width:4.0625in;height:2.27083in" />

Because we did not use the PARTITION BY clause, the ROW_NUMBER() function considers the whole result set as a partition.

The ORDER BY clause sorts the result set by product_id, therefore, the ROW_NUMBER() function assigns integer values to the rows based on the  product_id order.

In the following query, we change the column in the ORDER BY clause to product_name, the ROW_NUMBER() function assigns the integer values to each row based on the product name order.

SELECT

product_id,

product_name,

group_id,

ROW_NUMBER () OVER (

ORDER BY product_name

)

FROM

products;

Code language: SQL (Structured Query Language) (sql)

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image7.png" style="width:4.04167in;height:2.25in" />

In the following query, we use the PARTITION BY clause to divide the window into subsets based on the values in the  group_id column. In this case, the ROW_NUMBER() function assigns one to the starting row of each partition and increases by one for the next row within the same partition.

The ORDER BY clause sorts the rows in each partition by the values in the product_name column.

SELECT

product_id,

product_name,

group_id,

ROW_NUMBER () OVER (

PARTITION BY group_id

ORDER BY

product_name

)

FROM

products;

Code language: SQL (Structured Query Language) (sql)

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image8.png" style="width:4.03125in;height:2.26042in" />

## PostgreSQL ROW_NUMBER() function and DISTINCT operator

The following query uses the ROW_NUMBER() function to assign integers to the [distinct](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-select-distinct/) prices from the products table.

SELECT DISTINCT

price,

ROW_NUMBER () OVER (ORDER BY price)

FROM

products

ORDER BY

price;

Code language: SQL (Structured Query Language) (sql)

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image9.png" style="width:1.63542in;height:2.23958in" />

However, the result is not expected because it includes duplicate prices. The reason is that the ROW_NUMBER() operates on the result set before the DISTINCT is applied.

To solve this problem, we can get a list of distinct prices in a CTE, the apply the ROW_NUMBER() function in the outer query as follows:

WITH prices AS (

SELECT DISTINCT

price

FROM

products

) SELECT

price,

ROW_NUMBER () OVER (ORDER BY price)

FROM

prices;

Code language: SQL (Structured Query Language) (sql)

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image10.png" style="width:1.61458in;height:1.66667in" />

Or we can use a [subquery](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-subquery/) in the FROM clause to get a list of unique price, and then apply the ROW_NUMBER() function in the outer query.

SELECT

price,

ROW_NUMBER () OVER (ORDER BY price)

FROM

(

SELECT DISTINCT

price

FROM

products

) prices;

Code language: SQL (Structured Query Language) (sql)

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image11.png" style="width:1.64583in;height:1.64583in" />

## Using ROW_NUMBER() function for pagination

In application development, you use the pagination technique for displaying a subset of rows instead of all rows in a table.

Besides using the [LIMIT](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-limit/) clause, you can also use the ROW_NUMBER() function for the pagination.

For example, the following query selects the five rows starting at row number 6:

SELECT

\*

FROM

(

SELECT

product_id,

product_name,

price,

ROW_NUMBER () OVER (ORDER BY product_name)

FROM

products

) x

WHERE

ROW_NUMBER BETWEEN 6 AND 10;

Code language: SQL (Structured Query Language) (sql)

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image12.png" style="width:3.82292in;height:1.09375in" />

## Using ROW_NUMBER() function for getting the nth highest / lowest row

For example, to get the third most expensive products, first, we get the distinct prices from the products table and select the price whose row number is 3. Then, in the outer query, we get the products with the price that equals the 3rd highest price.

SELECT

\*

FROM

products

WHERE

price = (

SELECT

price

FROM

(

SELECT

price,

ROW_NUMBER () OVER (

ORDER BY price DESC

) nth

FROM

(

SELECT DISTINCT

(price)

FROM

products

) prices

) sorted_prices

WHERE

nth = 3

);

Code language: SQL (Structured Query Language) (sql)

<img src="370-F35 PostgreSQL LEAD() and ROW_NUMBER()_media/media/image13.png" style="width:3.64583in;height:0.35417in" />

In this tutorial, we have shown you how to use the PostgreSQL ROW_NUMBER() function to assign integer values to rows in a result set.
