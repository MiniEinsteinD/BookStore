# Author: Daniah Mohammed
import psycopg2
import psycopg2.extras      #To access the attributes as "column name not  list index number"
import dani



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
                host = dani.hostname,
                dbname = dani.database,
                user = dani.username,
                password = dani.pwd,
                port = dani.port_id) as conn:

        
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
                    check = True
                    while check:
                        unique = True
                        user_username = input("Please create a username [15 char limit]:  \n")
                        cur.execute('SELECT username FROM Users;')
                        for usernames in cur.fetchall():
                            if user_username  == usernames[0]:
                                print("Username is not unqiue, please try again\n")
                                unique = False
                                break
                        if unique:
                            cur.execute(insert_script("Users", [user_username, user_first_name, user_last_name, user_password, "300"]))
                            check = False

                if option == 'q' or option == 'Q':
                    quit = False

            

            
except Exception as error:
    print(error)


finally:
    if conn is not None:
        conn.close() 