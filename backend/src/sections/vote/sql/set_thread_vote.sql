INSERT INTO votes (user_id, thread_id, direction)
SELECT %s, thread_id, %s
FROM threads
WHERE thread_id = %s
ON CONFLICT (user_id, thread_id) DO UPDATE SET direction = EXCLUDED.direction;
