# Author: Daniah Mohammed
import psycopg2
import psycopg2.extras      #To access the attributes as "column name not  list index number"
import pgsql_credentials

# This function creates an insert sql statment
def insert_script(table_name, values):
    script = "INSERT INTO " + table_name + " VALUES ("

    count = 0
    for value in values:
        if count == len(values)-1:
            script += "'" + value + "'" + ");" 
            break
        script += "'" +  value + "'" + ", "
        count+=1

    return script
 
#Create connection with db
conn = None

try:
    with psycopg2.connect(
                host = pgsql_credentials.hostname,
                dbname = pgsql_credentials.database,
                user = pgsql_credentials.username,
                password = pgsql_credentials.pwd,
                port = pgsql_credentials.port_id) as conn:

        
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            
            quit = True
            while(quit):
                print("Welcome to DaJai BookStore\nEnter Q whenever you wish to quit\nPlease select one of the following options\n1.   Sign In\t2.    Sign Up\t3.    Browse\n")
                option = input("Enter your selection number here: ")
                if option == '1':
                    user_username = input("Username: \n")
                    user_password = input("Password: \n")
                    #cur.execute("FROM Users SELECT")
                if option == 'q' or option == 'Q':
                    quit = False

            

            cur.execute('SELECT * FROM Users')
            for record in cur.fetchall():
                print(record)
except Exception as error:
    print(error)


finally:
    if conn is not None:
        conn.close() 