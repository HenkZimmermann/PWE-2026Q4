UPDATE comments
SET message = '[gelöscht]', deleted_at = CURRENT_TIMESTAMP
WHERE comment_id = %s;
