# grace-3005-a3 - PostgreSQL Student Management

Database Interaction with PostgreSQL and Application Programming

Grace Ong  
101255932

A simple terminal app in Python that displays, adds, updates, and deletes student records in PostgreSQL.

## Requirements

- Python 3.10 or later
- PostgreSQL
- pgAdmin 4
- psycopg (installed through requirements.txt)

## Project Files

- menu.py — Python app and menu
- sql/setup.sql — Creates the students table and inserts the initial data
- requirements.txt — Python dependencies

## Database Setup

1. Open pgAdmin and connect to your PostgreSQL server.
2. Right-click Databases and select Create → Database.
3. Name the database `student_management`.
4. Select this database and open Tools → Query Tool.
5. Open `sql/setup.sql` and execute it.

Run the setup script only once in a database where the students table does not already exist.

The script inserts the three initial students: John Doe, Jane Smith, and Jim Beam.

## Setup

Open a terminal in the project folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, replace the activation command with:

```powershell
.venv\Scripts\Activate.ps1
```
NOTE: I AM ON macOS, the above info about running on Windows is not verified by me personally

## Connection Settings

The app connects to the local PostgreSQL database using these settings in menu.py:

```python
conn = psycopg.connect(
    host="localhost",
    dbname="student_management",
    user="graceong",
)
```

Change `graceong` to your PostgreSQL username before running. Add `password="your_password"` to the connection settings locally if your server requires a password. 
There are no login prompts so PostgreSQL must be running and the `student_management` database must be set up before starting the application.

## Run the Application

With the venv activagted, run:

```bash
python menu.py
```

Choose an option from the menu.

For dates, use format YYYY-MM-DD. Leave blank to store NULL.

Student IDs are auto-generated. Use that number when updating or deleting an entry.

## Verify Changes

In pgAdmin, execute this query after adding, updating, or deleting a student:

```sql
SELECT * FROM students ORDER BY student_id;
```

## Demo Vid [PLEASE SEE CAPTION for added note that I forgot to mention in video audio]
https://youtu.be/LH08UriXgPs
