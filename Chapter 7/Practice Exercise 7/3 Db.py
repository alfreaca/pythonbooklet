import sqlite3

new_db = sqlite3.connect('C:')

c=new_db.cusor()

c.execute('''CREATE TABLE Books
(book_isbn text,
book_title text,
book_type text,
book_author text,
publisher text)
''')

new_db.commit('''INSERT INTO Books
    VALUES ('978-0-340-8885103', 'A2 Pure Mathematics', 'Non fictional', 'Catherine Berry', 'Hodder Education')
    VALUES ('978-1-118-10227-5', 'Android 4 Application Development', 'Non fictional', 'Reto Meier', 'Wiley')
    VALUES ('0-596-00699-3', 'Programming C#', 'Non fictional', 'Jesse Liberty', 'O Reily')
''')
new_db.close()

new_db=sqlite3.connect('C:')

c=new_db.cursor()

book_library=c.fetchall()

for book in book_library:
    print(book)


new_db.close()
