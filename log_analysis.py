#! /usr/bin/env python

# Database code for the DB Forum, full solution!

import psycopg2
from datetime import datetime

DBNAME = "news"


def run_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        rows = c.fetchall()
        db.close()
        return rows
    except:
        print("Ooops! Can not connect to the database")


def top_articles():
    """Returns top 3 most read articles"""

    # Build Query String
    query = """
        SELECT articles.title, COUNT(log.id) AS views
        FROM articles, log
        WHERE log.path LIKE CONCAT('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY views DESC
        LIMIT 3;
        """

    # Run Query
    results = run_query(query)

    # Print Results
    print('\nTOP 3 ARTICLES BY PAGE VIEWS:')
    count = 1
    for i in results:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" with ' + str(i[1]) + " views"
        print(number + title + views)
        count += 1


def most_popular_authors():
    """returns the most popular authors"""

    # Build Query String
    query = """
        SELECT authors.name, count(*) AS views
        FROM authors, articles, log
        WHERE articles.author = authors.id
        and log.path like concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY views DESC
        LIMIT 5;
        """

    # Run Query
    results = run_query(query)

    # Print Results
    print('\n MOST POPULAR AUTHORS BY VIEWS:')
    count = 1
    for i in results:
        print('(' + str(count) + ') ' + i[0] + ' with ' + str(i[1]) + " views")
        count += 1

    # Create the Views as instructed on the README file first


def days_with_errors():
    """returns days where errors exceeded 1%"""

    # Build Query String
    query = """
        SELECT day, percentage_error
        FROM percent
        WHERE percent.percentage_error > 1.0;
        """

    # Run Query
    results = run_query(query)

    # Print Results
    print('\nDAYS WITH MORE THAN 1% ERRORS:')
    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1], 1)) + "%" + " errors"
        print(date + " -- " + errors)

print('Calculating Results...\n')
top_articles()
most_popular_authors()
days_with_errors()
