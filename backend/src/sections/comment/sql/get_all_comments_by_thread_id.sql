SELECT
    c.comment_id AS id,
    c.message AS content,
    c.created_at AS "publishedAt",
    u.username AS "authorName"
FROM comments AS c
JOIN users AS u ON u.user_id = c.user_id
WHERE c.thread_id = %s
ORDER BY c.created_at ASC NULLS LAST, c.comment_id ASC;
