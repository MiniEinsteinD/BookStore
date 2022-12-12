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
            cart = []
            order_num = 1000  
                 
            def place_order(owner, collection, cart): 
                total_price = 0; 
                for book in cart:
                    cur.execute("SELECT b.price FROM Book b WHERE b.ISBN='" + book[0] + "EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + owner + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN);")
                    price = cur.fetchall
                    print(price[0][0])

                cart = [] 
                return 

            def view_app(loggedin):
                while loggedin:
                    seller = choose_seller()
                    collection = choose_collection(seller)
                    browse = True
                    while browse: 
                        browse_option = choose_browse_option(seller, collection)
                        if browse_option == "1":
                            browse_by_book_name(seller, collection)
                        elif browse_option == "2":
                            browse_by_author_name(seller, collection)
                        elif browse_option == "3":
                            browse_by_ISBN(seller, collection)
                        elif browse_option == "4":
                            browse_by_genre(seller, collection)
                        elif browse_option == "5":
                            browse = False 
                            if len(cart) > 0:
                                print("Here is your cart: ")
                                print(cart) 
                                buy = input("Purchase books? (y/n) ")
                                if buy == "y":
                                    place_order(seller, collection, cart) 
                        else:
                            print("Please select a valid option")
                    check = input("Continue shopping? (y/n): ")
                    if check == "n":
                        loggedin = False 

            def choose_seller():
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t SELLERS \t")
                cur.execute("SELECT username, first_name, last_name FROM Owner;")
                seller_option = cur.fetchall()

                for seller in seller_option:
                    print("Owner username: " + seller[0])
                    print("\t First name: " + seller[1] + "Last name: " + seller[2])
                return input("Please enter the seller's username you wish to purches your books from: ")

            def choose_collection(ownername):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t COLLECTIONS \t")
                cur.execute("SELECT DISTINCT collection_name FROM Collection WHERE owner='" + ownername +"'")
                collections = cur.fetchall()
                for i in collections:
                    print("Collection name: " + i[0])
                return input("Please enter the collection name you wish to purches your books from: ")

            def choose_browse_option(owner, collection):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t BROWSE OPTION \t")
                print("All books in the collection you selected\n")
                cur.execute("SELECT b.name, b.ISBN FROM Book b WHERE EXISTS (SELECT 1 FROM Collection c WHERE c.owner='" + owner + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN)" )
                list_of_books_in_collection = cur.fetchall()
                for i in list_of_books_in_collection:
                    print("[Book Name: " + i[0] + "]\t    [Book's ISBN: " + i[1] + "]\n")
                print("Choose on of the options to search you book")
                print("\t1. Book Name")
                print("\t2. Author Name")
                print("\t3. ISBN")
                print("\t4. Genre")
                print("\t5. Select a different collection")
                
                return input("Please enter your option: ")

            def browse_by_book_name(owner, collection):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t BROWSE BY BOOK NAME \t")
                search_name = input("Please enter the name of the book you wish to buy: ")
                cur.execute("SELECT b.name, b.ISBN, c.quantity FROM Book b, Collection c WHERE b.name='" + search_name + "' AND c.owner='" + owner + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN")
                list_of_books = cur.fetchall()
                if len(list_of_books) == 0:
                    print("No results")
                elif len(list_of_books) == 1:
                    add_to_cart = input("Add " + list_of_books[0][0] + " to cart? (y/n) ")
                    print("There are " + str(list_of_books[0][2]) + " books in stock")
                    quantity = input("How many books would you like to purchase? ") 
                    if (int(quantity) > list_of_books[0][2]):
                        print("Not enough stock")
                    elif add_to_cart == "y":
                        cart.append([list_of_books[0][1], quantity])
                else:
                    print("Here is the list of books that match your search: ")
                    for book in list_of_books: 
                        print("[Book Name: " + book[0] + "]\t    [Book's ISBN: " + book[1] + "]\n")
                    selected_book = input("Enter the ISBN of the book you would like to add to your cart: ")
                    valid_book = False 
                    for book in list_of_books: 
                        if selected_book == book[1]:
                            valid_book = True
                            break 
                    if valid_book:
                        print("There are " + str(list_of_books[0][2]) + " books in stock")
                        quantity = input("How many books would you like to purchase? ") 
                        if int(quantity) > list_of_books[0][2]:
                            print("Not enough stock")
                        elif int(quantity) > 0:
                            cart.append([list_of_books[0][1], quantity]) 
                    else:
                        print("Invalid ISBN entered") 
                return 1

            def browse_by_ISBN(owner, collection):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t BROWSE BY BOOK ISBN \t")
                isbn = input("Enter the ISBN of the book you wish to buy: ")
                cur.execute("SELECT b.name, b.ISBN, c.quantity FROM Book b, Collection c WHERE b.isbn='" + isbn + "' AND c.owner='" + owner + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN")
                list_of_books = cur.fetchall()
                if (len(list_of_books) == 0):
                    print("No results")
                else:
                    add_to_cart = input("Add " + list_of_books[0][0] + " to cart? (y/n) ")
                    print("There are " + str(list_of_books[0][2]) + " books in stock")
                    quantity = input("How many books would you like to purchase? ") 
                    if (int(quantity) > list_of_books[0][2]):
                        print("Not enough stock")
                    elif add_to_cart == "y":
                        cart.append([list_of_books[0][1], quantity])
                return 1

            def browse_by_author_name(owner, collection):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t BROWSE BY AUTHOR NAME \t")
                fname = input("\nPlease Enter the author's first name: ")
                lname = input("\nPlease enter the author's last name: ")
                cur.execute("SELECT DISTINCT b.name, b.ISBN, c.quantity FROM Book b, Collection c WHERE c.owner='" + owner + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN AND EXISTS (SELECT 1 FROM Is_Author a WHERE b.ISBN=a.ISBN AND a.first_name='" + fname + "' AND a.last_name='" + lname + "')" )
                list_of_books = cur.fetchall()
                if (len(list_of_books) == 0):
                    print("No results")
                elif len(list_of_books) == 1:
                    add_to_cart = input("Add " + list_of_books[0][0] + " to cart? (y/n) ")
                    print("There are " + str(list_of_books[0][2]) + " books in stock")
                    quantity = input("How many books would you like to purchase? ") 
                    if (int(quantity) > list_of_books[0][2]):
                        print("Not enough stock")
                    elif add_to_cart == "y":
                        cart.append([list_of_books[0][1], quantity])
                else:
                    print("Here is the list of books that match your search: ")
                    for book in list_of_books: 
                        print("[Book Name: " + book[0] + "]\t    [Book's ISBN: " + book[1] + "]\n")
                    selected_book = input("Enter the ISBN of the book you would like to add to your cart: ")
                    valid_book = False 
                    for book in list_of_books: 
                        if selected_book == book[1]:
                            valid_book = True
                            break 
                    if valid_book:
                        print("There are " + str(list_of_books[0][2]) + " books in stock")
                        quantity = input("How many books would you like to purchase? ")
                        if (int(quantity) > list_of_books[0][2]):
                            print("Not enough stock")
                        elif int(quantity) > 0:
                            cart.append([list_of_books[0][1], quantity]) 
                    else:
                        print("Invalid ISBN entered") 
                return 1

            def browse_by_genre(owner, collection):
                print("------------------------------------------------------------------------------------------------------------\n")
                print("\t BROWSE BY BOOK GENRE \t")
                genre = input("\nPlease enter the desired genre: ")
                cur.execute("SELECT DISTINCT b.name, b.ISBN, c.quantity FROM Book b, Collection c WHERE c.owner='" + owner + "' AND c.collection_name='" + collection + "' AND c.ISBN=b.ISBN AND EXISTS (SELECT 1 FROM In_Genre g WHERE b.ISBN=g.ISBN AND g.genre='" + genre + "')")
                list_of_books = cur.fetchall()
                if (len(list_of_books) == 0):
                    print("No results")
                elif len(list_of_books) == 1:
                    add_to_cart = input("Add " + list_of_books[0][0] + " to cart? (y/n) ")
                    print("There are " + str(list_of_books[0][2]) + " books in stock")
                    quantity = input("How many books would you like to purchase? ") 
                    if (int(quantity) > list_of_books[0][2]):
                        print("Not enough stock")
                    elif add_to_cart == "y":
                        cart.append([list_of_books[0][1], quantity])
                else:
                    print("Here is the list of books that match your search: ")
                    for book in list_of_books: 
                        print("[Book Name: " + book[0] + "]\t    [Book's ISBN: " + book[1] + "]\n")
                    selected_book = input("Enter the ISBN of the book you would like to add to your cart: ")
                    valid_book = False 
                    for book in list_of_books: 
                        if selected_book == book[1]:
                            valid_book = True
                            break 
                    if valid_book:
                        print("There are " + str(list_of_books[0][2]) + " books in stock")
                        quantity = input("How many books would you like to purchase? ") 
                        if (int(quantity) > list_of_books[0][2]):
                            print("Not enough stock")
                        elif int(quantity) > 0:
                            cart.append([list_of_books[0][1], quantity]) 
                    else:
                        print("Invalid ISBN entered") 
                return 1

            print("Welcome to DaJia BookStore\nEnter Q whenever you wish to quit\nPlease select one of the following options")
            print("\t1. Sign In")
            print("\t2. Sign Up")
            print("\tEnter q to quit")
            option = input("Enter your selection number here: ")
            if option == '1':
                loggedin = False
                while not loggedin:
                    user_username = input("Username: ")
                    user_password = input("Password: ")
                    cur.execute("SELECT username, password FROM Users WHERE username = '" + user_username + "' AND password = '" + user_password + "';")
                    creds = cur.fetchall()
                    if  len(creds) == 0:
                        print("INVALID username or password, please try again\n")
                    elif creds[0][0]  == user_username and creds[0][1] == user_password:
                        loggedin = True
                    else:
                        print("INVALID username or password, please try again\n") 
                view_app(loggedin)  
                print("Goodbye! ")

            if option == '2':
                user_first_name = input("Please enter your first name: \n")
                user_last_name  = input("Please enter your last name: \n")
                user_password = input("Please create a password [15 char limit]:  \n")
                loggedin = False
                while not loggedin:
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
                        loggedin = True
                view_app(loggedin) 
                print("Goodbye!")


            

            
except Exception as error:
    print(error)


finally:
    if conn is not None:
        conn.close() 