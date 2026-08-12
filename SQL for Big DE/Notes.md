# Associated Youtube video
[SQL For Big Data Engineering [Full Course 2025]](https://youtube.com/watch?v=b0TCqhP2P7I)

# Intro
Every big data project these days makes use of distributed computing. SQL is used frequently, even with distributed computing. A widely used tool for this is Spark/Spark SQL.

# Overall summary of the SQL for Big DE course:
1. What is Spark SQL? Why is Spark SQL needed? What are some real use cases for Spark SQL?
2. Basics of Spark SQL
3. How can we register tables/external tables in Spark SQL?
4. Hands-on SQL - building complex queries, CTEs, subqueries, aggregation functions, window functions, etc.
5. Going from creating functions & stored procedures in SQL to creating them in Spark SQL
6. Row-level security & data masking in Spark SQL
7. Delta Live Tables in Spark SQL
8. Using delta lake (an open table format) with SQL/Spark SQL

# Pre-requisites (required)
1. Usage of cloud platforms, cloud knowledge/experience (for example, Azure, which works hand-in-hand with Databricks)
2. Companies frequently use cloud platforms & other related tools to easily deploy or scale nodes, VMs, etc. when they need computing power

# What is Spark SQL?
It's a module within Apache Spark that allows you to run SQL queries on big data in the same way that you would in a SQL database. It runs on top of Spark's distributed computing engine (allowing for speed & scalability). Apache Spark is a distributed computing engine that processes data in a distributed manner (for example, using 10 machines as 1 machine). In Spark SQL, you are running SQL queries normally (externally), but internally, Spark SQL is operating on data frames.

# Why do we need Spark SQL?
1. SQL is easy to learn (even if you're not a programmer)
2. It's great for ad-hoc analysis (just like querying a database)
3. It's widely used by data analysts, data scientists, & data engineers (all in 1 environment - promotes integration between these different data professionals)
4. SQL features & capabilities have been added/supported in basically all of the modern data tools (Databricks, Snowflake, Deltalake, dbt, etc.)