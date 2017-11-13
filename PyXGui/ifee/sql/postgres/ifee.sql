/**
 * 1)所有业务相关表必备的列：id, version, created_by, created_at, updated_by, updated_at, deleted。
 * 2)数据库名、表名、列名、sequence、函数名、触发器名全部使用下划线分隔并小写。
 * 3)金额用amount，数量用quantity。number可用no缩写，transaction可用tx缩写。损益可用pnl(即Profit and loss)表示。
 * 4)账户相关的数据表结构参考Apache Shiro认证授权框架。
 * 5)对于Postgres，想要在更新时自动更新updated_at列值，要么从程序中传递值过来，要么用Trigger。
 * 参考 https://stackoverflow.com/questions/2362871/postgresql-current-timestamp-on-update
 *
 * 更新历史
 * 2017-07-10
 * 所有表的主键统一改用id
 * 列名变更：creator -> created_by, modifier -> updated_by, creation_time -> created_at, modification_time -> updated_at。
 * 表名变更：payment -> expense, bao_xiao -> reimbursement
 *
 */
-- DROP DATABASE IF EXISTS ifee;

CREATE DATABASE ifee;


CREATE TABLE account(
    id SERIAL,
    version INTEGER NOT NULL,
    account_group_id INTEGER,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    salt VARCHAR(255),
    password_hint VARCHAR(50),
    gender VARCHAR(20),
    age INTEGER,
    phone_number VARCHAR(50),
    email VARCHAR(50),
    description VARCHAR(255),
    account_enabled BOOLEAN,
    account_locked BOOLEAN,
    account_expired BOOLEAN,
    credentials_expired BOOLEAN,
    created_by VARCHAR(50),
    updated_by VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- 更新时需要从程序中传递值过来，下同。
    deleted BOOLEAN,
    PRIMARY KEY (id)
);

CREATE TABLE account_group(
    id SERIAL,
    version INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255),
    created_by VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(50),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE portfolio(
    id SERIAL,
    version INTEGER NOT NULL,
    portfolio_name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255),
    created_by VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(50),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deleted BOOLEAN,
    PRIMARY KEY (id)
);

CREATE TABLE facility(
    id SERIAL,
    version INTEGER NOT NULL,
    facility_name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(255),
    created_by VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(50),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deleted BOOLEAN,
    PRIMARY KEY (id)
);

CREATE TABLE portfolio_position(
    id SERIAL,
    version INTEGER NOT NULL,
    position_name VARCHAR(50) NOT NULL UNIQUE,
    commitment_amount NUMERIC(25, 2),
    portfolio_id SERIAL,
    facility_id SERIAL,
    description VARCHAR(255),
    created_by VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(50),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deleted BOOLEAN,
    PRIMARY KEY (id)
);

-- 收入
CREATE TABLE income(
    id SERIAL,
    version INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    amount NUMERIC(25, 2),
    description VARCHAR(255),
    created_by VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(50),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deleted BOOLEAN,
    PRIMARY KEY (id)
);

-- 支出/开支
CREATE TABLE expense(
    id SERIAL,
    version INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    amount NUMERIC(25, 2),
    description VARCHAR(255),
    created_by VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(50),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deleted BOOLEAN,
    PRIMARY KEY (id)
);

-- 报销
CREATE TABLE reimbursement(
    id SERIAL,
    version INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    amount NUMERIC(25, 2),
    description VARCHAR(255),
    created_by VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(50),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deleted BOOLEAN,
    PRIMARY KEY (id)
);

-- 余额宝
CREATE TABLE yu_e_bao(
    id SERIAL,
    version INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    amount NUMERIC(25, 2),
    description VARCHAR(255),
    created_by VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(50),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deleted BOOLEAN,
    PRIMARY KEY (id)
);

CREATE TABLE book(
    id SERIAL,
    version INTEGER NOT NULL,
    book_chinese_name VARCHAR(50),
    book_english_name VARCHAR(50),
    author_chinese_name VARCHAR(100),
    author_english_name VARCHAR(100),
    book_type VARCHAR(20), -- 书籍载体介质种类：如纸质、Mobi、ePub、PDF和TXT等
    book_class VARCHAR(30), -- 书籍分类：如人文社科、自然科学、IT等
    description VARCHAR(255),
    reading_status VARCHAR(30), -- 阅读状态：未开始、想要阅读、正在阅读、已读等
    /* TODO 开篇时间、阅完时间、用时（以天为单位） */
    created_by VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(50),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deleted BOOLEAN,
    PRIMARY KEY (id)
);

CREATE TABLE todo(
    id SERIAL,
    version INTEGER NOT NULL,
    flag CHAR(1), -- 0 - 未开始, 1 - 进行中, 2 - Done
    add_or_reduce CHAR(1), -- +/-
    content VARCHAR(255),
    created_by VARCHAR(50),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(50),
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    deleted BOOLEAN,
    PRIMARY KEY (id)
);
