from flask import Flask, render_template,request,redirect,session# session i the short term memory that store logged in user's detail
import os
import sqlite3
from datetime import date
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key =os.getenv("Secret_key")  # Load secret key from .env file

DB_PATH = os.path.join(os.path.dirname(__file__), "library.db")


def initialize_schema(conn):
    conn.executescript(
        """
        PRAGMA foreign_keys = ON;
        CREATE TABLE IF NOT EXISTS book (
            book_name TEXT,
            book_id INTEGER PRIMARY KEY,
            no_of_book INTEGER
        );
        CREATE TABLE IF NOT EXISTS login (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS student (
            student_name TEXT,
            student_id INTEGER PRIMARY KEY,
            email TEXT,
            phone_number TEXT
        );
        CREATE TABLE IF NOT EXISTS book_issued (
            student_id INTEGER,
            book_id INTEGER,
            issued_date TEXT,
            due_date TEXT,
            return_date TEXT,
            FOREIGN KEY (student_id) REFERENCES student(student_id),
            FOREIGN KEY (book_id) REFERENCES book(book_id)
        );
        """
    )
    conn.commit()


def get_sqlite_connection():
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.execute("PRAGMA foreign_keys = ON")
    initialize_schema(conn)
    return conn


mydb = get_sqlite_connection()

mycursor=mydb.cursor()
@app.route("/")
def home():
    return render_template("signin.html")
@app.route("/n")
def home_page():
    if 'username' not in session:
        return redirect('/signin')
    
    return render_template("library.html")
@app.route("/signin",methods=['POST','GET'])
def signin():
    if request.method=='POST':
        name=request.form['username']
        pword=request.form['password']
        mycursor.execute("select * from login where username=? and password=?",(name,pword))
       
        
        user=mycursor.fetchone()
        
        if user :
            session['username'] = name
            session['password'] = pword
            print("login successful")
            
            return redirect("/n")
        else:
            print("invalid username or password")
            return render_template('signin.html', error ="Invalid username or password")
    return render_template("signin.html")
    

@app.route("/signup",methods=['POST','GET'])
def signup():
    if request.method=='POST':
        name=request.form['username']
        passw=request.form['password']
        confirm_password=request.form['confirm_password']
        if passw!=confirm_password:
            return render_template('signup.html',error="password didn't match")
        mycursor.execute("select * from login where username=?",(name,))
        user=mycursor.fetchone()
        if user:
            return render_template('signup.html',error="username already exist")
        mycursor.execute("insert into login(username,password)values(?,?)",(name,passw))
        mydb.commit()
        return redirect('/signin')
    return render_template('/signup.html')


@app.route("/add_book",methods=['POST','GET'])
def add_book():
    if 'username'not in session:
        return redirect('/signin')
    if request.method=='POST':
        name=request.form['book_name']
        id=request.form['book_id']
        stock=request.form['no_of_book']
        mycursor.execute("insert into book (book_name,book_id,no_of_book) values(?,?,?)",(name,id,stock))
        
        mydb.commit()
        return redirect('/n')
    return render_template("add_book.html")

@app.route("/add_student",methods=['POST','GET'])
def add_student():
    if 'username'not in session:
        return redirect('/signin')
    if request.method=='POST':
        name=request.form['student_name']
        id=request.form['student_id']
        email=request.form['email']
        phone=request.form['phone_number']
        # Check if the student already exists
        mycursor.execute("insert into student(student_name,student_id,email,phone_number) values (?,?,?,?)   ",(name,id,email,phone))
        
        mydb.commit()
        return redirect("/n")
    return render_template("add_student.html")

@app.route("/issue_book",methods=['POST','GET'])
def issue_book():
    if 'username'not in session:
        return redirect('/signin')
    if request.method=='POST':
        id_of_book=request.form.get("book_id")
        id_student=request.form.get("student_id")
        date_of_issue=request.form.get("issue_date")
        date_of_due=request.form.get("due_date")
        date_of_return=request.form.get("return_date",None)
        mycursor.execute("select no_of_book from book where book_id=?",(id_of_book,))
       
        book=mycursor.fetchone()
        

        if book and book[0]>0:
            mycursor.execute("insert into book_issued(book_id,student_id,issued_date,due_date,return_date) values(?,?,?,?,?)",(id_of_book, id_student, date_of_issue, date_of_due, date_of_return))
            
            mydb.commit()
            
            
            mycursor.execute("update book set no_of_book=no_of_book-1 where book_id=?",(id_of_book,))
            
            mydb.commit()
            return("book issued sucessfully!")
        else:
            return("book not available") 
    return render_template("issued_book.html",today=date.today())   
@app.route("/return_book",methods=['POST','GET'])
def return_book():
    if request.method=='POST':
        bookid=request.form.get('book_id')
        studentid=request.form.get('student_id')
        mycursor.execute("""update book_issued set return_date=?
        where student_id=? and book_id=? and return_date IS NULL""",(date.today(),studentid,bookid))
       
        
        mydb.commit()
        
        mycursor.execute("update book set no_of_book=no_of_book+1 where book_id=?",(bookid,))
        
        mydb.commit()
        return("book return successfoollyy")
    
    return render_template('return_book.html')

@app.route('/report')
def view_book():
    if 'username'not in session:
        return redirect('/signin')
    mycursor.execute("""
        SELECT 
            s.student_id, 
            s.student_name, 
            b.book_id, 
            b.book_name,
            i.issued_date, 
            i.due_date, 
            i.return_date 
        FROM book_issued i
        INNER JOIN student s ON i.student_id = s.student_id
        INNER JOIN book b ON i.book_id = b.book_id
    """)
    records = mycursor.fetchall()
    return render_template('report.html', records=records)
@app.route('/overdue')
def overdue_books():
    if 'username'not in session:
        return redirect('/signin')
    mycursor.execute("""
        SELECT
            s.student_id, 
            s.student_name, 
            b.book_id, 
            b.book_name, 
            i.issued_date, 
            i.due_date 
        FROM book_issued i
        INNER JOIN student s ON i.student_id=s.student_id
        INNER JOIN book b ON i.book_id=b.book_id
        WHERE i.return_date IS NULL AND i.due_date < date('now')
    """)
    records=mycursor.fetchall()
    return render_template('overdue_books.html',records=records)

@app.route('/report_issued_book')
def report_book():
    if 'username'not in session:
        return redirect('/signin')
    mycursor.execute("""
        SELECT
        b.book_name,count(*) as issued_book
        FROM book_issued i
        INNER JOIN book b ON i.booK_id=b.book_id
        WHERE i.return_date IS NULL
        GROUP BY b.book_id;
    """)
    records =mycursor.fetchall()
    return render_template('report_issued_books.html', records=records)
@app.route('/student_input')
def report_student():
    return render_template('student_input.html')

@app.route('/student_report',methods=['GET', 'POST'])
def student_report():
    if 'username'not in session:
        return redirect('/signin')
    student_id = request.values.get('student_id')
    if not student_id:
        return redirect('/student_input')
    mycursor.execute("""
        SELECT
        * FROM
        book_issued i 
        WHERE student_id=?""",(student_id,))
    records= mycursor.fetchall()
    return render_template('student_history.html',records=records,student_id=student_id) 

@app.route('/book_detail')
def book_detail():
    if 'username'not in session:
        return redirect('/signin')
    mycursor.execute("""
            SELECT 
                       
                b.book_name, 
                b.book_id, 
                b.no_of_book AS available_books,
                COALESCE(count_issued.total_issued, 0) AS total_issued,
                b.no_of_book + COALESCE(count_issued.total_issued, 0) AS total_books
        FROM book b
        LEFT JOIN (
            SELECT 
                book_id, COUNT(*) AS total_issued
            FROM book_issued
            WHERE return_date IS NULL
            GROUP BY book_id
        ) AS count_issued ON b.book_id = count_issued.book_id""")
        
    records = mycursor.fetchall()
   
    
    return render_template('book_detail.html', records=records, )   
                     
@app.route('/student_detail')
def student_detail():
    if 'username'not in session:
        return redirect('/signin')
    mycursor.execute("SELECT * FROM student")
    records = mycursor.fetchall()
    return render_template('student_detail.html', records=records)   
                                       
@app.route('/logout')
def logout():
    session.pop('username',None)
    session.pop('password',None)
    return redirect('/signin')


if __name__ == '__main__':
    app.run(debug=True)
