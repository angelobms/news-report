# Database code for the DB News.

import psycopg2
import bleach

DBNAME = "news"


def get_most_popular_articles():
    """Return the three last articles the 'database', most popular."""
    db = psycopg2.connect(database=DBNAME)
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
    """Return the authors the 'database', most popular."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT aut.name, COUNT(l.path) AS views " +
              "FROM log l INNER JOIN articles art " +
              "ON art.slug=split_part(l.path, '/', 3) " +
              "INNER JOIN authors aut ON aut.id=art.author " +
              "WHERE l.method='GET' AND l.status='200 OK' " +
              "GROUP BY aut.name ORDER BY views DESC")
    articles = c.fetchall()
    db.close()
    return articles


def get_day_most_errors():
    """Return the authors the 'database', most popular."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("SELECT to_char(DATE(time), 'DD/MM/YYYY') as date, " +
              "to_char(cast((((select count(l2.status) as qtd " +
              "from log l2 where l2.status <> '200 OK' " +
              "group by DATE(l2.time) order by qtd " +
              "desc limit 1)::Decimal * 100) " +
              "/ (select count(l3.status) as qtd from log l3 " +
              "where l3.status =  '200 OK' " +
              "group by DATE(l3.time) order by qtd desc "
              "limit 1)::Decimal) as DECIMAL), '999D99') as percents " +
              "from log group by DATE(time) order by date desc limit 1;")
    inf = c.fetchall()
    db.close()
    return inf
