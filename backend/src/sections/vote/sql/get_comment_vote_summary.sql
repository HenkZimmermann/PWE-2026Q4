SELECT COALESCE(SUM(v.direction), 0),
       COALESCE(MAX(v.direction) FILTER (WHERE v.user_id = %s), 0)
FROM comments AS c
LEFT JOIN comment_votes AS v ON v.comment_id = c.comment_id
WHERE c.comment_id = %s
  AND c.deleted_at IS NULL
GROUP BY c.comment_id;
