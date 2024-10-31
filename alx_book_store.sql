import mysql.connector

alx_book_store = mysql.connector.connect(
    host="localhost",
    user="root",
    password="JAN123456-",
    database="alx_book_store"
)

print(alx_book_store.get_server_info())