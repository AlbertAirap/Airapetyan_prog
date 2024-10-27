import psycopg2

conn = psycopg2.connect(
    user="postgres",
    password="Albert2004",
    host="localhost",
    port="5432"
)

conn.autocommit = True

cursor = conn.cursor()

create_table_query = '''
CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,             
    event_name VARCHAR(100) NOT NULL,
    type VARCHAR(100) NOT NULL, 
    location VARCHAR(100) NOT NULL,   
    event_time TIMESTAMP NOT NULL,     
    duration INTERVAL NOT NULL,       
    price DECIMAL(10, 2) NOT NULL  
);
'''
cursor.execute(create_table_query)
print("Таблица tickets создана.")
conn.commit()
cursor.close()
conn.close()