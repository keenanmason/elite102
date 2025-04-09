import sqlite3

DB_NAME = 'example.db'


def initialize_database():
    connection = sqlite3.connect(DB_NAME)
    print("Connected to the database.")
    cursor = connection.cursor()
    print("Cursor created.")
    # Create a sample table
    print("Creating table if it does not exist...")
    cursor.execute('''
        CREATE TABLE user
            (id integer primary key, 
            first_name text,
            last_name text,
            email text,
            phone_number text)

    ''')

    print("Table created.")

    # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO user (first_name,last_name, email, phone_number) VALUES
        ('Alice', 'john, 'alice@test.com', '555-555-555'),
        ('Bob', james, 'bob@test.com', '333-333-3333'),
        ('Charlie', brown, 'charlie@test.com', 222-222-2222)
    ''')
    print("Sample data inserted.")
    # Commit the changes and close the connection
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()


initialize_database()
