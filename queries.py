# queries

query_1 = """
        SELECT articles.title, COUNT(log.path)
        FROM log
        JOIN articles ON log.path = CONCAT('/article/', articles.slug)
        GROUP BY articles.title
        ORDER BY count
        DESC LIMIT 3;"""

query_2 = """
        SELECT authors.name, SUM(articleCount.count) as views
        FROM authors ,
            (SELECT articles.author, COUNT(log.path)
            FROM log
            JOIN articles ON log.path = CONCAT('/article/', articles.slug)
            GROUP BY articles.author) AS articleCount
        WHERE authors.id = articleCount.author
        GROUP BY authors.name
        ORDER BY views
        DESC ;"""

query_3 = """
SELECT * FROM (
    SELECT a.day,
    round(cast((100*b.hits) AS NUMERIC ) / cast(a.hits AS NUMERIC ), 2)
    AS errp FROM
        (SELECT date(time) AS day, COUNT(*) AS hits FROM log GROUP BY day) AS a
        INNER JOIN
        (SELECT date(time) AS day, COUNT(*) AS hits FROM log WHERE status
        LIKE '%404%' GROUP BY day) AS b
    on a.day = b.day)
as t where errp > 1.0;
"""
