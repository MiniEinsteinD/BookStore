# BookStore
COMP 3005 class project

We chose to use Python & psycopg2 module in order to create our BookStore Application. It is a command-line application that consists of 2 different main scripts: 
        User_Interface
        Owner_Interface

Each script is responsible for the functionality of the BookStore App. The database changes according to both scripts. 

First, create the db in pgAdmin with the name of 'BookStore'.
In order to run the script, you need to download the BookStore>code file. 
Please go to 'pgsql_credentials.py' and change the credentials required in order to build the connection with the db sql server.
After, please go to 'init_reltions.py' and run the script to populate the db with dummy values.
Finally, run the desired scrpit (user_interface or owner_interface) and follow the command-line instructions.

A demo of what the user/owner interface is added to the documantation. Please take a look at it for further help.

Note: You can not create an owner, so please look at the init_relations to find an owner username and password or run the tables in pgadmin to get the username and password of one of the owners.


Authors:
JiaQi Han (101140762)
Daniah Mohammed (101145902)

