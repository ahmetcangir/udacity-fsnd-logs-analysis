SELECT authors.name, count(*) AS num
    FROM articles, authors, log
    WHERE log.status='200 OK'
    AND authors.id = articles.author
    AND articles.slug = substr(log.path, 10)
    GROUP BY authors.name
    ORDER BY num DESC;