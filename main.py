#!/usr/bin/env python3
# 
# Udacity Full Stack NanoDegree Log Analysis Project

import psycopg2

DBNAME = "news"

# Function for making queries
def make_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()

# 1. What are the most popular three articles of all time?
query_1 = ""

# 2. Who are the most popular article authors of all time?
query_2 = ""

# 3. On which days did more than 1% of requests lead to errors?
query_3 = ""