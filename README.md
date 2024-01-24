# BookStore

Welcome to the BookStore application, a project developed for the COMP 3005 class. This command-line application is built using Python and the psycopg2 module. The application consists of two main scripts:

1. **User_Interface**
2. **Owner_Interface**

Each script is responsible for specific functionalities within the BookStore application, and the database undergoes changes based on the actions performed by these scripts.

## Getting Started

To set up and run the BookStore application, follow these steps:

1. **Create Database:** In pgAdmin, create a database named 'BookStore'.
2. **Download Code:** Download the 'BookStore' code file.
3. **Configure Database Connection:** Open 'pgsql_credentials.py' and update the credentials to establish a connection with the SQL server.
4. **Initialize Database:** Run 'init_relations.py' to populate the database with dummy values.
5. **Run Application:** Execute the desired script (`user_interface` or `owner_interface`) and follow the command-line instructions.

## Demo

Refer to the documentation for a detailed demo of the user and owner interfaces to assist you further in using the BookStore application.

## Note

- **Owner Credentials:** You cannot create an owner directly. Refer to 'init_relations.py' to find an existing owner's username and password. Alternatively, check the pgAdmin tables to retrieve the username and password of one of the owners.

## Authors

- **JiaQi Han (101140762)**
- **Daniah Mohammed (101145902)**

