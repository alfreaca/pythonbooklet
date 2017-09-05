import sqlite3
print ("Exercise 3\n")
new_db = sqlite3.connect("D:\Documents - Data Drive\Homework\Python Booklet\Library.db")
c = new_db.cursor()
c.execute('''CREATE TABLE Books
(book_isbn text,
book_title text,
book_type text,
book_author text,
publisher text)
''')

c.execute('''INSERT INTO Books
          VALUES ('978-0-340-88851-3', 'A2 Pure Mathematics', 'Non fictional', 'Catherine Berry', 'Hodder Education')''')
c.execute('''INSERT INTO Books
          VALUES ('978-1-118-10227-5', 'Android 4 Application Development', 'Non fictional', 'Reto Meier', 'Wiley')''')
c.execute('''INSERT INTO Books
          VALUES ('0-596-00699-3', 'Programming C#', 'Non fictional', 'Jesse Liberty', 'O Reilly')''')
new_db.commit()
new_db.close()

new_db = sqlite3.connect("D:\Documents - Data Drive\Homework\Python Booklet\Library.db")
c = new_db.cursor()
c.execute('''SELECT * FROM Books
''')

book_library = c.fetchone()
for book in (book_library):
    print (book)
print ("\n")

book_library = c.fetchone()
for book in (book_library):
    print (book)
print ("\n")

book_library = c.fetchone()
for book in (book_library):
    print (book)
print ("\n")

new_db.close()
