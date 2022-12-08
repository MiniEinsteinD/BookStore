# Author: Daniah Mohammed
import psycopg2
import psycopg2.extras

#Create connection with db  -- might hide in a diff file
hostname = 'localhost'
database = 'BookStore'
username = 'postgres'
pwd = 'Dano!123'
port_id = 5432
conn = None

try:
    with psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id) as conn:

        # To access the attributes as "column name not a number"
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            # Demo  
            #insert_script  = "INSERT INTO Publisher (email_address, first_name, last_name, password, balance) VALUES ('test.com', 'test', 'd1', 'shesh', 500)"
            insert_script  = "INSERT INTO Book (ISBN, name, page_num, price, publisher_percentage, publisher) VALUES ('1234567890123', 'test', 10, 12.5, 0.1, 'test.com') "
            # insert_values = [("1234567890123", "test", 10, 12.5, 0.1, "test.com")]
            # for record in insert_values:
            #     cur.execute(insert_script, record)
            cur.execute(insert_script)
            # update_script = 'UPDATE employee SET salary = salary + (salary * 0.5)'
            # cur.execute(update_script) 

            cur.execute('SELECT * FROM Book')
            for record in cur.fetchall():
                print(record)
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()