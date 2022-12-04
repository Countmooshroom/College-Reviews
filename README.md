This is a project to make and find reviews about teachers and classes in college.  It is currently designed right now for Casper College but may later be updated to included other colleges.

How to run this Django project in GitHub for Desktop with Visual Studio Code:

1. In GitHub for Desktop, clone the repository from the url or the username and repository (Countmooshroom/College-Reviews).
2. Fetch the repository.
3. Open a command line and navigate to the College-Reviews folder
4. Open the files with Visual Studio Code.  Assuming you have Python3 installed, start a virtual environment here with the command line. (Extra instructions: https://code.visualstudio.com/docs/python/tutorial-django)
5. In VS Code, select a new interpreter at view > command palette > python:select interpreter, and choose the virtual environment.
6. Close your terminal and make a new one; it should activate the venv.
7. Update pip: python -m pip install --upgrade pip
8. Install Django: python -m pip install django
9. Run the project: python manage.py runserver

Accessing the admin site:

1. At /admin, you can log in with the default username "admin" and the password "password".
