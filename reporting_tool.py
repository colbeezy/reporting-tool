#!/usr/bin/env python
"""using Python 2.7"""

import psycopg2


def top_articles():
    """
    Returns the 3 most-viewed articles of all time
    and the number of views they've received.
    """
    database = psycopg2.connect("dbname=news")
    cursor = database.cursor()
    cursor.execute(
        """SELECT *
        FROM article_views
        LIMIT 3;"""
    )
    results = cursor.fetchall()
    for i in results:
        print "%s - %d views" % (i[0], i[1])
    return results
    database.close()


def top_authors():
    """
    Returns authors sorted by # of page views
    and lists the number of page views
    """
    database = psycopg2.connect("dbname=news")
    cursor = database.cursor()
    cursor.execute(
        """SELECT *
        FROM views_by_author"""
    )
    results = cursor.fetchall()
    for i in results:
        print "%s - %d views" % (i[0], i[1])
    return results
    database.close()


def errorful_days():
    """
    Returns the dates in which the error rate exceeded 1%
    and lists those error rates
    """
    database = psycopg2.connect("dbname=news")
    cursor = database.cursor()
    cursor.execute(
        """SELECT to_char(date, 'MM/DD/YYYY'),
            round(100.0 * errors/requests, 2) AS error_rate
        FROM status_by_date
        WHERE 100.0 * errors/requests > 1
        order by error_rate desc;"""
    )
    results = cursor.fetchall()
    for i in results:
        print "%s - %s%% errors" % (i[0], i[1])
    return results
    database.close()


print "\nTop 3 articles of all time: "
top_articles()

print "\nAuthors ranked by popularity: "
top_authors()

print "\nDays with an error rate above 1%: "
errorful_days()
