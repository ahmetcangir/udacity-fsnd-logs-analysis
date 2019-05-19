select articles.title, count(*) as num
    from log, articles
    where log.status='200 OK'
        and articles.slug = substr(log.path, 10)
    group by articles.title
    order by num desc
    limit 3;