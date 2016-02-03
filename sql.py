# MODEL

# spl.py - Create a SQLITE3 table and populate it with data

import sqlite3

# Create a new database if the database doesn't already exist
with sqlite3.connect("blog.db") as connection:
	
	# get a cursor used to execute SQL commands
	c = connection.cursor()
	
	# Create the table
	c.execute("""CREATE TABLE posts
				(title TEXT, post TEXT)
				""")
				
	# Insert dummy data into the table
	c.execute('INSERT INTO posts VALUES("Good", "I\'m good.")')
	c.execute('INSERT INTO posts VALUES("Well", "I\'m well.")')
	c.execute('INSERT INTO posts VALUES("Great", "I\'m great.")')
	c.execute('INSERT INTO posts VALUES("Okay", "I\'m Okay.")')
	
				
