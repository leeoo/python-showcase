-- -------------------------
-- Initialize account table.
-- -------------------------
--truncate table account;
INSERT INTO account(
    username,
    password,
    salt,
    password_hint,
    gender,
    age,
    phone_number,
    email,
    description,
    creator,
    modifier,
    created_at,
    updated_at,
    account_enabled,
    account_locked,
    account_expired,
    credentials_expired
) VALUES
    ('admin', 'admin', '', '', 'male', 20, '13812345678', 'admin@ifee.com', 'admin', 'ifee', NULL, now(), NULL, true, false, false, false),
    ('user2', 'user2', '', '', 'female', 20, '13812345678', 'user2@ifee.com', 'user', 'ifee', NULL, now(), NULL, true, false, false, false),
    ('user3', 'user3', '', '', 'male', 20, '13812345678', 'user3@ifee.com', 'user', 'ifee', NULL, now(), NULL, true, false, false, false),
    ('user4', 'user4', '', '', 'male', 20, '13812345678', 'user4@ifee.com', 'user', 'ifee', NULL, now(), NULL, true, false, false, false),
    ('user5', 'user5', '', '', 'female', 20, '13812345678', 'user5@ifee.com', 'user', 'ifee', NULL, now(), NULL, true, false, false, false);


INSERT INTO book(
    book_chinese_name,
    book_english_name,
    author_chinese_name,
    author_english_name,
    book_type, -- 书籍载体介质种类：如纸质、Mobi、ePub、PDF和TXT等
    book_class, -- 书籍分类：如人文社科、自然科学、IT、漫画、期刊杂志等
    description,
    reading_status, -- 阅读状态：未读、想读、正在阅读、已读等
    creator,
    modifier,
    created_at,
    updated_at
) VALUES
    ('动物农场', 'Animal farm', '奥威尔', '', 'Mobi', '人文社科', '', '已读', 'Lex', null, now(), null),
    ('人类群星的闪耀时', null, '奥威尔', '', 'Mobi', '人文社科', '', '已读', 'Lex', null, now(), null),
    ('最初的爱情，最后的仪式', null, null, '', 'Mobi', '人文社科', '', '已读', 'Lex', null, now(), null),
    ('大明王朝的七张面孔', null, null, '', 'Mobi', '人文社科', '', '已读', 'Lex', null, now(), null),
    ('简明Python教程', null, null, '', 'PDF', 'IT', '', '已读', 'Lex', null, now(), null),
    ('老人与海', '', '海明威', null, 'Mobi', '文学', '', '未完', 'Lex', null, now(), null)
;