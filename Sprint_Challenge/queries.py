### Demo_Data queries

CREATE_DEMO_DATA_TABLE = '''
CREATE TABLE IF NOT EXISTS demo
("s" AUTOINCREMENT NOT NULL PRIMARY KEY VARCHAR(10),
"x" INT NOT NULL,
"y" INT NOT NULL;)
'''

INSERT_DEMO_DATA = '''
INSERT INTO demo ("s","x","y")
VALUES ('g', '3', '9'),
VALUES ('v', '5', '7'),
VALUES ('f', '8', '7');
'''

ROW_COUNT = '''
    SELECT COUNT(*) AS row_count
    FROM demo_data;
'''

XY_AT_LEAST_5 = '''
    SELECT COUNT(*) AS row_count
    FROM demo_data
    WHERE s BETWEEN x AND y
    GROUP BY s
    HAVING COUNT(*) >= 5;
'''

UNIQUE_Y = '''
    SELECT DISTINCT y
    FROM demo_data;
'''

DEMO_QUERIES = [CREATE_DEMO_DATA_TABLE,
                INSERT_DEMO_DATA,
                ROW_COUNT,
                XY_AT_LEAST_5,
                UNIQUE_Y]
