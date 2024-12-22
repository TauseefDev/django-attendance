#Attendance Tracker
##Video Demo: [URL HERE]

###Description
This project is a Django-based Attendance Tracker designed to simplify and enhance attendance management for educational institutions. The system allows administrators to record attendance, store it in a centralized database, and notify students about their attendance status. The integration of email notifications makes it a comprehensive solution for managing student attendance effectively.

Key Features
User-Friendly Interface:

Select attendance dates using a date picker.
View the list of students and mark their attendance conveniently.
Custom Attendance Categories:

Attendance statuses include "Present," "Absent," "Non-Maths," and "Halfday."
Automated Email Notifications:

Students marked as "Absent" receive an email alert.
Centralized Record Keeping:

Attendance records are stored in a database and can be managed via Django’s admin panel.
Responsive Design:

Utilizes Bootstrap for a clean and mobile-friendly user interface.
How It Works
Attendance Submission
The administrator accesses the Attendance Page via the application.

Steps include:

Selecting the attendance date.
Viewing a dynamically generated table of students.
Selecting the appropriate attendance status for each student from a dropdown menu.
Upon submission:

Attendance records are saved to the database.
Students marked "Absent" receive an automated email notification.
Email Notification
Content:

The email contains the student’s name, the selected attendance date, and a message encouraging them to contact the administration if the attendance is incorrect.
Integration:

Configured via Django's built-in email framework, using an SMTP email service for secure delivery.
Admin Panel Access
View, edit, and manage attendance records for students.
Records include the attendance date and attendance status for every student.
Technologies Used
Backend
Django Framework: Python-based framework for robust and scalable web development.
SQLite: Database used for local development.
Frontend
HTML and CSS: For the basic structure and styling of the attendance page.
Bootstrap: For responsive and modern UI design.
Email Integration
Django’s Email Framework: Configured with SMTP for sending automated email alerts.
Version Control
Git: For version control.
GitHub: For repository hosting and collaboration.
