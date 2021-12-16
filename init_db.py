import psycopg2
import config


conn = psycopg2.connect(database=config.db_connect['database'],
                        user=config.db_connect['user'],
                        password=config.db_connect['password'],
                        host=config.db_connect['host'],
                        port=config.db_connect['port'])
cursor = conn.cursor()
file = open('schema.sql', encoding="utf8")

cursor.execute(file.read())
conn.commit()
conn.close()
