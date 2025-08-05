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
	Activities: 
 		Set up repository
   		Define features
     	Draft documentation

Sprint 2

	Start Date: July 31
	End Date: August 6
	Activities: 
 		Core UI Setup- Implement the main Tkinter application window
		Navigation- Setup the primary navigation structure to switch between sections
		Placeholder Sections- Create empty frames/sections for each of the four main features (Activities, Events, Bulletin Board, Emergency Contacts)
		Initial Wireframes- Finalize basic UI wireframes for the overall app layout

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

	1	Activities/Task Manager	
	
	As a student, I want to easily manage my weekly schedule, including classes, appointments, and personal tasks, so I can stay organized and on top of my commitments.
	
	
	1.1	View Personal Schedule
	
	As a student, I want to view my weekly schedule of activities and tasks with a dedicated window or tab, so I can easily see my upcoming commitments at a glance.
	
	
	1.2	Add/Edit Activities/Tasks
	
	As a student, I want to be able to add new activities or tasks(ex: class, study group, appointment, etc.) through a clear input form, specifying details like title, description, date, and time, so I can keep my schedule updated.
	
	
	1.3	Receive Activity Reminders
	
	As a student, I want to be able to receive simple in-app notifications or visual alerts for upcoming activities (ex: pop-up message box or highlighting in schedule), so I don’t miss important commitments.
	
	
	1.4	Mark Tasks as Complete
	As a student, I want to mark tasks as complete via a checkbox or button, so I can track my progress and organize my pending items within the application.
	
	
	2	Event Calendar
	As a student, I want to find and subscribe to campus events categorized by my interests (academic, sports, clubs), so I can discover relevant activities and participate in campus life.
	
	
	2.1	Browse Campus Events
	
	As a student, I want to browse a list or grid of upcoming campus events within the applications calendar section, so I can discover activities relevant to my interests.
	
	
	2.2	Filter Events by Category
	
	As a student, I want to filter the displayed events by categories (ex: Academic, Sports, Civil, Clubs, etc.) using selection boxes or buttons, so I can easily find events that match my preferences.
	
	
	2.3	View Event Details
	
	As a student, I want to click on an event to view detailed information (ex: date, time, location, full description, etc.) in a dedicated pop-up or detail panel, so I can decide whether to attend. 
	
	
	2.4	Add Event to Personal Schedule
	
	As a student, I want to be able to add a campus event to my personal “Activities/Task Schedule Manager” with a single click, so I can integrate it into my daily plan.
	
	
	3	Bulletin Board
	
	As a student, I want to browse and post campus-relevant announcements, news, and student initiatives, so I can stay informed and connect with the campus community.
	
	
	3.1	View Announcements
	
	As a student, I want to view a scrollable feed of announcements posted on the bulletin board, sorted by recency, so I can stay informed about campus news and opportunities.
	
	
	3.2	Post New Announcements
	
	As a student, I want to be able to compose and post new announcements (ex: lost and found, study group invites, club promotions, etc.) through a dedicated input form, so I can share information with the community.
	
	
	3.3	Search/Filter Announcements
	
	As a student, I want to search or filter announcements by keywords or categories (if applicable), so I can quickly find relevant information.
	
	
	4	Emergency Contacts
	
	As a student, I want quick, one-click access to essential campus services like security, health, and counseling, so I can get help immediately in an emergency.


	4.1	Access Emergency Contacts
	
	As a student, I want quick access to a clearly displayed list of emergency and support contacts (ex: Campus Security, Health Services, Counseling) within a dedicated section, so I can get help when needed.


 	4.2	View Contact Details

	As a student, I want to be able to click on a contact to view their full phone number and any additional relevant details, so I can easily reach out for assistance.

