# Database code for the DB News.

import psycopg2

DBNAME = "news"
USER = "vagrant"
PASSWORD = "secret"


def get_most_popular_articles():
    """Return the three last articles mos popular in the 'database'."""
    db = psycopg2.connect(database=DBNAME, user=USER, password=PASSWORD)
    c = db.cursor()
    c.execute("SELECT title, COUNT(path) AS views " +
              "FROM log INNER JOIN articles " +
              "ON slug = split_part(path, '/', 3) " +
              "WHERE method='GET' AND status='200 OK' "
              "GROUP BY title ORDER BY views DESC LIMIT 3")
    articles = c.fetchall()
    db.close()
    return articles


def get_most_popular_authors():
    """Return the authors most popular in the 'database'."""
    db = psycopg2.connect(database=DBNAME, user=USER, password=PASSWORD)
    c = db.cursor()
    c.execute("SELECT aut.name, COUNT(l.path) AS views " +
              "FROM log l INNER JOIN articles art " +
              "ON art.slug=split_part(l.path, '/', 3) " +
              "INNER JOIN authors aut ON aut.id=art.author " +
              "WHERE l.method='GET' AND l.status='200 OK' " +
              "GROUP BY aut.name ORDER BY views DESC")
    authors = c.fetchall()
    db.close()
    return authors


def get_day_most_errors():
    """Return date and percents erros in the 'database'."""
    db = psycopg2.connect(database=DBNAME, user=USER, password=PASSWORD)
    c = db.cursor()

    c.execute("SELECT TO_CHAR(DATE(l.time), 'DD/MM/YYYY') AS DATE, " +
              "TO_CHAR(CAST(((COUNT(l.status)::DECIMAL * 100) / (SELECT " +
              "COUNT(l2.status) AS qtd FROM log l2 WHERE l2.status = " +
              "'200 OK' GROUP BY DATE(l2.time) ORDER BY qtd DESC " +
              "LIMIT 1)::DECIMAL) AS DECIMAL), '999D99') AS PERCENTS " +
              "FROM log l WHERE l.status <> '200 OK' GROUP BY DATE(l.time) " +
              "ORDER BY percents LIMIT 1;")

    inf = c.fetchall()
    db.close()
    return inf
