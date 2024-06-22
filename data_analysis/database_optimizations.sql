CREATE INDEX

CREATE TABLE time (
    special_key VARCHAR PRIMARY KEY,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    month_name VARCHAR,
);

DROP VIEW IF EXISTS view_bizarra;
CREATE VIEW 