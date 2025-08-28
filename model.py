import psycopg2
from psycopg2 import Error

connection = None  # Initialize the connection variable

try:
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",  # PostgreSQL username
        password="Salam316!@",  # PostgreSQL password
        database="postgres"  # PostgreSQL database name
    )

    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM songs_list")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if connection:
        cursor.close()  # Close the cursor
        connection.close()  # Close the connection
        print("PostgreSQL connection is closed")