SELECT
    u.user_id AS id,
    u.username,

    (
        SELECT COUNT(*)
        FROM threads t
        WHERE t.user_id = u.user_id
    ) AS "threadCount",

    (
        SELECT COUNT(*)
        FROM comments c
        WHERE c.user_id = u.user_id
    ) AS "commentCount",

    (
        SELECT g.group_name
        FROM threads t
        JOIN groups g ON g.group_id = t.group_id
        WHERE t.user_id = u.user_id
        GROUP BY g.group_id, g.group_name
        ORDER BY COUNT(*) DESC, g.group_id ASC
        LIMIT 1
    ) AS "mostActiveGroupName"

FROM users u
ORDER BY u.username ASC;