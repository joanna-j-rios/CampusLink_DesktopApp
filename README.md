# CampusLink_DesktopApp

Project Title: CampusLink Desktop App


Project Description

CampusLink is a desktop application built using Python and Tkinter, designed to serve as a centralized hub for university students. The application aims to simplify a student’s academic and social life by providing a single platform to manage schedules, discover events, stay informed through a community bulletin board, and access critical emergency contacts.


Key Features

	Activities & Task Schedule Manager: A user friendly interface to add, view, and edit a weekly schedule of classes, appointments, and personal tasks.
	Event Calendar: An interactive calendar to view and subscribe to various campus events. Categorized by interest such as academic, sports, and clubs.
	Bulletin Board: A dedicated section for Browse and posting announcements relevant to the campus community, including news, queries, and student led activities/initiatives.
	Emergency Contacts: A quick access panel with one click buttons to contact essential campus services like security, health, and counseling.


Development Methodology

This project is being developed using an agile methodology with an emphasis on iterative development, continuous feedback, testing, and collaboration through version control.


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

Joanna Rios - Technical Lead & System Architect

Responsibilities: Drives the technical vision, sets up the Git/GitHub repository and development environment, designs the overall software architecture, creates UML diagrams, and ensures code quality. The “swiss army knife” responsible for the technical documentation and ensuring deadlines are met.

Alicia Cortina - UI/UX Specialist/Prototyper & Feature Developer

Responsibilities: Focuses on the user interface design (Tkinter layouts, widgets, user flow), implements specific features like the "Activities/Task Schedule Manager" and "Bulletin Board," ensuring a good user experience.

Emma Pacheco - Backend Logic & Data Specialist / Tester

Responsibilities: Develops the underlying logic for features (e.g., notification systems, data handling for events/schedules), manages data storage (e.g., SQLite database i), sets up and runs testing procedures, and might focus on aspects like the "Event Calendar" data integration or "Emergency Contacts" logic.



Sprint Schedule
 
Sprint 1

	Start Date: July 24
	End Date: July 30
	Goal: Set up repository, define features, and draft documentation.

Sprint 2

	Start Date: July 31
	End Date: August 6
	Goal: Implement Create and Read tasks.

Sprint 3

	Start Date: August 7
	End Date: August 13
	Goal: Implement Update and Delete tasks.

Sprint 4

	Start Date: August 14
	End Date: August 20
	Goal: Add notifications and emergency contacts feature.


User Stories:

As a student, I want to create a new study task with a title, description, due date, and priority, so I can organize my work.

As a student, I want to view all my tasks in a list and filter them by due date or priority, so I can focus on what’s most urgent.

As a student, I want to mark tasks as complete, so I know what I’ve finished.

As a student, I want to edit the details of an existing task, so I can update information as needed.

As a student, I want to delete tasks that are no longer relevant, so my list stays clean.

As a student, I want to receive reminders for tasks due soon, so I don’t miss deadlines.

As a student, I want quick access to emergency campus contacts, so I can get help when needed.
