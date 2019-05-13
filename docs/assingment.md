# Your assignment: Build it!

Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the `psycopg2` module to connect to the database.

## So what are we reporting, anyway?
Here are the questions the reporting tool should answer. The example answers given aren't the right ones, though!

1. **What are the most popular three articles of all time?** Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top. **Example:**
- "Candidate is jerk, alleges rival" -- 338647 views
- "Bears love berries, alleges bear" -- 253801 views
- "Bad things gone, say good people" -- 170098 views

2. **Who are the most popular article authors of all time?** That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top. **Example:**
- Ursula La Multa -- 507594 views
- Rudolf von Treppenwitz -- 423457 views
- Anonymous Contributor -- 170098 views
- Markoff Chaney -- 84557 views

3. **On which days did more than 1% of requests lead to errors?** The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.) **Example:**

- July 17, 2016 — 2.26% views

# Good coding practices
## SQL style
Each one of these questions can be answered with a single database query. Your code should get the database to do the heavy lifting by using joins, aggregations, and the `where` clause to extract just the information you need, doing minimal "post-processing" in the Python code itself.

In building this tool, you may find it useful to add views to the database. You are allowed and encouraged to do this! However, if you create views, make sure to put the create view commands you used into your lab's README file so your reviewer will know how to recreate them.

## Python code quality
Your code should be written with good Python style. The PEP8 style guide is an excellent standard to follow. You can do a quick check using the [pep8](https://www.python.org/dev/peps/pep-0008/) command-line tool.