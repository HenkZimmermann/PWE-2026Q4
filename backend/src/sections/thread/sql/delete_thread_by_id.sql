DELETE FROM comments WHERE thread_id = %s;
DELETE FROM votes WHERE thread_id = %s;
DELETE FROM threads WHERE thread_id = %s;