# Author: Daniah Mohammed and JiaQi Han 
import random 

def ownerscript(username):
    logged_in = True; 
    while logged_in:
        # ask the owner what they would like to do
        print("-----OWNER MAIN MENU-----")
        print("\t1. View your collections")
        print("\t2. Generate reports")
        print("\t3. Logout")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            print("Here is a list of your currently available collections: ")
            # list collections owned by currently signed in owner 
            query = "SELECT DISTINCT collection_name FROM Collection WHERE owner='" + username + "'"
            cur.execute(query) 
            for record in cur.fetchall():
                print(record[0])
            count_collect = 0
            while count_collect == 0:
                count_collect = 0 
                collection = input("Please enter the name of the collection you are selecting: ")
                # check collection name is valid 
                find_collection = "SELECT DISTINCT * FROM Collection WHERE owner='" + username + "' AND collection_name='" + collection + "'"
                cur.execute(find_collection) 
                for collect in cur.fetchall():
                    count_collect += 1
                if count_collect == 0:
                    print("Please enter a valid collection name")
                else:
                    print("What would you like to do?")
                    print("\t1. Add a book to this collection")
                    print("\t2. Remove an exisiting book from this collection")
                    collection_choice = input("Enter the number of your choice: ")
                    choice_ok = False; 
                    while not choice_ok: 
                        if collection_choice == "1": 
                            print("Here is the list of books that are currently not in your collection: ")
                            find_books = "SELECT b.name, b.ISBN FROM Book b WHERE NOT EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + username + "' AND collection_name='" + collection + "' AND c.ISBN=b.ISBN)"
                            cur.execute(find_books)
                            for book in cur.fetchall():
                                print("Name: " + book[0] + " ISBN: " + book[1])
                            count_book = 0
                            while count_book == 0:
                                count_book = 0
                                book = input("Enter the ISBN of the book you wish to add to your collection: ")
                                #check that book selection is valid 
                                find_book = "SELECT * FROM Book WHERE ISBN='" + book + "'" 
                                cur.execute(find_book) 
                                book_values = []
                                for x in cur.fetchall():
                                    book_values = x
                                    count_book += 1 
                                if count_book == 0:
                                    print("Please enter a valid ISBN")
                                else:
                                    quantity = input("How many copies would you like to stock? ")
                                    add_book = "INSERT INTO Collection Values ('" + username + "','" + book + "','" + collection + "','" + quantity + "');" 
                                    cur.execute(add_book)
                                    print("successfully added " + book_values[1] + " to Collection") 
                                    choice_ok = True
                        if collection_choice == "2": 
                            print("Here is the list of books that are currently in your collection: ")
                            find_books = "SELECT b.name, b.ISBN FROM Book b WHERE EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + username + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN)"
                            cur.execute(find_books)
                            for book in cur.fetchall():
                                print("Name: " + book[0] + " ISBN: " + book[1])
                            count_book = 0
                            while count_book == 0:
                                count_book = 0
                                book = input("Enter the ISBN of the book you wish to remove from your collection: ")
                                #check that book selection is valid 
                                find_book = "SELECT * FROM Collection WHERE ISBN='" + book + "' AND owner='" + username + "' AND collection_name='" + collection + "'" 
                                cur.execute(find_book) 
                                book_values = []
                                for x in cur.fetchall():
                                    book_values = x
                                    count_book += 1 
                                if count_book == 0:
                                    print("Please enter a valid ISBN")
                                else:
                                    delete_book = "DELETE FROM Collection WHERE ISBN='" + book + "' AND owner='" + username + "' AND collection_name='" + collection + "'"  
                                    cur.execute(delete_book)
                                    print("successfully removed " + book_values[1] + " to Collection") 
                                    choice_ok = True
                        else:
                            print("Please enter a valid selection")
        if choice == "2": 
            print("These are the types of reports available: ")
            print("1. Total sales vs. expenditures")
            print("2. Sales by Genre")
            print("3. Sales by Author") 
            report_choice = input("Enter the number of your choice: ")
            # while not choice_ok: 
            #     if report_choice == "1":
            #         choice_ok = True; 
            #         # query to get report and print
            #     else:
            #         print("Please select a valid choice")
        if choice == "3":
            print("You are now logged out")
            logged_in = False; 
            username = "null"
                
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
            run = True
            while run:
                user_username = input("Username: \n")
                user_password = input("Password: \n")
                cur.execute("SELECT username, password FROM Owner WHERE username = '" + user_username + "' AND password = '" + user_password + "';")
                creds = cur.fetchall()
                if  len(creds) == 0:
                    print("INVALID username or password, please try again\n")
                elif creds[0][0]  == user_username and creds[0][1] == user_password:
                    ownerscript(user_username)
                else:
                    print("INVALID username or password, please try again\n")  

except Exception as error:
    print(error)


finally:
    if conn is not None:
        conn.close() 