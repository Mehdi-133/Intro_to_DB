import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="JAN123456-"  # Replace with your actual MySQL password
        )

        if connection.is_connected():
            # Create a cursor to execute SQL statements
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error: {"except mysql.connector.Error"}")

    finally:
        # Ensure the cursor and connection are closed properly
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Run the function to create the database
create_database()
