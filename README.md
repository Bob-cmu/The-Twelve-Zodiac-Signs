
# Zodiac Matcher

This is a simple zodiac sign matching system for course project.

## Features

- Determine zodiac sign based on birthday.
- Show personality based on gender.
- Suggest best matched zodiac with reason.
- RESTful API using Flask.
- Data stored in JSON and SQLite.
- Includes unit tests and integration tests.

## How to Run

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Initialize database:
   ```
   python db/init_db.py
   ```

3. Start server:
   ```
   python app.py
   ```

4. Test endpoint:
   ```
   POST http://localhost:5000/match
   Body: {"birthday": "06-06", "gender": "male"}
   ```

## Project Structure

- `app.py` - main Flask app
- `zodiac_utils.py` - zodiac logic
- `db/init_db.py` - create SQLite DB
- `data/zodiac_data.json` - zodiac information
- `tests/` - unit and API tests
