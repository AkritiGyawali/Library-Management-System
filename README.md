# Digital Library Management System

## Introduction
The digital library management system is a web based application system designed to manage library procedure(books,students,issue book and soon).It serves as a digital alternative to the traditional pen and paper method of recording available book , issued bookP , overdue book, in the library , aiming to improve efficiency,accuracy . Moreover, it also reduce human error and ensure secure data handling.

### 1.1 Problem Definition
Although the traditional manual process is functional, it has several limitations, Being paper based, it is time consuming to keep the proper record of the book, student who has accessed to the library,date of book issue , overdue, fine to pay and soon. Additionally,it is prone to human error and data loss. This causes improper and inefficient  management of the library. Even this demand more librarian .Therefore , The proposed system aim to address these challenges.

### 1.2  Proposed Solution
The system provides:
    • Authentication
    • Student and Book detail
    • Database Storage
	

## Objective
### 2.1 General Objective
To design and implement a prototype digital library management system following SAD principles.

### 2.2 Prototype Scope
    • Analyze the requirements
    • Design database schema and system architecture
    • Implement flask backend
    • Create simple frontend interface 
    • Demonstrating adding and viewing detail
### 2.3 Prototype Scope
The prototype of the library management system focuses on demonstrating the core functionalities of managing library resources digitally. The prototype will simulate how user interact with the system and how book records are managed.
The prototype include following prototype:
#### a. User Authentication
    • User login system
    • Librarian access
    • Basic authentication to access the system dashboard
#### b. Book Management
    • Add new book
    • View list of book
    • Update book information
    • Delete book record
#### c. Book Search
#### d. Issue Book Module
#### e. Return Book Module
#### f. Book availability Display





## 3.System Analysis Phase
### 3.1 Functional Requirements

The system provide the following functional capabilities<br>

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
### 3.2 Non-Functional Requirements

    • Performance : The system should provide fast response time for login , posting and data retrieval operations.
    • Usability: The system should offer a simple and user-friendly interface suitable for user
    • Security: The system should ensure secure user authentication and restrict access to authorized users only.
    • Accessibility: The system should be web-based and accessible across common devices and browsers.
## 4. System Design
### 4.1 Architecture Overview
The system follows a 3-tier architecture:

| Tier    |	Stack |
|:--------:|:------:|
| Frontend |	HTML,CSS |
| Backend	| Flask |
|Database |	Sqlite |



## 4.2 Use Case Diagram


![alt text](<img/Screenshot from 2026-03-14 17-28-20.png>)


## 4.3 Data Flow Diagram
### 4.3.1 DFD 0


![alt text](<img/Screenshot from 2026-03-16 15-40-31.png>)


### 4.3.2 DFD 1

![alt text](<img/Screenshot from 2026-03-16 15-50-03.png>)


### 4.3.3  DFD 2

![alt text](<img/Screenshot from 2026-03-16 15-53-05.png>)

## 4.4 Class Diagram




![alt text](<img/Screenshot from 2026-03-14 18-22-53.png>)











## 4.5 Sequence Diagram

![alt text](<img/Screenshot from 2026-03-16 16-45-26.png>)



## 4.6 Physical Entity Relationship (ER) Diagram



![alt text](<img/Screenshot from 2026-03-16 17-15-02.png>)








## 4.7 API Design

| Endpoint |	Method	| Input |	Output |
|:---------:|:-----------:|:------:|:--------:|
|/signin	|GET/POST|	Email,password|	Login and page redirect|
|/signup|	GET/POST|	Name,email,password	|Register new users/|
|/n	GET	|      |	Redirect to home page|
|/add_book	|GET/POST|	book_id,book_name,no.of copies|	Add new book|
|/add_student|	GET/POST|	Student name, student id, student email,phone number|	Add new student |
|/issue_book|	GET/POST	|Student id,book id,issued date,due date|	Added issued date and overdue date|
|/return_book|	GET/POST|	Student id,book id|	Update report|
|/report|	GET	|   |	View book report|
|/overdue	|GET|		|View overdue book|
|/report_issued_book|	GET	|  |	View currently issued book|
|/student_input	|GET/POST|	Student id	|View student Report|
|/book_detail|	GET|   |		View book detail|
|/student_detail|	GET	|  |	View student detail|




## 5.Implementation
### 5.1 Backend
The backend of the system is implemented using python with FLASK Framework and Sqlite database is used. Flask is a lightweight web framework that allows developers to build web applications quickly and efficiently. It follows a simple structure and provides flexibility in designing the application.

For the prototype, an SQLite database is used. This lightweight, file-based database is sufficient for development and testing, eliminating the need for a full-scale database server like PostgreSQL. The database schema is simple, with clearly defined tables to store user information, attendance records, and other necessary data.

The backend of the library management system is responsible for handling business logic,processing user requests, managing interaction with database.This architecture ensures that the backend is efficient, reliable, and easy to maintain, while providing all the necessary functionality for the prototype system.


## 5.2 Frontend
The frontend of the system is designed to provide an intuitive and user-friendly interface for users.
It is web-based, ensuring accessibility across devices and browsers. The interface is organized
based on user roles, with separate views for teachers and students.
#### User Interface:
The user interface provides all the tools required to manage library system. The frontend is
designed with simplicity in mind, ensuring that the user can interact with the system efficiently
without extensive training. The combination of dynamic table and role-based dashboard ensures
usability , clarity and quick access to information about library.
#### Login Page

All users must log in before accessing the system:

• Email/Password Input: Users enter their credentials to authenticate.<br>
• Role-Based Redirect: After login, users are redirected to the home page.
## 6. Testing

The system underwent functional testing to ensure that all core features operate correctly and
reliably. The following aspect were tested:

#### Login Interface:

•Verified that the login page is accessible<br>
•Verified that the username and password fields are present<br>
•Checked that the login page is present<br>
•Tested that the user can successfully login with valid credentials<br>
•verified that error message is displayed for invalid login attempts<br>
•Tested that the signup link is functional<br>
•Tested that the user can successfully register the account<br>
•Tested that the system redirect to login page after successful registration<br>
•Tested that the system redirects to the appropriate page after successful login<br>
•Verified that the system displays appropriate error message for missing credentials<br>
#### User Interface

•Tested that the authenticated user can add book detail, student detail<br>
•Verified that user can issue book and return book<br>
•Verified that the user can view the student detail, book detail and student history<br>
Verified that the system redirects to the appropriate page after successful logout<br>
#### Data Integrity :

•Ensured that all the records are displayed correctly and matched the backend records<br>
•Tested that the duplicate or conflicting entries are prevented by database constraints<br>
This testing phase confirms that the system meets the functional requirements and the user can
efficiently interact with the system.
## 7. Limitation
While the prototype demonstrate the core functionality of the library management system, it has
several limitations:

***•Limited Security Features:*** The system currently implements only basic authentication
mechanism. Advanced security features such as multi-factor authentication, role-based
access control and date encryption are not fully implemented which may cause potential
security risks.<br><br>
***•Lack of advanced search functionality:*** The system currently provide simple search
options such as searching book by book id and student by student id. Advanced searching
like filtering by category, author are not available<br><br>
***•Database limitation :*** Sqlite is used for simplicity , but it is not suitable for large scale ,
production -ready deployments.<br><br>
***•User Interface :*** The frontend has basic styling and lack advanced design or
responsiveness<br><br>
## 8. Future Enhancements
Several improvements can be implemented in the future to enhance functionality, security and
usability.

***• JWT Authentication:*** Implement JSON Web Tokens for secure and persistent user
sessions.<br><br>
***• Password Encryption:*** Store passwords securely using hashing algorithms to protect user
credentials.<br><br>
***• Mobile-Responsive UI:*** Enhance the frontend to be fully responsive, ensuring usability
across desktops, tablets, and mobile devices.<br><br>
***• Email/SMS Notifications:*** Introduce automated notifications to alert students about
attendance updates or reminders.<br><br>
These enhancements will make the system more secure, scalable, and user-friendly, bringing it
closer to a production-ready solution.
## 9. Conclusion
This prototype system successfully demonstrates the practical application of System Analysis and
Design (SAD) principles in developing an library management system.

***• Analysis:*** The inefficiencies and limitations of the manual process were identified,
highlighting the need for automation.<br><br>
***• Design:*** A clear database schema was created and a corresponding frontend interface to
meet user requirements.<br><br>
***• Implementation:*** A functional backend using FLASK and a simple web-based frontend
were developed, providing core features such as login,adding and issuing and summary
views.<br><br>
The system is scalable, user-friendly, and efficient, serving as a demonstration prototype for
classroom attendance management. While it has certain limitations in security, UI, it provides a
solid foundation for future enhancements and a practical example of SAD principles applied in a
real-world scenario.







