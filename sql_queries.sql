-- set search_path = "public"

SELECT datname FROM pg_database;

SELECT * FROM information_schema.tables
WHERE table_schema = 'public';

SELECT * FROM messages;

INSERT INTO messages (transport, target, message) VALUES ('mail', 'any@one.com', 'Hi there');
INSERT INTO messages (transport, target, message) VALUES ('file', 'john', 'Hi there2');