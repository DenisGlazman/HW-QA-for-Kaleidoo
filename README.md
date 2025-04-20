
## Overview
This project is an automation testing solution for the website https://homme.co.il/ using Playwright (Python + Pytest). The goal is to automate the process of adding a new ad and submitting it through the site's interface.

## Project Structure

```plaintext
├── conftest.py                  # Configuration for pytest
├── debug_submit_ad.png          # Screenshot for debugging ad submission
├── debug_submit_waited.png      # Screenshot for debugging ad submission (waiting state)
├── images                       # Directory for image uploads
├── pages                         # Page Object Model (POM) classes
│   ├── home_page.py
│   ├── login_page.py
│   └── new_ad_page.py
├── tests                         # Test cases
│   ├── happy_path               # Tests for happy path scenarios
│   ├── resources                # Resource files for tests (e.g., images)
│   └── validation_&_edge_cases  # Tests for validation and edge cases
└── .venv                         # Virtual environment (not pushed to repo)
```

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/DenisGlazman/HW-QA-for-Kaleidoo.git
   ```

2. Navigate to the project directory:
   ```bash
   cd HW-QA-for-Kaleidoo
   ```

3. Set up the virtual environment:
   ```bash
   python3 -m venv .venv
   ```

4. Activate the virtual environment:
   - For macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - For Windows:
     ```bash
     .venv\Scriptsctivate
     ```

5. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

- Run tests with Pytest:
  ```bash
  pytest
  ```

- To run a specific test file:
  ```bash
  pytest tests/happy_path/test_create_new_ad_successfully.py
  ```

## Features

### Page Object Model (POM)
- The project uses POM to structure the tests, which makes the tests more maintainable and scalable.
- The `new_ad_page.py` contains the logic for interacting with the "Create New Ad" page.

### Screenshots
- Screenshots are taken during the test execution to debug issues.
- For example, `debug_submit_ad.png` and `debug_submit_waited.png` capture the state during ad submission.




