from flask import Flask, render_template, request, url_for, redirect
#import os
import psycopg2
#from flask import Flask, render_template

application = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='postgrescontainer',
                            database='flask_db',
                            user="sammy",
                            password="")
    return conn
conn = get_db_connection()
cur = conn.cursor()
# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS books;')
cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                'title varchar (150) NOT NULL,'
                                'author varchar (50) NOT NULL,'
                                'pages_num integer NOT NULL,'
                                'review text,'
                                'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                )

# Insert data into the table

cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('A Tale of Two Cities',
            'Charles Dickens',
            489,
            'A great classic!')
            )


cur.execute('INSERT INTO books (title, author, pages_num, review)'
            'VALUES (%s, %s, %s, %s)',
            ('Anna Karenina',
            'Leo Tolstoy',
            864,
            'Another great classic!')
            )

conn.commit()

cur.close()
conn.close()

@application.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM books;')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', books=books)
   

# ...

@application.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    return render_template('create.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port='5000')
