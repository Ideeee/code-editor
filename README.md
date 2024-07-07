# PYTHON CODE EDITOR

#### An application to test and grade python code written by csc202 students

## SETUP

1. Clone the repo
2. Create a virtual environment with `python3 -m venv env`
2. Activate the virtual environment using `.\env\bin\Activate.ps1` or `.\env\bin\Activate.bat`
3. Copy the contents of env.sample into your .env file
4. Run `npm install`
5. Run `pip install -r requirements.txt` 
6. cd into the backend folder
7. Run the migrations using `alembic upgrade head`
8. Start the app with `uvicorn main:app --reload`, the application should start on `localhost:8000`
9. Navigate to `localhost:8000/docs` for the interactive api documentation


