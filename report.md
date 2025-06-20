
# Final Project Report - Zodiac Matcher

## High-Level Description

Zodiac Matcher is a simple web application. It helps users find their zodiac sign based on birthday and gender. It also returns personality and best matched zodiac sign.

## Architecture

The application has 3 main parts:
1. Web API (Flask)
2. Zodiac logic module
3. Database (JSON and SQLite)

```plaintext
+-------------+      +-------------------+      +------------------+
| HTTP Client | -->  | Flask App (API)   | -->  | zodiac_utils.py  |
+-------------+      +-------------------+      +------------------+
                                                |
                                                v
                                           zodiac_data.json
```

## Design Justifications

- Flask is simple and good for REST API.
- Data is small, so SQLite and JSON are enough.
- Matching rules are static, stored in JSON and DB.

## System Requirements

- Input: birthday (MM-DD), gender (male/female)
- Output: zodiac, personality, match, reason
- Testable: Yes (unit and integration tests)

## Tests

- `test_zodiac_utils.py`: check zodiac logic
- `test_api.py`: check endpoint returns correct data
