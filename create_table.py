import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
print("Opened database successfully")

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Perform database operations here
conn.execute('DROP TABLE IF EXISTS users')
conn.execute('CREATE TABLE users (name TEXT, id INTEGER PRIMARY KEY, points INTEGER)')
print("Table created successfully")

# Insert data into the table
conn.execute("INSERT INTO users (name, id, points) VALUES ('Steve Smith', 211, 80), ('Jian Wong', 122, 92), ('Chris Peterson', 213, 91), ('Sai Patel', 524, 94), ('Andrew Whitehead', 425, 99), ('Lynn Roberts', 626, 90), ('Robert Sanders', 287, 75)")
conn.commit()
print("Data inserted successfully")

# Close the connection
conn.close()