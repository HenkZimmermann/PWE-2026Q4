SELECT
    t.thread_id AS id,
    t.title,
    t.message AS content,
    t.created_at AS "publishedAt",
    u.username AS "authorName",
    g.group_name AS "groupName",
    (SELECT COUNT(*) FROM comments AS c WHERE c.thread_id = t.thread_id) AS "commentCount"
FROM threads AS t
JOIN users AS u ON u.user_id = t.user_id
JOIN groups AS g ON g.group_id = t.group_id
WHERE t.thread_id = %s;
