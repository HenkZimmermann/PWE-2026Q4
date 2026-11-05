DELETE FROM follows WHERE user_id = %s;
DELETE FROM follows WHERE followed_user_id = %s;
DELETE FROM votes WHERE user_id = %s;
DELETE FROM member_of WHERE user_id = %s;
DELETE FROM comments WHERE user_id = %s;
DELETE FROM threads WHERE user_id = %s;
DELETE FROM users WHERE user_id = %s;