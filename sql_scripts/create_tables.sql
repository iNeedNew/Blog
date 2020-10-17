CREATE TABLE users (

    id INT PRIMARY KEY AUTO_INCREMENT,
    role_id INT DEFAULT 1,

    username VARCHAR(16) NOT NULL,
    email VARCHAR(64) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,

    first_name VARCHAR(24),
    last_name VARCHAR(24),
    country VARCHAR(128),
    city VARCHAR(128),
    dob DATE,

    create_account DATETIME,
    is_blocked BOOLEAN DEFAULT 1
);
-----
CREATE TABLE articles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    category_id INT,

    title VARCHAR(64),
    body TEXT,
    published DATETIME,

    is_blocked BOOLEAN DEFAULT 1
);
-----
CREATE TABLE comments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    parent_id INT,
    article_id INT,

    text VARCHAR(512),
    published DATETIME,
    is_blocked BOOLEAN DEFAULT 1
);
-----
CREATE TABLE follows (
    follower_id INT,
    followed_id INT,
    datetime DATETIME
);
-----
CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    named VARCHAR(128)
);
-----
CREATE TABLE likes_dislikes (
    user_id INT,
    article_id INT,
    appraisal BOOLEAN
);
