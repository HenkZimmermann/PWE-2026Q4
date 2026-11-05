INSERT INTO comments (thread_id, parent_comment_id, message, votes, user_id) 
VALUES (%s, %s, %s, %s, %s) RETURNING *;
