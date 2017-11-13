
DROP DATABASE IF EXISTS ifee;

CREATE DATABASE IF NOT EXISTS ifee;


CREATE TABLE account(
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    version INTEGER,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    salt VARCHAR(255),
    password_hint VARCHAR(50),
    gender VARCHAR(20),
    age INTEGER,
    phone_number VARCHAR(50),
    email VARCHAR(50),
    description VARCHAR(255),
    creator VARCHAR(50),
    modifier VARCHAR(50),
    create_time TIMESTAMP,
    update_time TIMESTAMP,
    account_enabled BOOLEAN,
    account_locked BOOLEAN,
    account_expired BOOLEAN,
    credentials_expired BOOLEAN,
    PRIMARY KEY (account_id)
);

CREATE TABLE portfolio(
    portfolio_id INTEGER PRIMARY KEY AUTOINCREMENT,
    version INTEGER,
    portfolio_name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255),
    creator VARCHAR(50),
    modifier VARCHAR(50),
    create_time TIMESTAMP,
    update_time TIMESTAMP
);

CREATE TABLE facility(
    facility_id INTEGER PRIMARY KEY AUTOINCREMENT,
    version INTEGER,
    facility_name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255),
    creator VARCHAR(50),
    modifier VARCHAR(50),
    create_time TIMESTAMP,
    update_time TIMESTAMP
);

CREATE TABLE portfolio_position(
    position_id INTEGER PRIMARY KEY AUTOINCREMENT,
    version INTEGER,
    position_name VARCHAR(50) NOT NULL UNIQUE,
    commitment_amount DOUBLE(25, 2),
    portfolio_id INTEGER,
    facility_id INTEGER,
    description VARCHAR(255),
    creator VARCHAR(50),
    modifier VARCHAR(50),
    create_time TIMESTAMP,
    update_time TIMESTAMP
);

-- 收入
CREATE TABLE income(
    income_id INTEGER PRIMARY KEY AUTOINCREMENT,
    version INTEGER,
    name VARCHAR(50) NOT NULL,
    amount DOUBLE(25, 2),
    description VARCHAR(255),
    creator VARCHAR(50),
    modifier VARCHAR(50),
    create_time TIMESTAMP,
    update_time TIMESTAMP
);

-- 支出
CREATE TABLE payment(
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    version INTEGER,
    name VARCHAR(50) NOT NULL,
    amount DOUBLE(25, 2),
    description VARCHAR(255),
    creator VARCHAR(50),
    modifier VARCHAR(50),
    create_time TIMESTAMP,
    update_time TIMESTAMP
);

-- 报销
CREATE TABLE bao_xiao(
    bao_xiao_id INTEGER PRIMARY KEY AUTOINCREMENT,
    version INTEGER,
    name VARCHAR(50) NOT NULL,
    amount DOUBLE(25, 2),
    description VARCHAR(255),
    creator VARCHAR(50),
    modifier VARCHAR(50),
    create_time TIMESTAMP,
    update_time TIMESTAMP
);

-- 余额宝
CREATE TABLE yu_e_bao(
    yu_e_bao_id INTEGER PRIMARY KEY AUTOINCREMENT,
    version INTEGER,
    name VARCHAR(50) NOT NULL,
    amount DOUBLE(25, 2),
    description VARCHAR(255),
    creator VARCHAR(50),
    modifier VARCHAR(50),
    create_time TIMESTAMP,
    update_time TIMESTAMP
);


