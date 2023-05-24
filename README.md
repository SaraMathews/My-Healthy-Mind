# My Healthy Mind

## Description

### Who is the user?

### What is the purpose?

## UX and design

### Mind Map

![Mind Map](docs/mindmap.png)

### Wireframe

![Home Page wireframe](docs/wireframe_homepage.png)
![Daily Journal wireframe](docs/wireframe_dailyjournal.png)
![Past Journals wireframe](docs/wireframe_pastjournals.png)

## Features

### Home Page with navigation

The Home Page offers visitors a welcoming text and an image capturing the purpose of the website. A navbar is displayed on the top of the page for easy navigation between the websites different pages. A footer is displayed on the bottom of the page.

### User autentication

To be able to log a Daily Journal with the supporting features, the visitor of the webiste must first sign up. They can then sign in and sign out at any time. This feature of user authentication ensures secure access to the website's features. Only registered users can sign in, log a journal, view past journals, edit and delete their journals.

### Features Cards

### Daily Quotes Card

A daily quote is displayed on the homepage to inspire and motivate both users and visitors, with new quotes added and updated regularly by the admin. This feature offers both users and visitors a positive and motivational experience while on the website.

### Log Daily Journal

This features allows the users to record their daily thoughts, emotions and happenings of the day. With the additional features of rating their day and upload a photo, the user can create a more personalised and memorable journal.

### View Past Journal entries

This feature lets the user view their past journal entries as a list, in a convenient way. This allows the user to look back and reflect on previous days thoughts and feelings.

### Edit Past Journal entries

On each journal entry there is an edit button that lets the user edit the Journal entry. This gives the user the ability to make changes or correct mistakes. The user can either save the updated form or cancel the ongoing edit.

### Delete Past Journal entries

On each journal there is a delete button that allows the user to delete journal entries that they no longer wish to keep.
It gives the user the flexibility to delete journals that no longer serve a purpose or that they would rather not have on record.
The user is taken to a confirmation page where they have to confirm they want to delete the journal, or they have the option to cancel the initiated deletion.

### Admin page

While on the Admin page the administrator can manage and maintain features on the website. They can create, edit or delete Daily Quotes and handle management regarding the Journal features, and users.

## User Stories

![User stories overview](docs/userstories.png)

## Entity-relationship Diagram

## Testing

### Performance

### Validator testing

### Functional testing

### Unfixed bugs

## Technologies

Django, gunicorn(server heroku),
supporting libraries - dj_database_url, psycopg2
cloudinary

### Languages

### Frameworks and libraries

### Databases

PostgreSQL

## Deployment

### Version control

The git commands below were used throughout development to push code to the remote repository in GitHub:

git add . - This command was used to add a change in the working directory to the staging area.
git commit -m "message" -This command was used to save changes to the local repository. A brief description of what has changed and when.
git push - This command was used to push all commits to the remote repository on GitHub.
Deploy to Heroku

### Deploy to Heroku

The steps below were followed to deploy the app to Heroku:

Open the Heroku website and select "New" to create a new app.
After choosing a name for the new app, and selecting the correct region, click on "Create app".
Navigate to "Settings" and go to the Config Vars section. Add a Config Var with the keyword "PORT" and value of "8000".

Navigate to the top menu and go to "Deploy". Scroll down and set the Deployment Method to "Github". Once Github is selected, locate your repository and link it to Heroku.
Scroll down to Manual Deploy, ensure that the "main" branch is selected, and click "Deploy Branch".
You will see the text "Your app was successfully deployed.". Click the button "View" to open the link to your deployed app.

### Clone the Repository from GitHub

The steps below were followed to clone the repository locally:

Navigate to the main page of the GitHub Repository you want to clone.
Above the list of files, click on the drop-down button "<>Code".
Copy the repository link.
Open Terminal, type git clone followed by the copied URL, and press enter to create your local clone.

## Credits
