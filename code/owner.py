# script has the currently signed-in's username saved 
username = "test"

def ownerscript():
    logged_in = True; 
    while logged_in:
        # ask the owner what they would like to do
        print("-----OWNER MAIN MENU-----")
        print("Enter 'm' at any time to return to the main menu")
        print("\t1. View your collections")
        print("\t2. Generate reports")
        print("\t3. Logout")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            # print("Here is a list of your currently available collections: ")
            # list collections owned by currently signed in owner 
            print("Here is the list of books currently in your collection: ")
            query = "SELECT * FROM Collection WHERE owner='" + username + "'"
            cur.execute(query); 
            for record in cur.fetchall():
                print(record)
            collection = input("Please select a collection: ")
            if collection != 'q':
                print("What would you like to do?")
                print("\t1. Add a book to this collection")
                print("\t2. Remove an exisiting book from this collection")
                collection_choice = input("Enter the number of your choice: ")
                choice_ok = False; 
                while not choice_ok: 
                    if collection_choice == "1": 
                        # could also change to book title and show all results that match (for different editions of same book)
                        ISBN = input("Please enter the ISBN of the book to add") 
                        # find book in relation using query 
                        # add book to collection using query 
                        found = False #change it to actually find book in database 
                        if not found: 
                            # add book
                            print("Book added") 
                            choice_ok = True 
                        else:
                            add_book = input("This ISBN is not currently in the database. Would you like to add the information for the book? (Y/N)")
                            if add_book == "Y": 
                                choice_ok = True 
                                # collect book info and query to add book
                                print("Book information collected")
                            if add_book == "N": 
                                choice_ok = True 
                                print("Returning to collection selection...")
                    if collection_choice == "2": 
                        choice_ok = True; 
                        ISBN = input("Please enter the ISBN of the book from this collection to remove") 
                        # find book in collection and remove using query 
                        found = False 
                        if not found:
                            print("This book is not currently in this collection and can therefore not be removed")
                        else:
                            #remove book
                            print("Book removed from collection")
                    if collection_choice == "m":
                        choice_ok = True
                        print("Returning to main menu...") 
                    else:
                        print("Please select a valid choice")
    if choice == "2": 
        print("These are the types of reports available: ")
        print("1. Total sales vs. expenditures")
        # some other choices 
        report_choice = input("Enter the number of your choice: ")
        while not choice_ok: 
            if report_choice == "1":
                choice_ok = True; 
                # query to get report and print
            else:
                print("Please select a valid choice")
    if choice == "3":
        print("You are now logged out")
        logged_in = False; 
                
# Author: JiaQi Han
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
            ownerscript(); 

except Exception as error:
    print(error)


finally:
    if conn is not None:
        conn.close() 