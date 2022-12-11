# Author: Daniah Mohammed and JiaQi Han 
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
                cur.execute(insert_script("Collection", ["owner2", isbn, "collection1", quantity])) 
            
            for x in range (3, 31, 3): 
                isbn = str(1234567890000 + x)
                quantity = str(random.randint(1, 20))
                cur.execute(insert_script("Collection", ["owner2", isbn, "collection2", quantity])) 
            #----------------------------------------------------------------------------------------------------------------------
            #create phone for publisher
            
            #----------------------------------------------------------------------------------------------------------------------
            #create is_author

            #----------------------------------------------------------------------------------------------------------------------
            #create is_genre
            
            #----------------------------------------------------------------------------------------------------------------------
            #create in_order

            #----------------------------------------------------------------------------------------------------------------------
            #create lives_at 
            
            #----------------------------------------------------------------------------------------------------------------------
            #create works at

            #----------------------------------------------------------------------------------------------------------------------
            #create user_banking

            cur.execute('SELECT * FROM book')
            for record in cur.fetchall():
                print(record)
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close() 


'''insert_script2  = "INSERT INTO Book (ISBN, name, page_num, price, publisher_percentage, publisher) VALUES (%s, %s, %d, %d, %d, %s) "
            insert_values = [('1234567890ss123', 'test', 10, 12.5, 0.1, 'test.com')]
            for record in insert_values:
                 cur.execute(insert_script, record)
            #'''