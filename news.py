#!/usr/bin/env python3

from flask import Flask, request, redirect, url_for

import newsdb

app = Flask(__name__)

# HTML template
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Report of News</title>
  </head>
  <body>
    <h1>Report of News</h1>
        <!-- post content will go here -->
%s
  </body>
</html>
'''

# HTML template for articles
MOST_POPULAR_ARTICLES = '''\
    <div><ul><li><em class=date>%s</em> - %s views</li></ul></div>
'''

# HTML template for authors
MOST_POPULAR_AUTHORS = '''\
    <div><ul><li><em class=date>%s</em> - %s views</li></ul></div>
'''

# HTML template for erross
MOST_ERROS = '''\
    <div><ul><li><em class=date>%s</em> - %s%% error</li></ul></div>
'''


@app.route('/', methods=['GET'])
def main():

    TITLE1 = "<h2>The three most popular articles of all time:</h2>"
    TITLE2 = "<h2>The authors of most popular articles of all time:</h2>"
    TITLE3 = "<h2>Day in which more than 1%" +\
        " of requests result in errors:</h2>"

    '''Main page of the news report.'''
    most_popular_articles = TITLE1 + \
        "".join(MOST_POPULAR_ARTICLES % (text, date)
                for text, date in newsdb.get_most_popular_articles())

    most_popular_authors = TITLE2 + \
        "".join(MOST_POPULAR_AUTHORS % (text, date)
                for text, date in newsdb.get_most_popular_authors())

    day_most_errors = TITLE3 + \
        "".join(MOST_ERROS % (text, date)
                for text, date in newsdb.get_day_most_errors())

    html = HTML_WRAP % most_popular_articles + \
        most_popular_authors + day_most_errors
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
