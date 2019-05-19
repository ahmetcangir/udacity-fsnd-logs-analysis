select authors.name, count(*) as num
    from articles, authors, log
    where log.status='200 OK'
    and authors.id = articles.author
    and articles.slug = substr(log.path, 10)
    group by authors.name
    order by num desc;