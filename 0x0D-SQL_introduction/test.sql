-- create table and fill with records
CREATE TABLE IF NOT EXISTS third_table (
id INT,
name VARCHAR(256),
score INT);

INSERT INTO third_table (id, name, score) VALUES (1, NULL, 10);
INSERT INTO third_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO third_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO third_table (id, name, score) VALUES (4, 'George', 8);
