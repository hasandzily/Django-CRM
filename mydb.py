import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='m1h2s3'
    )

    if connection.is_connected():
        print("Connected to MySQL server")

        # Prepare a cursor object
        cursor = connection.cursor()

        # Create a new database
        cursor.execute("CREATE DATABASE crmproject")
        print("Database 'crmproject' created successfully")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")