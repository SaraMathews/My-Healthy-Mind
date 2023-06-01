# My Healthy Mind

## Description

My Healthy Mind is an online journaling platform where users can log their daily thoughts, reflect on their experiences and work towards a happier healthier self.
The core functionality of My Healthy Mind revolves around journaling. In the journal, the user can write down all their thoughts and feelings. Beyond that, they can rate their day on a spectrum ranging from "Awful" to "Amazing, and they can also upload a photo to capture their day.
When users visit the website's home page, they are greeted with inspirational quotes that updates every time the website is reloaded. This feature aims to fill the user's experience with positivity and motivation.

### Who is the user?

My Healthy Mind is aimed at people who want to prioritize their mental well-being and that seek a platform for daily journaling to exprees their thoughts and feelings.

### What is the purpose?

The purpose of My Healthy Mind is to provide users with an online space to log their daily journal, and to be able to reflect on past journals. With a user-friendly interface and features like daily rating and uploading photos, the goal is to to promote mental wellness and a positive mindset.

![Device Mockup](docs/device_mockup.png)

## UX and design

### Mind Map

The Mind Map was made using Lucidchart.
![Mind Map](docs/mindmap.png)

### Wireframe

The Wireframe was made using Balsamiq Wireframes.

![Home Page wireframe](docs/wireframe_homepage.png)
![Daily Jo wireframe](docs/wireframe_dailyjournal.png)
![Past Journals wireframe](docs/wireframe_pastjournals.png)

## Features

### Home Page with navigation

- The Home Page offers visitors a welcoming text and an image capturing the purpose of the website.
- A navbar is displayed on the top of the page for easy navigation between the websites different pages.
- The navbar items differ depending on if the user is signed in or not.
- A footer is displayed on the bottom of the page with links to social media platforms.

![Homepage with navbar visitor](docs/navbar_visitor.png)
![Navbar user](docs/navbar_loggedin.png)

### User authentication

- To be able to log a Daily Journal with the supporting features, the visitor of the webiste must first sign up. They can then sign in and sign out at any time. This feature of user authentication ensures secure access to the website's features.
- Only registered users can sign in, log a journal, view past journals, edit and delete their journal entries.
- When the user has either signed up, signed in or signed out, a success message will appear letting the user know the action was successfull.

![Sign up](docs/signup.png)
![Sign in](docs/signin.png)
![Sign out](docs/signout.png)

### Features and Daily Quotes Cards

- On the home page two cards are displayed, brielfy explaing the two features "Daily Journal" and Past Journals" with two corresponding buttons. If the user (or a visitor on the page) is not signed in, the buttons are changed to link to the sign up page, and displays the text "Sign in to Journal" and "Sign in to view Past Journals" respectively.
- A daily quote is displayed on the home page, in between the two features cards, to inspire and motivate both users and visitors, with new quotes added and updated regularly by the admin. This feature offers both users and visitors a positive and motivational experience while on the website.

![Features and Daily Quote](docs/features_quotes.png)

### Log Daily Journal

- This features allows the users to record their daily thoughts, emotions and happenings of the day. With the additional features of rating their day and uploading a photo, the user can create a more personalised and memorable journal.
- A success message is displayed when the journal has been successfully submitted.

![Daily Journal](docs/dailyjournal.png)
![Submit confirmation](docs/submitted.png)

### View Past Journal entries

- This feature lets the user view their past journal entries as a list, in a convenient way. When the user clicks on the list item for the journal they want to view, it expands to view the journal content. To collapse the opened journal the user can click on the list item again.
- The ability to view past journals allows the user to look back and reflect on previous days, thoughts, and feelings.

![Past Journals](docs/past_journals.png)
![Past Journals expanded](docs/past_journals_expand.png)

### Delete Past Journal entries

- On each journal there is a delete button that allows the user to delete Journal entries that they no longer wish to keep.
  It gives the user the flexibility to delete journals that no longer serve a purpose or that they would rather not have on record.
- The user is taken to a confirmation page where they have to confirm the deletion of the journal entry, or they have the option to cancel the initiated deletion.
- A success message is displayed when the journal entry has been deleted sucessfully.

![Delete Journal confirm](docs/confirm_deletion.png)
![Delete Journal success](docs/deleted.png)

### Edit Past Journal entries

- On each journal entry there is an edit button that lets the user edit the journal entry. This gives the user the ability to make changes or correct mistakes. The user can either save the updated form or cancel the ongoing edit.
- A success message is displayed when the journal has been updated sucessfully.

![Edit Journal](docs/edit_journal.png)
![Edit confirmation](docs/updated.png)

### Error pages

- I've included three error pages for the webiste.
- The layout remains consistent across all error pages, with the appropriate error message displayed for each specific error.

  - 404: Indicates that the requested resource could not be found on the server.
  - 403: Signifies that access to the requested resource is forbidden or restricted.
  - 500: Represents an internal server error, indicating that something went wrong on the server's side while processing the request.

Below I have included the 404 error page to illustrate the design presented to the user when they are redirected to an error page.

![Error 404](docs/error404.png)

### Admin page

- While on the Admin page the administrator can manage and maintain features on the website. They can create, edit or delete daily quotes, and handle management regarding the journal features, and users.

![Admin page](docs/admin.png)

### Features left to implement

**Filter Past Journals**

- A filter that lets the user search and retrieve past journal entries based on specific dates and daily ratings.

## User Stories

I created user stories in Github and assigned them to 5 different milestones (Daily Journal, User Experience Improvements, User Authentication, Home Page and Development) and applied appropriate labels to each one. I organized and prioritized the tasks within the My Healthy Mind project.

![User stories overview](docs/userstories.png)

## Database schema & Entity-relationship Diagram

### JournalLog

- **id**
  - This attribute serves as the primary key for the JournalLog model, uniquely identifying each record in the table.
- **user**
  - This attribute is a Foreign Key field that establishes a relationship with the "User" model, indicating the user associated with each journal entry. It's a many-to-one relationship, where each journal entry is linked to a single user, and one user can have many journal entries.
- **created_on**
  - This attribute represents the date when the journal was created, and is a DateField which is used to store dates (year,month and day)
- **content**
  - This attribute stores the content of the Journal, and is a TextField which is used to store lager amounts of text data.
- **rating**
  - This attribute represents the daily rating that is given to to the Journal, and is a CharField which is used to store character data, such as strings. The available choices for the rating are 'Amazing', 'Good', 'Okay', 'Bad', and 'Awful'. The default value is set to 'Okay'.
- **image**
  - This attribute stores the image linked with the Journal using CaloudinaryField, which is a field specifically designed for storing Cloudinary image references.

![Entity-relationship Diagram](docs/ERD.png)

### DailyQuote

- **id**
  - This attribute serves as the primary key for the DailyQuote model, uniquely identifying each record in the table.
- **quote**
  - This attribute stores the Daily quote using a TextField.
- **author**
  - This attribute stores the name/details of the author of the Daily Quote, using a CharField
- **created_on**
  - This attribute represents the date when the quote was created, using a DateField

## Testing

### Performance

### Lighthouse

- Performance: 75
- Accessibility: 100
- Bess Practices: 100
- SEO: 100

### WAVE Web Accessibility Evaluation Tools**

- No errors

### Browser testing

The website is tested and displays well in Google Chrome, Mozilla Firefox, Safari and Microsoft Edge.

### Validator testing

### PEP8 validator
 
**dailyjournal app**

- admin.py: no errors
- models.py: no errors
- forms.py: no errors
- urls.py: no errors
- views.py: no errors

**home app**

- admin.py: no errors
- models.py: no errors
- urls.py: no errors
- views.py: no errors

**myhealthymind project**

- settings.py: no errors
- urls.py: no errors

### JSHint

- Not used for this project. I am using jQuery, and JSHint gives an "Undefined variable" error when jQuery is used.

### W3C CSS validator

- No errors

### W3C HTML validator

- base.html: No errors or warnings to show
  
- home.html : No errors or warnings to show
  
- daily_journal.html:
  - "Error: Attribute maxlength is not allowed on the select element at this point." - I will maintain the current implementation with the maxlength attribute on the select element because I am not completely sure how to resolve it, and with very little time left before the submission date, I don't want to compromise the current code and potentially face bigger issues and errors.
  
- previous_journals.html: No errors or warnings to show
  
- journallog_confirm_delete.html: No errors or warnings to show
  
- edit_journal.html:
  - "Error: Attribute maxlength is not allowed on the select element at this point." - I will maintain the current implementation with the maxlength attribute on the select element because I am not completely sure how to resolve it, and with very little time left before the submission date, I don't want to compromise the current code and potentially face bigger issues and errors.
  
- signup.html: No errors or warnings to show
  
- login.html: No errors or warnings to show
  
- logout.html : No errors or warnings to show

### Functional testing

Below, I have summarized the testing in screenshots of several Excel sheets for an easier overview. I have separated the sheets into the following categories: Home Page, Daily journal, User Autenthication, Error Pages & Success messages, and Admin.

**Home Page**
![Test Navbar and Footer](docs/test_navbar_footer.png)
![Test Daily Quote and Features cards](docs/test_quote_featurescard.png)

**Daily Journal**
![Test Daily Journal](docs/test_dailyjournal.png)

**User Autenthication**
![Test User Autenthication](docs/test_user_authentication.png)

**Error Pages & Success messages**
![Test Error Pages ](docs/test_error_pages.png)
![Test Success messages ](docs/test_success_messages.png)

**Admin**
![Test Admin Page ](docs/test_user_authentication.png)

### Unfixed bugs
daily_journal.html: "Error: Attribute maxlength is not allowed on the select element at this point.".I will be correcting this error in the future.

## Security measures

In order to maintain the security and privacy of the user's personal journal entries on My Healthy Mind website, I have implemented two measures. One is the usage of the {% csrf_token %} in the HTML forms. This token acts as a protective shield against potential attacks that could compromise the integrity of the user's journal data. It ensures that only authenticated and authorized users can submit, edit, and delete journal entries.

Additionally, on the views, I have implemented a custom test function using the LoginRequiredMixin and UserPassesTestMixin. This test_func checks if the currently logged-in user matches the user associated with the object being accessed. By verifying the user's identity, it ensures that only authorized users can perform specific actions, such as deleting and editing a journal entry.

## Technologies

- **HTML**
  - Used to structure and present the content of the web pages
- **CSS**
  - For adding personalized stying to the web pages
- **Bootstrap**
  - To provide pre-designed and pre-built components to style the web pages
- **JavaScript**
  - Used to enable interactive and dynamic behavior on the web pages
- **jQuery**
  - Is a JavaScript library that makes it easier to build an interactive and dynamic website.
- **Python**
  - Used in Django projects as the core programming language, responsible for handling the server-side logic, data processing, and constructing the backend functionality of applications, like My Healthy Mind.
  - Python packages dependencies used
    - asgiref==3.6.0
    - cloudinary==1.32.0
    - dj-database-url==0.5.0
    - dj3-cloudinary-storage==0.0.6
    - Django==3.2.19
    - django-allauth==0.54.0
    - gunicorn==20.1.0
    - oauthlib==3.2.2
    - psycopg2==2.9.6
    - PyJWT==2.7.0
    - python3-openid==3.2.0
    - pytz==2023.3
    - requests-oauthlib==1.3.1
    - sqlparse==0.4.4
    - urllib3==1.26.15
    - django-cloudinary-storage==0.3.0
- **Django**
  - This project was created using the Django framework
- **Balsamic Wireframes**
  - Used to create the wireframes
- **Lucidchart**
  - Used to make the MindMap
- **ui.dev/amiresponsive**
  - Used to create the Device Mockup image
- **DBeaver**
  - Used to create the ERD
- **uxwing.com**
  - Used for the social media icons
- **CodeAnywhere**
  - The IDE used for writing the code
- **Git**
  - Version control used to track changes in code during the development of the project
- **Github**
  - Used for storing my project
- **Heroku**
  - Used as the platform to deploy my project
- **Google Fonts**
  - Used to import the Lato font
- **PEP8 validator (CI Python Linter)**
  - Used to check so the python code in my project adheres to the guidelines specified in PEP 8
- **W3C HTML & W3C CSS**
  - Used to check my HTML and CSS code for errors
- **Lighthouse**
  - Used to help analyze and improve the quality of my website
- **WAVE Web Accessibility Evaluation Tools**
  - Used to help me identify potential accessibility issues on my webiste
- **Chrome Developer Tools**
  - Used to inspect and debug code

### Databases

- I used PostgreSQL as my database for storing and managing data

## Deployment

### Version control

The git commands below were used throughout development to push code to the remote repository in GitHub:

- `git add .` - This command was used to add a change in the working directory to the staging area.
- `git commit -m "message" ` -This command was used to save changes to the local repository. A brief description of what has changed and when.
- `git push`- This command was used to push all commits to the remote repository on GitHub.

### Deploy to Heroku

The steps below were followed to deploy the app to Heroku:

- Open the Heroku website and select "New" to create a new app.
- After choosing a name for the new app, and selecting the correct region, click on "Create app".
- Navigate to "Settings" and go to the Config Vars section.
  -Add the neccessary Config Vars.
  (Making sure to remove the DISABLE_COLLECTSTATIC, 1 and DEBUG, True before deployment.)

- Navigate to the top menu and go to "Deploy". Scroll down and set the Deployment Method to "Github". Once Github is selected, locate your repository and link it to Heroku.
- Scroll down to Manual Deploy, ensure that the "main" branch is selected, and click "Deploy Branch".
- You will see the text "Your app was successfully deployed.". Click the button "View" to open the link to your deployed app.

### Clone the Repository from GitHub

The steps below were followed to clone the repository locally:

- Navigate to the main page of the GitHub Repository you want to clone.
- Above the list of files, click on the drop-down button "<>Code".
- Copy the repository link.
- Open Terminal, type git clone followed by the copied URL, and press enter to create your local clone.

## Credits

- Code Institute LMS
- I Think Therefore I Blog - LMS
- The Slack Community
- My mentor Daisy McGirr
  - https://www.codu.co/articles/securing-django-views-from-unauthorized-access-npyb3to_
- Tutor Assistance
- Stack Overflow
- Bootstrap 4 documentation - www.getbootstrap.com
- Bootstrap 4 - www.3schools.com
- Bootstrap CSS Framework - Full Course for Beginners - https://www.youtube.com/watch?v=-qfEOE4vtxE
- Django documentation (all sections relating to my project) - https://docs.djangoproject.com/en/4.2/
- Python Django Web Framework - Full Course for Beginners - https://www.youtube.com/watch?v=F5mRW0jo-U4&list=PLTwiqKOPckq-B8XQQ-p7w4U11J6q8vwSo
- How to create a sticky footer - https://css-tricks.com/couple-takes-sticky-footer/ 
- Etag error Cloudinary - https://code-institute-room.slack.com/archives/C026PTF46F5/p1682785940128589?thread_ts=1682778905.761519&cid=C026PTF46F5
- uxwing.com - social media icons
- Google fonts - Lato font
- Allauth - for autentication pages
- Resize images - https://tinypng.com/
- Background image - https://www.freepik.com/
  **Create ERD**
- https://dbeaver.io/
- https://technology.amis.nl/database/quick-start-with-free-managed-postgresql-database-on-elephantsql/ 

### Inspired by

- Build a Personal Diary With Django and Python - https://realpython.com/django-diary-project-python/
- Build a Personal Journal With Django and Python - https://betterprogramming.pub/build-a-personal-journal-with-django-and-python-f4835d27368c