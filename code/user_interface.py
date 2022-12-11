# Author: Daniah Mohammed
import psycopg2
import psycopg2.extras      #To access the attributes as "column name not  list index number"
import pgsql_credentials
import random


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
                print("Welcome to DaJai BookStore\nEnter Q whenever you wish to quit\nPlease select one of the following options\n1.   Sign In\t2.    Sign Up\n")
                option = input("Enter your selection number here: ")
                if option == '1':
                    user_username = input("Username: \n")
                    user_password = input("Password: \n")
                    #cur.execute("FROM Users SELECT")
                if option == '2':
                    user_first_name = input("Please enter your first name: \n")
                    user_last_name  = input("Please enter your last name: \n")
                    user_password = input("Please create a password [15 char limit]:  \n")
                    unique = True
                    while unique:
                        user_username = input("Please create a username [15 char limit]:  \n")
                        cur.execute('SELECT username FROM Users;')
                        list_of_users = cur.fetchall()
                        for usernames in list_of_users[len(list_of_users)][0]:
                            usernames = str(usernames)
                            print(type(usernames))
                            if user_username  == usernames:
                                unique = False
                                print("Username is not unqiue, please try again\n")
                        unique = False

                if option == 'q' or option == 'Q':
                    quit = False

            

            
except Exception as error:
    print(error)


finally:
    if conn is not None:
        conn.close() 