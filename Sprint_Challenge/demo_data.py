import sqlite3


conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()


def execute_query(curs, query):
    curs.execute(query)
    conn.commit()
    return curs.fetchall()


create_demo_data_table = '''
    CREATE TABLE IF NOT EXISTS demo(
    s TEXT NOT NULL,
    x INT NOT NULL,
    y INT NOT NULL);
'''

insert_demo_data = '''
    INSERT INTO demo ("s","x","y")
    VALUES ('g', '3', '9'),
    ('v', '5', '7'),
    ('f', '8', '7');
'''

row_count = '''
    SELECT COUNT(*) FROM demo;
'''

xy_at_least_5 = '''
    SELECT COUNT(*) FROM demo
    WHERE x >= 5 AND y >=5;
'''

unique_y = '''
    SELECT COUNT(DISTINCT y)
    FROM demo;
'''

demo_queries = [create_demo_data_table,
                insert_demo_data]


if __name__ == '__main__':
    execute_query(curs, demo_queries)
