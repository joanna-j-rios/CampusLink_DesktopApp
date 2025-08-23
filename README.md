# CampusLink_DesktopApp

Project Title: CampusLink Desktop App


Project Description

CampusLink is a desktop application built using Python and Tkinter, designed to serve as a centralized hub for university students. The application aims to simplify a student’s academic and social life by providing a single platform to manage schedules, discover events, stay informed through a community bulletin board, and access critical emergency contacts.


Key Features

	User Authentication & Account Management: A secure system to create unique accounts, log in, and log out and a space for displaying user information and managing sessions.

	Activities & Task Schedule Manager: A user friendly interface to add, view, and edit a weekly schedule of classes, appointments, and personal tasks.
 
	Bulletin Board: A dedicated section for Browse and posting announcements relevant to the campus community, including news, queries, and student led activities/initiatives.
 
	Emergency Contacts: A quick access panel with essential campus services like security, health, and counseling.


Development Methodology

This project is being developed using an agile methodology with an emphasis on iterative development, continuous feedback, testing, and collaboration through version control. Useid Tkinter and sqlite3 database.


Basic Usage Instructions

To get a local copy of this project up and running on your machine, follow these simple steps.

Prerequisites 

	Python 3.x installed on your system
	git command line tool

Installation

	For collaborators: Clone this repository directly.
	For public users: First, fork this repository to your own Github account, then clone your fork.
 
		git clone [repository-URL]
  
	Navigate to the project directory:
 
		cd [repository-name]
  
	Create and activate a virtual environment to manage project dependencies
 
		python -m venv virt
		Source virt/bin/activate
  
	Run the application
 
		python main.py



Agile Planning


Team members and Roles

	Joanna Rios - Technical Lead, Code Reviewer (& Tester), & System Architect
	
	Responsibilities: Drives the technical vision, sets up the Git/GitHub repository and development environment, designs the overall software architecture, creates UML diagrams, and ensures code quality. The “swiss army knife” responsible for the technical documentation and ensuring deadlines are met.

 
	Alicia Cortina - UI/UX Prototyper & Feature Developer
	
	Responsibilities: Focuses on the user interface design (Tkinter layouts, widgets, user flow), implements specific features like the "Activities/Task Schedule Manager" and "Bulletin Board," ensuring a good user experience.

 
	Emma Pacheco - Contact Information Specialist
	
	Responsibilities: Meant to focus on displaying information for emergency contacts information.



Sprint Schedule
 
Sprint 1

	Start Date: July 24
	End Date: July 30
	Activities: 
		Set up a repository (and any other channels of communication Google Docs, Discord, Whatsapp, etc.)
		Define features (user stories)
		Draft documentation (User Manual - README & Technical Doc.)

Sprint 2

	Start Date: July 31
	End Date: August 6
	Activities: 
 		Core UI Setup- Implement the main Tkinter application window
		Navigation- Setup the primary navigation structure to switch between sections
		Log In/ Create Account: Get the login and account creation flow running.
		Placeholder Sections: Create empty frames/sections/pages for each of the main features (Activities, Bulletin Board, Emergency Contacts, Account Info. with logout).
		Initial Wireframes: Finalize basic UI wireframes and prototypes for the overall app layout.


Sprint 3

	Start Date: August 7
	End Date: August 13
	Activities: 
 		High Priority UI Implementation- Implement basic UI for all priority 1 user stories
		Basic Data Display- For at least one section (ex: Emergency Contacts) display the data to show the interface is “running”
		Database Connection (initial)- Setup the initial SQLite database connection (without full CRUD yet)

Sprint 4

	Start Date: August 14
	End Date: August 20
	Activities:
		Attempt Priorities 2 implementation
		Documentation Update- Ensure all project documentation is up-to-date with current state
		Final Presentation Prep- Prepare for final presentation


User Stories
	
	0	User Authentication & Account Management
	
	As a student, I want a secure and personalized experience, so I must first create an account and log in to access my personal data and the app’s features
	
	
	0.1	Create an Account
	
	As a new student, I want to create an account by providing a unique username and password, so that I can securely access the CampusLink application for the first time.
	
	
	0.2	Log In to Account
	
	As a student, I want to log in to my account with my username and password, so that I can access my personalized schedule, tasks, and campus information.
	
	
	0.3	View Account Details
	
	As a student, I want to see my username and account details in an “Account” tab, so that I can verify I am logged in and feel a sense of ownership over my data.
	
	
	0.4	Log Out of Account
	
	As a student, I want to log out of my account from the “Account” tab, so that my personal information is protected when I am no longer using the application.


	1	Activities/Task Manager	
	
	As a student, I want to easily manage my weekly schedule, including classes, appointments, and personal tasks, so I can stay organized and on top of my commitments.
	
	
	1.1	View Personal Schedule
	
	As a student, I want to view my weekly list of activities and tasks with a dedicated window or tab, so I can easily see my upcoming commitments at a glance.
	
	
	1.2	Add/Edit Activities/Tasks
	
	As a student, I want to be able to add new activities or tasks(ex: class, study group, appointment, etc.) through a clear input form, specifying details like title, description, date, and time, so I can keep my schedule updated. And have the option to delete them after completion or if no longer relevant.
	
	
	1.3	Mark Tasks as Complete
	As a student, I want to mark tasks as complete via a checkbox or button, so I can track my progress and organize my pending items within the application.
	
	
	2	Bulletin Board
	
	As a student, I want to browse and post campus-relevant announcements, news, and student initiatives, so I can stay informed and connect with the campus community.
	
	
	2.1	View Announcements
	
	As a student, I want to view a scrollable feed of announcements posted on the bulletin board, so I can stay informed about campus news and opportunities.
	
	
	2.2	Post New Announcements
	
	As a student, I want to be able to compose and post new announcements (ex: lost and found, study group invites, club promotions, etc.) through a dedicated input form, so I can share information with the community.
	
	
	2.3	Search/Filter Announcements
	
	As a student, I want to search or filter announcements by keywords or categories (if applicable), so I can quickly find relevant information.
	
	
	3	Emergency Contacts
	
	As a student, I want quick, one-click access to essential campus services like security, health, and counseling, so I can get help immediately in an emergency.


	3.1	Access Emergency Contacts
	
	As a student, I want quick access to a clearly displayed list of emergency and support contacts (ex: Campus Security, Health Services, Counseling) within a dedicated section, so I can get help when needed.


 	3.2	View Contact Details

	As a student, I want to be able to click on a contact to view their full phone number , so I can easily reach out for assistance.

