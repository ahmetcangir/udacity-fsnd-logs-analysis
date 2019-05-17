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
query_3 = """select error_rates.day, error_rates.rate AS error_rate
    from (
        select day, cast(error_count as real) / cast(total_count as real) as rate
            from (
                select http_requests_count.day,
                    http_requests_count.count as total_count,
                    http_error_counts.count as error_count
                    from
                        (
                            select date_trunc('day', log.time) as day, count(*)
                            from log
                            group by day
                        ) as http_requests_count,
                        (
                            select date_trunc('day', log.time) as day, count(*)
                            from log
                            where log.status similar to '(4|5)%' -- 400, 500 series status codes
                            group by day
                        ) as http_error_counts
                where http_requests_count.day = http_error_counts.day
          ) as daily_http_request_counts
       ) as error_rates
    where error_rates.rate > 0.01;
    """

print("# LOGS ANALYSIS \n\r")


def top_three_articles():
    print("## The most popular three articles of all time:")
    query = query_db(query_1)
    for title, num in query:
        print(" - \"{}\" -- {} views".format(title, num))
    print()


def top_authors():
    print("## The most popular article authors of all time:")
    query = query_db(query_2)
    for name, num in query:
        print(" - {} -- {} views".format(name, num))
    print()


def top_error_days():
    query = query_db(query_3)
    print("## The days on which more than 1% of requests lead to errors:")
    for day, rate in query:
        print(" - {0:%B %d, %Y} — {1:.2%} views".format(day, rate))
    print()


def main():
    top_three_articles()
    top_authors()
    top_error_days()


if __name__ == "__main__":
    main()
