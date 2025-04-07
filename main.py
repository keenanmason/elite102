import sqlite3


def main():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()

    # Create a sample table
    results = cursor.execute('''
        SELECT id, name, age, grade, gpa FROM students
    ''')

    print("Results:")
    for row in results:
        print(row)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    main()
