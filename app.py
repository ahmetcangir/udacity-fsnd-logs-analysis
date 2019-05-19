#!/usr/bin/env python3
#
# Udacity Full Stack NanoDegree Log Analysis Project

import psycopg2
from pathlib import Path


def query_db(sql_request):
    """
    query_db returns the results of an SQL query.

    query_db takes an SQL query as a parameter,
    executes the query and returns the results as a list of tuples.
    args:
    sql_request - an SQL query statement to be executed.

    returns:
    A list of tuples containing the results of the query.
    """
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(sql_request)
    results = cursor.fetchall()
    conn.close()
    return results


def top_three_articles():
    """
    returns:
    The most popular three articles of all time.
    """
    print("## The most popular three articles of all time:")
    sql = Path('sql/top_three_articles.sql').read_text()
    query = query_db(sql)
    for title, num in query:
        print(" - \"{}\" -- {} views".format(title, num))
    print()


def top_authors():
    """
    returns:
    The most popular article authors of all time.
    """
    print("## The most popular article authors of all time:")
    sql = Path('sql/top_authors.sql').read_text()
    query = query_db(sql)
    for name, num in query:
        print(" - {} -- {} views".format(name, num))
    print()


def top_error_days():
    """
    returns:
    The days on which more than 1% of requests lead to errors.
    """
    print("## The days on which more than 1% of requests lead to errors:")
    sql = Path('sql/top_error_days.sql').read_text()
    query = query_db(sql)
    for day, rate in query:
        print(" - {0:%B %d, %Y} — {1:.2%} views".format(day, rate))
    print()


def main():
    """
    executes top_three_articles, top_authors and top_error_days functions
    """
    print("# LOGS ANALYSIS \n\r")
    top_three_articles()
    top_authors()
    top_error_days()


if __name__ == "__main__":
    main()
