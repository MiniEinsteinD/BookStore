# Author: Daniah Mohammed
import psycopg2
import psycopg2.extras      #To access the attributes as "column name not  list index number"
import dani
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
                host = dani.hostname,
                dbname = dani.database,
                user = dani.username,
                password = dani.pwd,
                port = dani.port_id) as conn:



        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            def choose_seller():
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t SELLERS \t")
                cur.execute("SELECT username, first_name, last_name FROM Owner;")
                seller_option = cur.fetchall()

                for seller in seller_option:
                    print("[Owner username: " + seller[0] + "]\t    [Owner first name: " + seller[1] + "]\t     [Owner last name: " + seller[2] + "]\n")
                return input("Please enter the seller's username you wish to purches your books from\n")

            def choose_collection(ownername):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t COLLECTIONS \t")
                cur.execute("SELECT DISTINCT collection_name FROM Collection WHERE owner='" + ownername +"'")
                collections = cur.fetchall()
                for i in collections:
                    print("[collection name: " + i[0] + "]\n")
                return input("Please enter the collection name you wish to purches your books from\n")
            def browse_option(owner, collection):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t BROWSE OPTION \t")
                print("All books in the collection you selected\n")
                cur.execute("SELECT b.name, b.ISBN FROM Book b WHERE EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + owner + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN)" )
                list_of_books_in_collection = cur.fetchall()
                for i in list_of_books_in_collection:
                    print("[Book Name: " + i[0] + "]\t    [Book's ISBN: " + i[1] + "]\n")
                print("Choose on of the options to search you book\n- Book Name\t- Author Name\t- ISBN\t- genre\n")
                
                return input("Please enter your option: ")
            def browse_by_book_name(owner, collection):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t BROWSE BY BOOK NAME \t")
                search_name = input("Please Enter the name of the book you wish to buy")
                cur.execute("SELECT b.name, b.ISBN FROM Book b WHERE b.name='" + search_name + "' AND EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + owner + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN)")
                list_of_books = cur.fetchall()
                print(list_of_books)
                return 1
            def browse_by_ISBN(owner, collection):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t BROWSE BY BOOK ISBN \t")
                cur.execute("SELECT b.ISBN FROM Book b WHERE EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + owner + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN);")
                list_of_books = cur.fetchall()
                print(list_of_books)
                return 1
            def browse_by_author_name(owner, collection):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t BROWSE BY AUTHOR NAME \t")
                fname = input("\nPlease Enter the author's first name: ")
                lname = input("\nPlease enter the author's last name: ")
                cur.execute("SELECT DISTINCT b.name, b.ISBN FROM Book b WHERE EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + owner + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN) AND EXISTS (SELECT 1 FROM Is_Author a WHERE b.ISBN=a.ISBN AND a.first_name='" + fname + "' AND a.last_name='" + lname + "')" )
                list_of_books = cur.fetchall()
                print(list_of_books)
                return 1
            def browse_by_genre(owner, collection):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t BROWSE BY BOOK GENRE \t")
                genre = input("\nPlease enter the desired genre: ")
                cur.execute("SELECT DISTINCT b.name, b.ISBN FROM Book b WHERE EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + owner + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN) AND EXISTS (SELECT 1 FROM In_Genre g WHERE b.ISBN=g.ISBN AND g.genre='" + genre + "')")
                list_of_books = cur.fetchall()
                print(list_of_books)
                return 1

            quit = True
            while(quit):
                print("Welcome to DaJia BookStore\nEnter Q whenever you wish to quit\nPlease select one of the following options\n1.   Sign In\t2.    Sign Up\n")
                option = input("Enter your selection number here: ")
                if option == '1':
                    check = True
                    while check:
                        valid = False
                        user_username = input("Username: \n")
                        user_password = input("Password: \n")
                        cur.execute("SELECT username, password FROM Users WHERE username = '" + user_username + "' AND password = '" + user_password + "';")
                        creds = cur.fetchall()
                        if  len(creds) == 0:
                            print("INVALID username or password, please try again\n")
                        elif creds[0][0]  == user_username and creds[0][1] == user_password:
                            valid = True
                        else:
                            print("INVALID username or password, please try again\n") 
                        if valid:
                            check = False
                    seller = choose_seller()
                    collection = choose_collection(seller)
                    browse_option = browse_option(seller, collection)

                    if browse_option == "Book Name":
                        browse_by_book_name(seller, collection)
                    elif browse_option == "Author Name":
                        browse_by_author_name(seller, collection)
                    elif browse_option == "ISBN":
                        browse_by_ISBN(seller, collection)
                    elif browse_option == "genre":
                        browse_by_genre(seller, collection)

                if option == '2':
                    user_first_name = input("Please enter your first name: \n")
                    user_last_name  = input("Please enter your last name: \n")
                    user_password = input("Please create a password [15 char limit]:  \n")
                    check = True
                    while check:
                        unique = True
                        user_username = input("Please create a username [15 char limit]:  \n")
                        cur.execute("SELECT username FROM Users;")
                        for usernames in cur.fetchall():
                            if user_username  == usernames[0]:
                                print("Username is not unqiue, please try again\n")
                                unique = False
                                break
                        if unique:
                            cur.execute(insert_script("Users", [user_username, user_first_name, user_last_name, user_password, str(random.randint(50, 500)) ]))
                            check = False
                    seller = choose_seller()
                    collection = choose_collection(seller)
                    browse_option = browse_option(seller, collection)
                    if browse_option == "Book Name":
                        browse_by_book_name(seller, collection)
                    elif browse_option == "Author Name":
                        browse_by_author_name(seller, collection)
                    elif browse_option == "ISBN":
                        browse_by_ISBN(seller, collection)
                    elif browse_option == "genre":
                        browse_by_genre(seller, collection)

                if option == 'q' or option == 'Q':
                    quit = False

            

            
except Exception as error:
    print(error)


finally:
    if conn is not None:
        conn.close() 