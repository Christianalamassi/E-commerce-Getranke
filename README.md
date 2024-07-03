# E-commerce (Getränke)

## Overview

This project was designed, developed, and based on the idea of online shop to create a simple and easy method for the customers to buy drinks online. The users are given the possibility to add the order to thier basket, update it and delete it at any time before the payment. All these functionalities can be accessed by any user with an account. The admins have special permissions for controlling the data (CRUD). The website was made for real life simulation, although the shop and drinks don't exist in real life. The web site was developed using HTML, CSS, JS, Python "Django" and data are stored in an Elephant SQL database. The project can be accessed through this link [Getränke]().

### Features
Some elements appear on all of the pages of the website, like navbar and the footer.

- Navbar
  - The navigation is fixed at the top of the page and esay to use. It includs three buttons "Home","Order Here" and either or "log out" and "Profile" when the user logged in "log in" and " register" when the user logged out and "Management" if the user is superuser.
  - Also, the navbar is responsive to different screen sizes.

- Footer
    The footer includes the contact of the shop, email and social media links.

### Home
This is the main page, and just includes background and if the user is authenticated can see the basket in right top of the page.

### Order Here
- This page is available to everyone.
On this page where customers can find products and see the details of each product.
- When the user clicks on any item, it displays the item individually, where the user can add the order to the cart in the quantity a user needs, provided that it is less than 1000



appointment panel

Four inputs "The pet name", "The date", "The time", "Textarea". notace The imee is available for booking an appointment (different options)".

Two buttons to submit or reset.

Three validation errors that appear:

when the user enters an invalid time
when the user books an already booked appointment
when the user tries to book more than one appointments
A link to the information on the appointment

This link gives the user the possibility to access the booked appointment including the information.
Also, it shows them a message, if they don't have an appointment, to inform them that they don't have one yet.
It provides buttons to edit and delete if the user has booked an appointment or an appointment button if the user does not have one.
The user receives a confirmation message before the deletion.
 - Additionally it includes a Home button, which takes the user to the homepage. 


Sign Up
On the main page, the user can click on "Sign Up" if the user wants to create an account. It has a link to the log-in page if the user already has an account. The user has to choose a username and a password that has to be filled-in twice, email is optional. The form has instructions that the user has to follow to be able to create an account. 

Login
On this page, the user only has to enter their username and password to log in to the page. It has a link to the Sign Up page if the user has no account. The user will automatically be to the booking panel when it logged in. 

Logout
When the user is logged in and clicks on "Logout" up on the navigation bar, the user will automatically be redirected to this page first. The user receives the question if they are sure they want to log out. To log out they click on the button "confirm" 

UX
Strategy
Project Goal
This Project was created for a vet clinic that is useful for clients and staff members.

User story
The purpose of the project is to give the possibility for the clients to book an appointment to see the vet for their pets. They just need to create an account and then log in to access the appointment panel where they can book their appointment.

In addition, the users have the ability to change (edit) and delete their appointments at any time, as long as they are logged in. The webiste is easy for the user to navigate through.

Also, any visitor to the website can read about the vets to know who they are before they decide whether to be a client or not.

- As a user, I can get to know the doctors&#39; history in order to decide whether to be their client or not.
- As a user, I can click on the booked appointment link so that I can see my appointment at any time.
- As a user, I can book an available appointment so that nobody interferes with the appointment.
- As an admin, I can style the base.HTML page so that I can inherit style to the rest of the HTML pages.
- As a user, I can find the appointment bottom in the navbar so that I can access the appointment page without turning back to the main page
- As a user, I can book, edit, or delete an appointment so that I have flexibility.
- As a user, I can ignore the deletion so that I have the chance to keep my appointment.
- As a user I can sign up so that I have an account to be able to book an appointment.
- As a user, I can go to profile so that I can make an appointment.
- As a user I can easily navigate from the home page so that I can access whatever I want without confusion.
- As an Admin I can create, read, update, and delete the bookings so that I can manage the booking system.
- As an admin I can create, read, update, and delete the bookings so that I can manage the booking system.
- As a user I can sign up so that I can have my own profile.
Here is the link to User stories 



Structure
The user can access the home page and the About Us page without having a profile, but to access the booking system, the user must create an account. Then the user will have their own profile so that they can access the booking and booking panel. To schedule an appointment, the user will receive a text message confirming the appointment with the ability to modify or delete the appointment. Also, if the user returns to the home page, they can still come back at any time to edit or delete the appointment. 

Scope
Simple and intuitive User Experience.
Create a responsive design for desktop, tablet, and mobile devices.
Add information about location contact and social media.
Allow access to the Profile page only for client type of users
Make a clear and easy design for the users
Create a booking system feature that allows the users to display, edit, and delete the appointment as well as the staff members..
Create a Profile page for the user, so the user can book an appointment.
Skeleton
The project uses the ElephentSQL relational database for storing the data. There was just one diagram created for this project.

Surface
Visual Effects

Flex-box
Animation
Hover effects
Box shadows
Color palette

rgba(255, 255, 255, 0.4)
rgb(224, 205, 205)
Black
rgb(138, 119, 15)
rgb(224, 205, 205)
Fonts imported from fonts.googleapis google.font

Verdana, Geneva, Tahoma, sans-serif
Arial, Helvetica
Technologies Used
Languages
HTML was used as the foundation of the site.
CSS was used to add the style and layout of the site.
JavaScript was used for interaction
Python Used for back end and front end
Frameworks:
Django Used as a framework
Bootstrap5 For adding predefined styled elements and creating
Other tools:
Cloudinary For storing static data
Gitpod Hosted the workspace.
Heroku Used for deploying the project
GitHub Used for hosting the source code of the program
Favicon.io Used for generating the website favicon
Chrome-Del-Tools For debugging the project
W3C HTML Validator Used for validating the HTML
CI Python Linter Used to validating Python
Font-Awesome For creating attractive UX with icons responsiveness
Google-Fonts for typography
JsHint used for validating the javascript code
Jigsaw CSS Validator Used for validating the CSS
elephantsql Where the DB is storing
django-allauth Used for the authorization
gunicorn
app-diagrams Used to design the RED
amiresponsive Used to check responsive screen
Deployment
Install the dependencies:

Open the terminal window and type:
pip3 install -r requirements.txt.
Create a .gitignore file in the root directory of the project where you should add env.py.
Create a .env file. and added the following.
Added "DEVELOPMENT" in os.environ to DEBUG in setting.py.
Added '.herokuapp.com' in the setting to ALLOWED_HOSTS.
import os:
os.environ['SECRET_KEY'] = 'Add a secret key'.
os.environ['DATABASE_URL'] = 'will be used to connect to the database'.
Also add os.environ['DEVELOPMENT'] = "True" in env.py.
Push to GitHub.
Migrate by Run the following commands in a terminal:

python3 manage.py makemigrations.
python3 manage.py migrate.
Setting up Heroku

Go to the Heroku website Heroku.

Log in or create a Heroku account.

Login to Heroku and choose Create App.


Click New and Create a new app.


Choose a name and select your location.


Go to the Resources tab.

From the Resources list select Heroku Postgres.


Navigate to the Deploy tab

Click on Connect to Github and search for your repository.


Navigate to the Settings tab.

Click on the "Settings" tab and then on "Reveal Config Vars".

Delete "DISABLE_COLLECTSTATIC = 1" from the list.

Add CLOUDINARY_URL = API, DATABASE_URL = API, SECRET_KEY = API to the list.


Now click on the tab "Deploy"


and then on the button "Deploy Branch" at the bottom of the page. - 

When it's deployed, Click on "Open App" to access the website.

Here is the website Vet Tiere.

Testing
I have tested the project by the following points

Validator Testing
Python

Passed the code to PEP8.
  
HTML

No errors were returned when passing through the official W3C validator
  
CSS

No errors were found when passing through the official (Jigsaw) validator

JavaScript

Undefined bootstrap was checked and there are no error Jshint validator.

The website has been tested and works on different screen sizes and is responsive.








Lighthouse








Manually checking
General Tests
It has been tested and works in several web browsers such as Firefox and Edge.
All alerts disappear after four seconds.
The user can't book an invalid date or multiple appointments.
It was made sure that each user had their own appointment.
The user gets alert messages when they log in or log out.
The navigation stays at the top of the page.
Booking system
Back end connected with front end.
It shows a message for the user when they entered an invalid date or multiple appointments or a taken appointment.
It takes the user to a confirmation message that includes the information of the appointment.
Delete and Edit are functioning
It allows the user to delete, edit, and read the appointment at any time.
It gives the user a chance to undelete the appointment after clicking on delete bottom.
Authorization
Sign-Up
The Sign-Up page works good.
The link to the Log-in page works correctly.
Log-in
The Log-in page works good.
The link to the Sign-Up page works correctly.
The user has to enter the user details correctly to be able to log in.
Log-out
The Log-out page works good.
The button works good.
Bugs
Fixed bugs
The error was solved by deleting the duplicate id. 

The elements were unclear. It was fixed by adding background.  

It wasn't clear to the user that they could book only one appointment. It was fixed by adding a message at the top of the page. 

Unfixed bugs
The user can't see the available and unavailable appointments before choosing on the date.
ERD


Credits
inspiration was taken from Code Institute
Icons are from Font-Awesome.
This website uses Bootstrap.
Images on this website are hosted and managed by Cloudinary.
Fonts are from Google-Fonts.
This website is powered by Django.
To check representative screen amiresponsive.
Used to test JavaScript JsHint.
Used to stor DB elephantsql.
Used to test CSS Jigsaw CSS Validator.
Used to test HTML code W3 W3C HTML Validator.
Used for Favicon.
Used to design the RED app-diagrams.
Used to check resporesponsive screens responsiveviewer
Media
An image was taken from depositphotos.
Images were taken from 123rf.
An image was taken from pixabay.
About
No description, website, or topics provided.
Resources
 Readme
 Activity
Stars
 0 stars
Watchers
 1 watching
Forks
 0 forks
Releases
No releases published
Create a new release
Packages
No packages published
Publish your first package
Deployments
76
 ppfour last month
+ 75 deployments
Languages
JavaScript
38.9%
 
CSS
35.6%
 
HTML
16.8%
 
Python
8.7%
Suggested workflows
Based on your tech stack
Node.js logo
Node.js
Build and test a Node.js project with npm.
Webpack logo
Webpack
Build a NodeJS project with npm and webpack.
Publish Node.js Package logo
Publish Node.js Package
Publishes a Node.js package to npm.
More workflows
Footer
