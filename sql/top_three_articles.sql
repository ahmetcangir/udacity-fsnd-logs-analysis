SELECT articles.title, count(*) AS num
    FROM log, articles
    WHERE log.status='200 OK'
        AND articles.slug = substr(log.path, 10)
    GROUP BY articles.title
    ORDER BY num DESC
    LIMIT 3;