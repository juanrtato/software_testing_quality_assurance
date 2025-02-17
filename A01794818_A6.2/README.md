# Activity 6.2
# Hotel Management System

## Requirements
Before running the exercises, make sure you have Python 3 installed. You can install the required dependencies using:

```sh
pip install -r requirements.txt
```

### Running the Application
To start the application, execute:

```sh
python3 main_hotels.py
```

#### Application Usage
The application is operated via the console, where users can:

- Add, modify, and delete hotels.
- Create and cancell reservations.
- Add, modify, and delete customers.
- Retrieve hotel and customers details.

### Running the Application
Unit tests are located in the test/unit/ directory. To execute all tests, run:
```sh
python3 test/unit/hotels_reservation_test.py
```
# Directory organization
- data/: Stores application data, including customers, hotels, and reservations in JSON format.
- hotels_reservation.py: The core module that handles hotel management functionalities.
- evidence/: Contains execution evidence, including screenshots of the system running and linting results.
- test/: Includes unit tests for the system.
```sh
├── data
│   ├── customers.json
│   ├── hotels.json
│   └── reservations.json
├── evidence
│   ├── menu_hotel_manager.png
│   ├── pylint_flake8.png
│   └── test_execution.png
├── hotels_reservation.py
├── instructions
│   └── Actividad 6.2_Ejercicios-1.pdf
├── __inti__.py
├── main_hotels.py
├── __pycache__
│   └── hotels_reservation.cpython-310.pyc
├── README.md
├── requirements.txt
└── test
    ├── __init__.py
    ├── __pycache__
    │   └── __init__.cpython-310.pyc
    └── unit
        ├── hotels_reservation_test.py
        ├── __init__.py
        ├── __pycache__
        │   └── __init__.cpython-310.pyc
        ├── test_customers.json
        ├── test_hotels.json
        └── test_reservations.json

```
