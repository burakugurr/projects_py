import psycopg2
import psycopg2.extras
import pandas as pd
import sqlalchemy
import sqlite3


hostname = 'localhost'
database = 'postgres'
username = 'postgres'
pwd = '147512'
port_id = '5432'

conn = None
cur = None

try:
    conn = psycopg2.connect(
                        host = hostname,
                        dbname = database,
                        user = username,
                        password = pwd,
                        port = port_id
                        )

    cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)

# Queries here 
# 
#
#
    cur.execute(' select * from employee LIMIT 5 ')
#    print(cur.fetchall())
    for record in cur.fetchall():
        print(record['first_last_name'], record['salary'])   



    conn.commit()

except Exception as err:
    print(err) 

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()



pd.read_sql('employee', conn)