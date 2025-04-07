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
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    print("Table created.")

    # Insert sample data
    print("Inserting sample data...")
    cursor.execute('''
        INSERT INTO users (name, age) VALUES
        ('Alice', 30),
        ('Bob', 25)
    ''')
    print("Sample data inserted.")
    # Commit the changes and close the connection
    print("Committing changes and closing the connection...")
    connection.commit()
    connection.close()


initialize_database()
