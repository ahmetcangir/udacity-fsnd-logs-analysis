#!/usr/bin/env python3
#
# Udacity Full Stack NanoDegree Log Analysis Project

import psycopg2

# Define database name
DBNAME = "news"


def query_db(sql_request):
    '''Query data from the database, open and close the connection'''
    conn = psycopg2.connect(database=DBNAME)
    cursor = conn.cursor()
    cursor.execute(sql_request)
    results = cursor.fetchall()
    conn.close()
    return results


# 1. What are the most popular three articles of all time?
query_1 = """select articles.title, count(*) as num
    from log, articles
    where log.status='200 OK'
        and articles.slug = substr(log.path, 10)
    group by articles.title
    order by num desc
    limit 3;"""

# 2. Who are the most popular article authors of all time?
query_2 = """select authors.name, count(*) as num
    from articles, authors, log
    where log.status='200 OK'
    and authors.id = articles.author
    and articles.slug = substr(log.path, 10)
    group by authors.name
    order by num desc;
    """

# 3. On which days did more than 1% of requests lead to errors?
query_3 = ""


def top_three_articles():
    '''Print the top three articles of all time'''
    print("The most popular three articles of all time:")
    query = query_db(query_1)
    for title, num in query:
        print(" - \"{}\" -- {} views".format(title, num))


def top_authors():
    '''Print the most popular article authors of all time.'''
    print("The most popular article authors of all time:")
    query = query_db(query_2)
    for name, num in query:
        print(" - {} -- {} views".format(name, num))


if __name__ == '__main__':
    top_three_articles()
    top_authors()
