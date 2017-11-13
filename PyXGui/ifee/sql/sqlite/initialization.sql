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
    create_time,
    update_time,
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


