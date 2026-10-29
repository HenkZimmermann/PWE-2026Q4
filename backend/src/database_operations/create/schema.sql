CREATE TABLE IF NOT EXISTS Roles (
    role_id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL,
    permissions TEXT[] NOT NULL
);
CREATE TABLE IF NOT EXISTS Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    role_id SERIAL NOT NULL REFERENCES roles(Role_id)
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
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    message TEXT NOT NULL,
    user_id INT NOT NULL REFERENCES Users(user_id),
    votes INT DEFAULT 0,
    group_id INT NOT NULL REFERENCES Groups(group_id),
    title VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS Comments (
    comment_id SERIAL PRIMARY KEY,
    thread_id INT NOT NULL REFERENCES Threads(thread_id),
    parent_comment_id INT REFERENCES Comments(comment_id),
    message TEXT NOT NULL,
    votes INT DEFAULT 0,
    user_id INT NOT NULL REFERENCES Users(user_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);