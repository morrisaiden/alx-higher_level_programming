-- lists all records of the table second_table of the database hbtn_0c_0 in MySQL server.
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)
-- Records should be listed by descending score

INSERT INTO second_table (score, name)
VALUES(18, 'Aria'),
(12, 'Aria');
DELETE FROM second_table WHERE name="George";

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name !='' ORDER BY score DESC;
