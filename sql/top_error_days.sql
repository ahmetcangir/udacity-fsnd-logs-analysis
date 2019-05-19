select error_rates.day, error_rates.rate AS error_rate
    from (
    select day, cast(error_count as real) / cast(total_count as real) as rate
        from (select http_requests_count.day,
            http_requests_count.count as total_count,
            http_error_counts.count as error_count
                from (select date_trunc('day', log.time) as day, count(*)
                    from log
                    group by day) as http_requests_count,
                (select date_trunc('day', log.time) as day, count(*)
                    from log
                    where log.status similar to '(4|5)%' -- 400, 500 series status codes
                    group by day) as http_error_counts
                where http_requests_count.day = http_error_counts.day) as daily_http_request_counts
        ) as error_rates
    where error_rates.rate > 0.01;