#!/usr/bin/env python3

import psycopg2
import datetime

db = psycopg2.connect(dbname="news")

try:

    c = db.cursor()

    print("\n")
    print("------------------------------------")
    ''' What are the most popular three articles of all time? '''

    c.execute("""
        SELECT articles.title, count(log.path) AS article_views
        FROM log, authors, articles
        WHERE substring(log.path from 10) = articles.slug
        AND articles.author = authors.id
        GROUP BY articles.title
        ORDER BY article_views DESC
        FETCH first 3 rows only;
    """)

    print("Top 3 articles of all time:")
    for row in c.fetchall():
        print('"' + str(row[0]) + '"' + ' - ' + str(row[1]) + ' views')

    print("\n")

    ''' Who are the most popular article authors of all time? '''

    c.execute("""
        SELECT authors.name, count(log.path) AS article_views
        FROM log, authors, articles
        WHERE substring(log.path from 10) = articles.slug
        AND articles.author = authors.id
        GROUP BY authors.name
        ORDER BY article_views DESC;
    """)

    print("Most popular article authors of all time:")
    for row in c.fetchall():
        print(str(row[0]) + ' - ' + str(row[1]) + ' views')

    print("\n")

    ''' On which days did more than 1% of requests lead to errors? '''

    c.execute("""
        SELECT z.prct_err, z.calendar_day
        FROM
        (
        SELECT e.stat_error, a.attempted_views, a.calendar_day,
        (ROUND(CAST(e.stat_error AS numeric)/a.attempted_views*100, 2)) 
        AS prct_err
        FROM
        (SELECT count(status) AS stat_error,
        to_char(time, 'Mon DD, YYYY') AS calendar_day
        FROM log
        WHERE status != '200 OK'
        GROUP BY calendar_day) AS e,
        (SELECT count(path) AS attempted_views,
        to_char(time, 'Mon DD, YYYY') AS calendar_day
        FROM log
        GROUP BY calendar_day) AS a
        WHERE e.calendar_day = a.calendar_day
        ) AS z
        WHERE prct_err > 1
        ORDER BY calendar_day;
    """)

    print("Percent of requests returning with errors greater than 1%:")
    for row in c.fetchall():
        calendar_day = str(row[1])
        prct_errors = str(row[0])

        print(calendar_day + ' - ' + prct_errors + '%')

    print("------------------------------------")

except Exception as ex:
    print("ERROR: ", ex)

finally:
    db.close()
