import sqlite3


def initialize_database():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Create a sample table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    # Insert sample data
    cursor.execute('''
        INSERT INTO users (name, age) VALUES
        ('Alice', 30),
        ('Bob', 25)
    ''')

    connection.commit()
    connection.close()


def main():
    initialize_database()

    #
    print("Database initialized and sample data inserted.")


if __name__ == "__main__":
    main()
