WITH matches AS (
    SELECT
        t.thread_id AS id,
        t.title,
        t.message AS content,
        t.created_at AS "publishedAt",
        u.username AS "authorName",
        g.group_name AS "groupName",
        COALESCE(c.comment_count, 0) AS "commentCount"
    FROM threads AS t
    JOIN users AS u ON u.user_id = t.user_id
    JOIN groups AS g ON g.group_id = t.group_id
    LEFT JOIN (
        SELECT thread_id, COUNT(*) AS comment_count
        FROM comments
        GROUP BY thread_id
    ) AS c ON c.thread_id = t.thread_id
    WHERE (%(group_id)s::integer IS NULL OR t.group_id = %(group_id)s)
        AND (t.title ILIKE %(pattern)s OR t.message ILIKE %(pattern)s)
),
page AS (
    SELECT *
    FROM matches
    ORDER BY "publishedAt" DESC NULLS LAST, id DESC
    LIMIT %(limit)s
)
SELECT
    COALESCE(json_agg(page ORDER BY page."publishedAt" DESC NULLS LAST, page.id DESC), '[]') AS threads,
    (SELECT COUNT(*) FROM matches) AS "totalCount"
FROM page;
