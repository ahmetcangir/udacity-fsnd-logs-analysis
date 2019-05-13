## Introduction
This is the solution for [the Logs Analysis project](https://github.com/cangir-education/udacity-fsnd-logs-analysis/blob/master/docs/assingment.md) in [Udacity Full Stack Nanodegree course](https://eu.udacity.com/course/full-stack-web-developer-nanodegree--nd004). In this, we have to execute complex queries on a large database to extract intersting stats.

![log Analysis preview](https://github.com/cangir-education/udacity-fsnd-logs-analysis/blob/master/screenshot.png)

## Project Overview
This project uses Python3 to interact with a PostgreSQL database containing information from a newspaper site. The Python3 module [app.py](https://github.com/cangir-education/udacity-fsnd-logs-analysis/blob/master/app.py) is a reporting tool that creates a report that answers the following questions:

- What are the most popular three articles of all time?
- Who are the most popular authors of all time?
- On which days did more than 1% of requests lead to errors?

## Requirements
- [Python 3](https://www.python.org/downloads/) - The code uses ver 3.7.3
- [VirtualBox](https://www.virtualbox.org/) - An open source virtualiztion product.
- [Vagrant](https://www.vagrantup.com/) - A virtual environment builder and manager
- [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) - The data provided by Udacity


## Instructions
1. If you don't already have the latest version of python download it from the link in requirements.
2. Download and install Vagrant and VirtualBox.
3. Clone this repository.
4. Download the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) database.
5. Navigate to the `udacity-fsnd-logs-analysis` folder in your bash interface.
6. Open Git Bash and launch the virtual machine with command `vagrant up`
7. Once Vagrant installs necessary files use `vagrant ssh` to continue.
8. The command line will now start with vagrant. Here get into to the shared /vagrant folder by command `cd /vagrant`.
9. Unpack newsdata.zip into `udacity-fsnd-logs-analysis` folder.
10. Load the database type psql -d news -f newsdata.sql
11. Use command `python3 app.py` to run the python program that fetches query results.
12. Use command `python3 app.py > output.md` to export results to an output.md file. 