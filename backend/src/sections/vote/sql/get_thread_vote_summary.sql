SELECT COALESCE(SUM(v.direction), 0),
       COALESCE(MAX(v.direction) FILTER (WHERE v.user_id = %s), 0)
FROM threads AS t
LEFT JOIN votes AS v ON v.thread_id = t.thread_id
WHERE t.thread_id = %s
GROUP BY t.thread_id;
