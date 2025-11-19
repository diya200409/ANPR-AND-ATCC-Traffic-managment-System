import pymysql

# Connect to MySQL database
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='123456789',
    database='Store',
    port=3307
)

print("Database connection successful!")

try:
    with connection.cursor() as cursor:
        # 1. INSERT data
        insert_query = "INSERT INTO books(book_id, book_name, price) VALUES (%s, %s, %s)"
        values = (1, "R.D Sharma", 499.99)
        cursor.execute(insert_query, values)

        values = (2, "Oswal", 399.99)
        cursor.execute(insert_query, values)

        values = (3, "Tec Knowledge", 299.99)
        cursor.execute(insert_query, values)

        values = (4, "Anabell", 199.99)
        cursor.execute(insert_query, values)

        connection.commit()
        print("\nBooks inserted successfully!")

        # 2. READ data
        select_query = "SELECT * FROM books"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        print("\nBooks list:")
        for row in rows:
            print(row)

        # 3. UPDATE data
        update_query = "UPDATE books SET price=%s WHERE book_id=%s"
        cursor.execute(update_query, (450.00, 1))
        connection.commit()
        print("\nBook price updated!")

        # 4. READ again to verify update
        cursor.execute(select_query)
        rows = cursor.fetchall()
        print("\nBooks list after update:")
        for row in rows:
            print(row)

        # 5. DELETE data
        delete_query = "DELETE FROM books WHERE book_id=%s"
        cursor.execute(delete_query, (1,))
        connection.commit()
        print("\nBook record deleted!")

finally:
    connection.close()
    print("\nDatabase connection closed.")
