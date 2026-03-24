Digital Library Management System

Introduction
The digital library management system is a web based application system designed to manage library procedure(books,students,issue book and soon).It serves as a digital alternative to the traditional pen and paper method of recording available book , issued bookP , overdue book, in the library , aiming to improve efficiency,accuracy . Moreover, it also reduce human error and ensure secure data handling.

1.1 Problem Definition
Although the traditional manual process is functional, it has several limitations, Being paper based, it is time consuming to keep the proper record of the book, student who has accessed to the library,date of book issue , overdue, fine to pay and soon. Additionally,it is prone to human error and data loss. This causes improper and inefficient  management of the library. Even this demand more librarian .Therefore , The proposed system aim to address these challenges.

1.2  Proposed Solution
The system provides:
    • Authentication
    • Student and Book detail
    • Database Storage
	

Objective
2.1 General Objective
To design and implement a prototype digital library management system following SAD principles.

2.2 Prototype Scope
    • Analyze the requirements
    • Design database schema and system architecture
    • Implement flask backend
    • Create simple frontend interface 
    • Demonstrating adding and viewing detail
2.3 Prototype Scope
The prototype of the library management system focuses on demonstrating the core functionalities of managing library resources digitally. The prototype will simulate how user interact with the system and how book records are managed.
The prototype include following prototype:
a. User Authentication
    • User login system
    • Librarian access
    • Basic authentication to access the system dashboard
b. Book Management
    • Add new book
    • View list of book
    • Update book information
    • Delete book record
c. Book Search
d. Issue Book Module
e. Return Book Module
f. Book availability Display





3.System Analysis Phase
3.1 Functional Requirements
The system provide the following functional capabilities
    • User signup
    • User login
    • Add new books
    • Add new students
    • Issue book
    • Return book
    • View Reports
    • View Overdue Books
    • View Issued Books
    • Search Student ID
    • Student History
    • Book Detail
    • Student Detail
3.2 Non-Functional Requirements
    • Performance : The system should provide fast response time for login , posting and data retrieval operations.
    • Usability: The system should offer a simple and user-friendly interface suitable for user
    • Security: The system should ensure secure user authentication and restrict access to authorized users only.
    • Accessibility: The system should be web-based and accessible across common devices and browsers.
4. System Design
4.1 Architecture Overview
The system follows a 3-tier architecture:

Tier	Stack
Frontend	HTML,CSS
Backend	Flask
Database	Sqlite
0 : Browser Flask – SQLite Database
0
4.2 Use Case Diagram





4.3 Data Flow Diagram
4.3.1 DFD 0





4.3.2 DFD 1




4.3.3  DFD 2



4.4 Class Diagram
















4.5 Sequence Diagram





4.6 Physical Entity Relationship (ER) Diagram












4.7 API Design

Endpoint	Method	Input 	Output
/signin	GET/POST	Email,password	Login and page redirect
/signup	GET/POST	Name,email,password	Register new users/
/n	GET		Redirect to home page
/add_book	GET/POST	book_id,book_name,no.of copies	Add new book
/add_student	GET/POST	Student name, student id, student email,phone number	Add new student 
/issue_book	GET/POST	Student id,book id,issued date,due date	Added issued date and overdue date
/return_book	GET/POST	Student id,book id	Update report
/report	GET		View book report
/overdue	GET		View overdue book
/report_issued_book	GET		View currently issued book
/student_input	GET/POST	Student id	View student Report
/book_detail	GET		View book detail
/student_detail	GET		View student detail




5.Implementation
5.1 Backend
The backend of the system is implemented using python with FLASK Framework and Sqlite database is used. Flask is a lightweight web framework that allows developers to build web applications quickly and efficiently. It follows a simple structure and provides flexibility in designing the application.

For the prototype, an SQLite database is used. This lightweight, file-based database is sufficient for development and testing, eliminating the need for a full-scale database server like PostgreSQL. The database schema is simple, with clearly defined tables to store user information, attendance records, and other necessary data.

The backend of the library management system is responsible for handling business logic,processing user requests, managing interaction with database.This architecture ensures that the backend is efficient, reliable, and easy to maintain, while providing all the necessary functionality for the prototype system.










