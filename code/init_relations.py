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

            # creating dummy values - init the tables with those values
            #-----------------------------------------------------------
            
            # create users
            #cur.execute(insert_script("Users", ["user1", "Ahmed", "Elroby", "12345"]))
            cur.execute(insert_script("Users", ["user2", "Moe", "Za", "54321"]))
            cur.execute(insert_script("Users", ["user3", "Dani", "Mo", "12345D"]))
            #----------------------------------------------------------------------------------------------------------------------
            # create owner
            #cur.execute(insert_script("Owner", ["owner1", "Ali", "Alex", "54321", "500"] ))
            #----------------------------------------------------------------------------------------------------------------------
            # create publishers
            cur.execute(insert_script("Publisher", ["publ1@test.ca", "Bob", "Ta", "54321t", "500"]))
            cur.execute(insert_script("Publisher", ["publ2@test.ca", "John", "Fa", "54321t", "450"]))
            cur.execute(insert_script("Publisher", ["publ3@test.ca", "Tash", "Feen", "54321t", "550"]))
            # create books
            cur.execute(insert_script("Book", ["1234567891234", "Lord of the Flies", "300", "100", "0.1", "publ1@test.ca"]))
            cur.execute(insert_script("Book", ["1234567891224", "Lord of the Rings", "340", "105", "0.2", "publ2@test.ca"]))
            cur.execute(insert_script("Book", ["1134567891234", "The Day We Met", "200", "50", "0.3", "publ3@test.ca"]))
            #----------------------------------------------------------------------------------------------------------------------
            # create address
            cur.execute(insert_script("Address", ["K2OW0P", "1", "street1", "Ottawa", "ON", "Canada"]))
            cur.execute(insert_script("Address", ["K2OZ0P", "2", "street2", "Seattle", "WN", "USA"]))
            cur.execute(insert_script("Address", ["K2OZ0D", "3", "street3", "Bahagdad", "BG", "IQ"]))
            #----------------------------------------------------------------------------------------------------------------------
            # create banks for users
            cur.execute(insert_script("Bank", ["123456789", "12345", "500"]))
            cur.execute(insert_script("Bank", ["987654321", "54321", "1000"]))
            cur.execute(insert_script("Bank", ["123451234", "56789", "50"]))

            #----------------------------------------------------------------------------------------------------------------------
            # create orders


            #----------------------------------------------------------------------------------------------------------------------
            # create collections

            #create phone for publisher

            #create is_author

            #create is_genre

            #create in_order

            #create lives_at 

            #create works at

            #create user_banking

            cur.execute('SELECT * FROM users')
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