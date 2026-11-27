WITH profile_user AS (
    SELECT user_id, created_at
    FROM Users
    WHERE user_id = %s
),
weeks AS (
    SELECT generate_series(
        date_trunc('week', CURRENT_DATE::timestamp) - INTERVAL '7 weeks',
        date_trunc('week', CURRENT_DATE::timestamp),
        INTERVAL '1 week'
    ) AS week_start
),
weekly_threads AS (
    SELECT date_trunc('week', t.created_at) AS week_start,
           COUNT(*) AS total
    FROM Threads t
    JOIN profile_user u ON u.user_id = t.user_id
    WHERE t.created_at >= (SELECT MIN(week_start) FROM weeks)
    GROUP BY 1
),
weekly_comments AS (
    SELECT date_trunc('week', c.created_at) AS week_start,
           COUNT(*) AS total
    FROM Comments c
    JOIN profile_user u ON u.user_id = c.user_id
    WHERE c.created_at >= (SELECT MIN(week_start) FROM weeks)
    GROUP BY 1
)
SELECT
    u.user_id,
    u.created_at AS joined_at,

    (SELECT COUNT(*) FROM Threads t
     WHERE t.user_id = u.user_id) AS thread_count,

    (SELECT COUNT(*) FROM Comments c
     WHERE c.user_id = u.user_id) AS comment_count,

    (SELECT COUNT(*)
     FROM votes v
     JOIN Threads t ON t.thread_id = v.thread_id
     WHERE t.user_id = u.user_id) AS thread_votes_received,

    (SELECT COUNT(DISTINCT f.user_id)
     FROM follows f
     WHERE f.followed_user_id = u.user_id) AS follower_count,

    (
        SELECT json_build_object(
            'id', t.thread_id,
            'title', t.title,
            'created_at', t.created_at
        )
        FROM Threads t
        WHERE t.user_id = u.user_id
        ORDER BY t.created_at DESC NULLS LAST, t.thread_id DESC
        LIMIT 1
    ) AS latest_thread,

    (
        SELECT COALESCE(
            json_agg(
                json_build_object('id', g.group_id, 'name', g.group_name)
                ORDER BY g.group_name
            ),
            '[]'::json
        )
        FROM Groups g
        WHERE EXISTS (
            SELECT 1
            FROM member_of m
            WHERE m.group_id = g.group_id
              AND m.user_id = u.user_id
        )
    ) AS groups,

    (
        SELECT json_agg(
            json_build_object(
                'week_start', w.week_start::date,
                'threads', COALESCE(t.total, 0),
                'comments', COALESCE(c.total, 0)
            )
            ORDER BY w.week_start
        )
        FROM weeks w
        LEFT JOIN weekly_threads t ON t.week_start = w.week_start
        LEFT JOIN weekly_comments c ON c.week_start = w.week_start
    ) AS weekly_activity

FROM profile_user u;