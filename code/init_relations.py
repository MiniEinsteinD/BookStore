# Author: Daniah Mohammed and JiaQi Han 
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

            # creating dummy values - init the tables with those values
            #-----------------------------------------------------------
            # create users
            cur.execute(insert_script("Users", ["user1", "Ahmed", "Elroby", "12345", "50"]))
            cur.execute(insert_script("Users", ["user2", "Moe", "Za", "54321", "500"]))
            cur.execute(insert_script("Users", ["user3", "Dani", "Mo", "12345D", "300"]))
            #----------------------------------------------------------------------------------------------------------------------
            # create owner
            cur.execute(insert_script("Owner", ["owner1", "Ali", "Alex", "54321", "500"] ))
            cur.execute(insert_script("Owner", ["owner2", "Janet", "Smith", "54321", "500"] ))
            #----------------------------------------------------------------------------------------------------------------------
            # create publishers
            cur.execute(insert_script("Publisher", ["publ1@test.ca", "Bob", "Ta", "54321t", "500"]))
            cur.execute(insert_script("Publisher", ["publ2@test.ca", "John", "Fa", "54321t", "450"]))
            cur.execute(insert_script("Publisher", ["publ3@test.ca", "Tash", "Feen", "54321t", "550"]))
            #----------------------------------------------------------------------------------------------------------------------
            # create books
            for x in range (1, 11):
                isbn = str(1234567890000 + x)
                book_name = "book" + str(x)
                page_num = str(random.randint(250, 650))
                price = str(random.randint(20, 50))
                pub_percent = str(round(random.random(), 2))
                cur.execute(insert_script("Book", [isbn, book_name, page_num, price, pub_percent, "publ1@test.ca"]))

            for x in range (11, 21):
                isbn = str(1234567890000 + x)
                book_name = "book" + str(x)
                page_num = str(random.randint(250, 650))
                price = str(random.randint(20, 50))
                pub_percent = str(round(random.random(), 2))
                cur.execute(insert_script("Book", [isbn, book_name, page_num, price, pub_percent, "publ2@test.ca"]))

            for x in range (21, 31):
                isbn = str(1234567890000 + x)
                book_name = "book" + str(x)
                page_num = str(random.randint(250, 650))
                price = str(random.randint(20, 50))
                pub_percent = str(round(random.random(), 2))
                cur.execute(insert_script("Book", [isbn, book_name, page_num, price, pub_percent, "publ3@test.ca"]))
            #----------------------------------------------------------------------------------------------------------------------
            # create address
            cur.execute(insert_script("Address", ["K2OW0P", "1", "street1", "Ottawa", "ON", "Canada"]))
            cur.execute(insert_script("Address", ["K2OZ0P", "2", "street2", "Seattle", "WN", "USA"]))
            cur.execute(insert_script("Address", ["K2OZ0D", "3", "street3", "Bahagdad", "BG", "IQ"]))
            cur.execute(insert_script("Address", ["K2Y6Y5", "4", "street4", "Calgary", "AL", "Canada"]))
            #----------------------------------------------------------------------------------------------------------------------
            # no initial orders, will be made by users 

            #----------------------------------------------------------------------------------------------------------------------
            # create collections
            for x in range (1, 31):
                isbn = str(1234567890000 + x)
                quantity = str(random.randint(1, 20))
                cur.execute(insert_script("Collection", ["owner1", isbn, "collection1", quantity])) 
            
            for x in range (1, 31, 3): 
                isbn = str(1234567890000 + x)
                quantity = str(random.randint(1, 20))
                cur.execute(insert_script("Collection", ["owner2", isbn, "collection2", quantity])) 
            
            for x in range (3, 31, 3): 
                isbn = str(1234567890000 + x)
                quantity = str(random.randint(1, 20))
                cur.execute(insert_script("Collection", ["owner2", isbn, "collection3", quantity])) 
            #----------------------------------------------------------------------------------------------------------------------
            #create phone
            cur.execute(insert_script("Phone", ["publ1@test.ca", "1234567890"]))
            cur.execute(insert_script("Phone", ["publ1@test.ca", "1234567891"]))
            cur.execute(insert_script("Phone", ["publ2@test.ca", "1234567892"]))
            cur.execute(insert_script("Phone", ["publ3@test.ca", "1234567893"]))
            #----------------------------------------------------------------------------------------------------------------------
            #create is_author
            # add one initial author for every book 
            for x in range (1, 31):
                isbn = str(1234567890000 + x)
                fname = "authorf" + str(x) 
                lname = "authorl" + str(x) 
                cur.execute(insert_script("Is_Author", [isbn, fname, lname])) 

            for x in range (1, 6):
                # add a second author to last 5 books 
                isbn = str(1234567890000 + x)
                fname = "authorf" + str(x+25) 
                lname = "authorl" + str(x+25) 
                cur.execute(insert_script("Is_Author", [isbn, fname, lname]))

                # first 5 initial authors are also the author to the next 5 books 
                isbn = str(1234567890005 + x)
                fname = "authorf" + str(x) 
                lname = "authorl" + str(x) 
                cur.execute(insert_script("Is_Author", [isbn, fname, lname]))
            #----------------------------------------------------------------------------------------------------------------------
            #create in_genre
            for x in range(1, 31):
                isbn = str(1234567890000 + x)
                genre = "genre" + str(x%5+1) 
                cur.execute(insert_script("In_Genre", [isbn, genre])) 
                if (x%5 == 0):
                    cur.execute(insert_script("In_Genre", [isbn, "genre6"])) 
            #----------------------------------------------------------------------------------------------------------------------
            #create lives_at 
            cur.execute(insert_script("Lives_At", ["user1", "K2OW0P"]))
            cur.execute(insert_script("Lives_At", ["user2", "K2OW0P"]))
            cur.execute(insert_script("Lives_At", ["user3", "K2OZ0P"]))
            #----------------------------------------------------------------------------------------------------------------------
            #create works_at
            cur.execute(insert_script("Works_At", ["publ1@test.ca", "K2OZ0D"]))
            cur.execute(insert_script("Works_At", ["publ2@test.ca", "K2OZ0D"]))
            cur.execute(insert_script("Works_At", ["publ3@test.ca", "K2Y6Y5"]))


except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close() 