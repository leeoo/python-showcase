-- -------------------------
-- Alter tables.
-- -------------------------

ALTER TABLE payment RENAME TO expense;
ALTER TABLE bao_xiao RENAME TO reimbursement;


ALTER TABLE account RENAME account_id TO id;
ALTER TABLE account RENAME creation_time TO created_at;
ALTER TABLE account RENAME modification_time TO updated_at;


ALTER TABLE book RENAME book_id TO id;
ALTER TABLE book RENAME creation_time TO created_at;
ALTER TABLE book RENAME modification_time TO updated_at;





