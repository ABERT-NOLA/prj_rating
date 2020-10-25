# prj_rating
Prj_rating enables users to view various projects uploaded other users, rate and comment on them.An authenticated User can uploaded his/her project.The user can also view other user profiles along with how many projects the user has.

## Prerequisites
- Have Git installed.
- Have Python and Pip Installed
- Have a text editor or an IDE installed e.g VS Code, Atom
### Technologies Used
- Python, Django, JavaScript, CSS and HTML
- VS Code.
### API Endpoints
1. posts = `https://project-rater-alb.herokuapp.com/v1/posts`
2. users = `https://project-rater-alb.herokuapp.com/v1/users`
### Setup Installation
To run the application:-
1. Clone the repository to a folder in your machine using `https://github.com/ABERT-NOLA/prj_rating.git`
2. Cd to that folder.
3. Create a virtual environment using `python3 -m venv virtual`
4. Activate the virtual environment using `source virtual/bin/activate`
5. Install all the django packages in 'requirements.txt' using `pip install -r requirements.txt`.
6. Create a .env file add the following:
    `SECRET_KEY='<insert_your_ secretkey>'`
    `DEBUG=True`
    `DB_NAME='<database_name>'`
    `DB_USER='<database_username>'`
    `DB_PASSWORD='<database_password>'`
    `DB_HOST='127.0.0.1'`
    `MODE='dev'`
    `ALLOWED_HOSTS='*'`
    `DISABLE_COLLECTSTATIC=1`
7. Run:-
    - `python3 manage.py makemigrations`- Creates a migrations folder and database with all the tables
    - `python3 manage.py migrate`

8. Open the project on your Text Editor/IDE
9. Run `python3 manage.py runserver` on your terminal


#### Author
- Albert Omboge
    
