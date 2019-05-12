# Logs Analysis
A Udacity FSND project.

## Introduction
This is the solution for the Logs Analysis project in Udacity Full Stack Nanodegree course. In this, we have to execute complex queries on a large database to extract intersting stats.

The database in question is a newspaper company database where we have 3 tables; articles, authors and log.

 - articles - Contains articles posted in the newspaper so far.
```
                                  Table "public.articles"
 Column |           Type           |                       Modifiers
--------+--------------------------+-------------------------------------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     |
 body   | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('articles_id_seq'::regclass)
```

 - authors - Contains list of authors who have published their articles.
```
                         Table "public.authors"
 Column |  Type   |                      Modifiers
--------+---------+------------------------------------------------------
 name   | text    | not null
 bio    | text    |
 id     | integer | not null default nextval('authors_id_seq'::regclass)
```

 - log - Stores log of every request sent to the newspaper server.
 ```
                                   Table "public.log"
 Column |           Type           |                    Modifiers
--------+--------------------------+--------------------------------------------------
 path   | text                     |
 ip     | inet                     |
 method | text                     |
 status | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('log_id_seq'::regclass)
```

This project implements a single query solution for each of the question in hand. 
See [main.py](https://github.com/cangir-education/udacity-fsnd-logs-analysis/blob/master/main.py) for more details.

## How to use this code?
- Please note that you need the **[newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)** file in order to run this code.

- Then run the following command to execute it in news database. You might have to create the database before-hand.

```
psql -d news -f newsdata.sql
```

- After importing the data into **news** database, run the following command in order to execute program.

```
python2 main.py
```