#!/usr/bin/env python 3

import psycopg2

#===========================================================
# 1). What are the most popular three articles of all time?
#===========================================================

# articles.title has an alias of article_title
# article_views is the alias for when we use the aggregate function COUNT(). This will generate the total number of articles per author
# WHERE clause to make certain we are counting only the succesfully reached articles
# GROUP BY clause to tell the database how we want our data displayed
# ORDER BY clause COUNT(artilces.title) DESC with a limit of only 3 records

articles = """

SELECT 
    articles.title AS article_title,
    COUNT(articles.title) AS article_views

    FROM articles

    JOIN log ON articles.slug=substr(log.path, 10)

    WHERE log.status = '200 OK'

    GROUP BY articles.title

    ORDER BY COUNT(articles.title)

    DESC

    LIMIT 3;

            """

#===========================================================
# 2). Who are the most popular authors of all time?
#===========================================================

# authors.name has an alias of authors_name
# Using aggregate function COUNT() to count total articles each author has written
# Give this an alias of authors_views
# Pull from articles table as we are 'inner' joining authors and log tables
# WHERE clause to determine which articles have beeen successfully reached
# GROUP BY to tell database how we want our data displayed
# ORDER BY in DESC order by authors_views which is an alias for a COUNT(articles.author)

authors = """

SELECT 
    authors.name AS authors_name,
    COUNT(articles.author) AS authors_views

    FROM articles

    JOIN authors ON articles.author=authors.id
    JOIN log ON articles.slug=substr(log.path, 10)

    WHERE log.status = '200 OK'

    GROUP BY authors.name

    ORDER BY authors_views

    DESC;

          """

#===========================================================
# 3). What days did more than 1% of requests lead to errors?
#===========================================================

errors = """

SELECT
    log.time AS day,
    COUNT(log.time)/(SELECT SUM(CAST(log.status AS INT)) FROM log) > 1 AS percentage_total

    FROM log

    WHERE log.status NOT LIKE '200 OK'

    GROUP BY log.time

    ORDER BY log.time

    DESC;

         """

#===========================================================
# Generate the report from SQL queries
#===========================================================

def title_desc(title):
    print("\n\t\t" + title + "\n")

#===========================================================
# CONNECT DATABASE with python module psycopg2
#===========================================================

# Pull data from the news database with all 3 SQL queries
# Connect the news database
# Create an instance of the connected database
# Execute instance || 'cursor'
# Fetch all of the results the queries are asking for with fetchall()
# Create a variable for the results named results
# Close the connection with close()
# Return the results variable

def connect_DB(queries):
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(queries)
    results = cursor.fetchall()
    conn.close()
    return results

#===========================================================
# Create a function per each query from above
#===========================================================

# 1). Query 1

def top_articles():
    top_articles = connect_DB(articles)
    title_desc("Top 3 most viewed articles of all time")

    for article_title, article_views in top_articles:
        print(" {} --- {} views".format(article_title, article_views))

# 2). Query 2

def top_authors():
    top_authors = connect_DB(authors)
    title_desc("Most popular authors of all time")

    for authors_name, authors_views in top_authors:
        print(" {} --- {} total views".format(authors_name, authors_views))

# 3). Query 3

def display_errors():
    display_errors = connect_DB(errors)
    title_desc("Days where more than {1%} lead to errors")

    # For loop through content

#===========================================================
# Launch Python Application
#===========================================================

if __name__ == '__main__':
    top_articles()
    top_authors()