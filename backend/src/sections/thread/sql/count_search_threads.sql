SELECT COUNT(*) AS "totalCount"
FROM threads AS t
JOIN users AS u ON u.user_id = t.user_id
JOIN groups AS g ON g.group_id = t.group_id
WHERE (%(group_id)s::integer IS NULL OR t.group_id = %(group_id)s)
    AND (t.title ILIKE %(pattern)s OR t.message ILIKE %(pattern)s);
