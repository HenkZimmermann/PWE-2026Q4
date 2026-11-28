INSERT INTO comment_votes (user_id, comment_id, direction)
SELECT %s, comment_id, %s
FROM comments
WHERE comment_id = %s
ON CONFLICT (user_id, comment_id) DO UPDATE SET direction = EXCLUDED.direction;
