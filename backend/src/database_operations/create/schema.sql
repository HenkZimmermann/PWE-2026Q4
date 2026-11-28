CREATE TABLE IF NOT EXISTS Roles (
    role_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    permissions TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role_id SERIAL NOT NULL REFERENCES roles(Role_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS Groups (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(100) UNIQUE NOT NULL,
    category VARCHAR(100) NOT NULL,
    members INT DEFAULT 0,
    system_created BOOLEAN DEFAULT FALSE,
    description TEXT
);

CREATE TABLE IF NOT EXISTS Threads (
    thread_id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    user_id INT NOT NULL REFERENCES Users(user_id),
    votes INT DEFAULT 0,
    group_id INT NOT NULL REFERENCES Groups(group_id),
    title VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS Comments (
    comment_id SERIAL PRIMARY KEY,
    thread_id INT NOT NULL REFERENCES Threads(thread_id) ON DELETE CASCADE,
    parent_comment_id INT REFERENCES Comments(comment_id) ON DELETE CASCADE,
    message TEXT NOT NULL,
    votes INT DEFAULT 0,
    user_id INT NOT NULL REFERENCES Users(user_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS votes (
    user_id INT NOT NULL REFERENCES Users(user_id),
    thread_id INT REFERENCES Threads(thread_id) ON DELETE CASCADE,
    direction SMALLINT NOT NULL DEFAULT 1 CHECK (direction IN (-1, 1)),
    PRIMARY KEY (user_id, thread_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS member_of (
    user_id INT NOT NULL REFERENCES Users(user_id),
    group_id INT NOT NULL REFERENCES Groups(group_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);

CREATE TABLE IF NOT EXISTS follows (
    user_id INT NOT NULL REFERENCES Users(user_id),
    followed_user_id INT NOT NULL REFERENCES Users(user_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
