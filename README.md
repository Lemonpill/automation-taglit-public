# automation-taglit-public

## Usage
1. Run `pipenv install` to install dependencies (requires Python 3.11 and pipenv)
2. Run `pipenv shell` to access the virtual environment
3. Run `python main.py` to run tests (select from src/suites.py)

## Overview
This performs a set of sanity tests on a number of pages. Tests include performing a valid sign-up and login from home pages of multiple countries (US, CA, SU, FR, DE, UK, AR) and reporting results to ./reports/ folder.

Reports include a CSV with test results and screenshots for each test.

This project uses Selenium for working with webdrivers and unittest for organizing and executing tests.

This project implements Page Object Model, in which page methods represent available page actions and can be reused during tests, avoiding (where possible) code replication.

## Structure
The project is structured in the following way

```
project-name/
  |
  |- /drivers/                                  webdrivers executables
     |
     |- chromedriver.exe                        currently only chrome
     |- ...
  |- /reports/                                  generated reports files
     |
     |- /test-report-1/                         example test report directory
        |
        |- /screenshots/                        test screenshots
           |
           |- 1-step-screenshot.png
           |- 2-step-screenshot-fail.png        'fail' mark on failed test steps
           |- ...
        |- result.csv                           current test results
     |- ...
     |- test-users.csv                          users created during tests
  |- /src/                                      source code
     |
     |- /cases/                                 test cases
        |
        |- /signup/                             signup test cases
           |
           |- country-a-signup-test.py
           |- country-b-signup-test.py
           |- ...
        |- /login/                              login test cases
           |
           |- country-a-login-test.py
           |- country-b-login-test.py
           |- ...
        |- ...
     |- /elements/                              page elements
        |
        |- base.py                              abstract base element
        |- application.py                       application page elements
        |- homepage.py                          home page elements                   
        |- ...
     |- /pages/                                 pages for implementing page-object model
        |
        |- base-page.py                         base page object
        |- application.py                       application page object
        |- homepage.py                          home page objects
        |- ...
     |- config.py                               configuration - use only on PROD
     |- helpers.py                              general use helper functions
     |- mailbox.py                              custom virtual mailbox class
     |- reporter.py                             custom reporter class
     |- suites.py                               here tests are loaded into suites
  |- main.py                                    main file
  |- Pipfile                                    dependencies
  |- Pipfile.lock                               
  |- README.md
  |- test.log                                   logger output
```

