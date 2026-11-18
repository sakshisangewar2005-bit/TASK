# Recruitment & Placement Management System

**Technology:** Python, OOP, MySQL, `mysql-connector-python`, SQL, file handling.  
**Application type:** Console-based backend application. The HTML/CSS pages are a separate UI prototype and are not connected to the Python backend.

## Features
- Candidate registration, listing, search by ID and deactivation
- Company creation and listing
- Job creation and open-job listing
- Eligibility checks for active candidate, open job, deadline, percentage, passing year, backlog count and technology
- Duplicate application prevention
- Controlled recruitment status workflow
- Interview, offer and placement record creation
- Reports: candidates by technology, open jobs, applications by status, company-wise placements, placed and unplaced candidates
- Parameterized SQL, custom exceptions and `activity_log.txt`

## Project structure
```text
Recruitment_Placement_Management_System/
├── main.py
├── config.py
├── requirements.txt
├── rpms/
│   ├── model/       # Candidate and Job objects
│   ├── dao/         # MySQL database operations
│   ├── service/     # Business rules and eligibility engine
│   ├── util/        # Database connection and activity log
│   ├── exception/   # Custom exceptions
│   └── app/         # Console menu
├── sql/schema.sql
├── ui-prototype/   # Standalone HTML/CSS mock-up
└── tests/
```

## Setup (Windows / VS Code)
1. Install Python 3.10+ and MySQL Server.
2. Open this project folder in VS Code.
3. Create the database and tables by running `sql/schema.sql` in MySQL Workbench, or run:
   ```bash
   mysql -u root -p < sql/schema.sql
   ```
4. Open `config.py` and set your MySQL username and password. The database name should remain `rpms_db` unless you also change the SQL script.
5. In the project terminal:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
6. Start the application from the project root:
   ```bash
   python main.py
   ```

## First-use workflow
1. Add a company (menu 2).
2. Add a candidate (menu 1).
3. Create a job for that company (menu 3). Use the candidate's technology and passing year when testing eligibility.
4. Apply to the job (menu 4).
5. Update application status through `SHORTLISTED`, `INTERVIEW`, `SELECTED`, `OFFERED`, then `JOINED`. `REJECTED` is available as an alternative.
6. Add interview, offer and placement records from their respective menu options.

## Notes / limitations
- The HTML/CSS prototype uses sample display values only; it is not connected to Python or MySQL, as specified in the project abstract.
- Add/update operations for every possible field and a graphical/web backend are intentionally not included; the supplied technical specification says no web framework is required.
- Before creating an offer or placement, ensure the application is in the appropriate workflow status.
- MySQL `YEAR` columns expect a valid year.
- Database operations require a running MySQL server and valid credentials in `config.py`.

## Tests
Run the lightweight model test:
```bash
python -m unittest discover -s tests
```
