# Database code for the DB News.

import psycopg2

DBNAME = "news"
USER = "vagrant"
PASSWORD = "secret"


def get_most_popular_articles():
    """Return the three last articles mos popular in the 'database'."""
    db = psycopg2.connect(database=DBNAME, user=USER, password=PASSWORD)
    c = db.cursor()
    query = """\
    SELECT title,
       COUNT(PATH) AS views
    FROM log
    INNER JOIN articles ON slug = split_part(PATH, '/', 3)
    WHERE METHOD='GET'
    AND status='200 OK'
    GROUP BY title
    ORDER BY views DESC
    LIMIT 3
    """
    c.execute(query)
    articles = c.fetchall()
    db.close()
    return articles


def get_most_popular_authors():
    """Return the authors most popular in the 'database'."""
    db = psycopg2.connect(database=DBNAME, user=USER, password=PASSWORD)
    c = db.cursor()
    query = """\
    SELECT aut.name,
       COUNT(l.path) AS views
    FROM log l
    INNER JOIN articles art ON art.slug=split_part(l.path, '/', 3)
    INNER JOIN authors aut ON aut.id=art.author
    WHERE l.method='GET'
    AND l.status='200 OK'
    GROUP BY aut.name
    ORDER BY views DESC
    """
    c.execute(query)
    authors = c.fetchall()
    db.close()
    return authors


def get_day_most_errors():
    """Return date and percents erros in the 'database'."""
    db = psycopg2.connect(database=DBNAME, user=USER, password=PASSWORD)
    c = db.cursor()
    query = """\
    SELECT TO_CHAR(DATE(l.time), 'DD/MM/YYYY') AS DATE,
       TO_CHAR(CAST(((COUNT(l.status)::DECIMAL * 100) / x.qtd::DECIMAL) AS DECIMAL), '999D99') AS PERCENTS
    FROM log l
    INNER JOIN qtdStatusOkByTime x ON DATE(l.time) = x.date
    WHERE l.status <> '200 OK'
    GROUP BY DATE(l.time),
            x.qtd
    HAVING ((COUNT(l.status) * 100) / x.qtd) > 1;
    """
    c.execute(query)
    inf = c.fetchall()
    db.close()
    return inf
