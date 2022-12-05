This is a project to make and find reviews about teachers and classes in college.  It is currently designed right now for Casper College but may later be updated to included other colleges.

How to run this Django project with Visual Studio Code:

1. Clone and fetch this repository.
2. Open a command line and navigate to the College-Reviews folder
3. Open the files with Visual Studio Code.  Assuming you have Python3 installed, start a virtual environment here with the command line. (Extra instructions: https://code.visualstudio.com/docs/python/tutorial-django)
4. In VS Code, select a new interpreter at view > command palette > python:select interpreter, and choose the virtual environment.
5. Close your terminal and make a new one; it should activate the venv.
6. Update pip: python -m pip install --upgrade pip
8. Install the requirements: pip install -r requirements.txt
9. Run the project: python manage.py runserver

Accessing the admin site:

1. At /admin, you can log in with the default username "admin" and the password "password".
