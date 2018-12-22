#!/usr/bin/env python 3

import psycopg2

# ===========================================================
# 1). What are the most popular three articles of all time?
# ===========================================================

articles = """

SELECT articles.title AS article_title,
       COUNT(articles.title) AS article_views
       FROM articles
       JOIN log ON articles.slug=substr(log.path, 10)
       WHERE log.status = '200 OK'
       GROUP BY articles.title
       ORDER BY COUNT(articles.title)
       DESC
       LIMIT 3;

            """

# ===========================================================
# 2). Who are the most popular authors of all time?
# ===========================================================

authors = """

SELECT authors.name AS authors_name,
       COUNT(articles.author) AS authors_views
       FROM articles
       JOIN authors ON articles.author=authors.id
       JOIN log ON articles.slug=substr(log.path, 10)
       WHERE log.status = '200 OK'
       GROUP BY authors.name
       ORDER BY authors_views
       DESC;

          """

# ===========================================================
# 3). What days did more than 1% of requests lead to errors?
# ===========================================================
errors = """

SELECT * FROM (SELECT Date(log.time),
    ROUND(100.0 * Sum(CASE log.status
    WHEN '200 OK' THEN 0
    ELSE 1
    end) / COUNT(log.status), 3) AS error_data
    FROM  log
    GROUP BY Date(log.time)
    ORDER BY error_data DESC) AS query_data
    WHERE error_data > 1;

         """


# ===========================================================
# Generate the report from SQL queries
# ===========================================================


def title_desc(title):
    print("\n\t\t" + title + "\n")

# ===========================================================
# CONNECT DATABASE with python module psycopg2
# ===========================================================


def connect_DB(queries):
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(queries)
    results = cursor.fetchall()
    conn.close()
    return results

# ==========================================================
# Create a function per each query from above
# ==========================================================

# 1). Query 1


def top_articles():
    top_articles = connect_DB(articles)
    title_desc("Top 3 most viewed articles of all time")

    for article_title, article_views in top_articles:
        print(" {} --- {} Articles".format(article_title, article_views))

# 2). Query 2


def top_authors():
    top_authors = connect_DB(authors)
    title_desc("Most popular authors of all time")

    for authors_name, authors_views in top_authors:
        print(" {} --- {} Total Views".format(authors_name, authors_views))

# 3). Query 3


def display_errors():
    display_errors = connect_DB(errors)
    title_desc("Days where more than {1%} lead to errors")

    for error_data, query_data in display_errors:
        print(" {} --- {} Percentage".format(error_data, query_data))

# ===========================================================
# Launch Python Application
# ===========================================================


if __name__ == '__main__':
    top_articles()
    top_authors()
    display_errors()
