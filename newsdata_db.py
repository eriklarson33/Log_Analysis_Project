# "Database code" for the DB news.

import psycopg2
import datetime

db = psycopg2.connect(dbname="news")

try:

    c = db.cursor()

    print("\n")
    print("------------------------------------")
    ''' What are the most popular three articles of all time? '''

    c.execute("SELECT articles.title, count(log.path) as article_views FROM log, authors, articles WHERE substring(log.path from 10) = articles.slug AND articles.author = authors.id GROUP BY articles.title ORDER BY article_views DESC FETCH first 3 rows only;")

    print("Top 3 articles of all time:")
    for row in c.fetchall():
        print('"' + str(row[0]) + '"' + ' - ' + str(row[1]) + ' views')


    print("\n")

    ''' Who are the most popular article authors of all time? '''

    c.execute("SELECT authors.name, count(log.path) as article_views FROM log, authors, articles WHERE substring(log.path from 10) = articles.slug AND articles.author = authors.id GROUP BY authors.name ORDER BY article_views DESC;")

    print("Most popular article authors of all time:")
    for row in c.fetchall():
        print(str(row[0]) + ' - ' + str(row[1]) + ' views')
  

    print("\n")

    ''' On which days did more than 1% of requests lead to errors? '''

    c.execute("SELECT count(path) as attempted_views, (SELECT count(status) FROM log WHERE status LIKE '4%' OR status LIKE '5%') as stat_error,  to_char(time, 'Month DD, YYYY') as calendar_day FROM log GROUP BY calendar_day; ")
  

    print("Percent of requests returning with errors:")
    for row in c.fetchall():
        total_views = str(row[0])
        day_errors = str(row[1])
        calendar_day = str(row[2])
    
        print(calendar_day + ' - ' + str(round(float(day_errors)/float(total_views) * 100, 2)) + '%')
    
    print("------------------------------------")

except Exception as ex:
    print("ERROR: ", ex)

finally:
    db.close()
