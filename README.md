# Mechanic Shop API

A RESTful API for managing a mechanic shop built with Flask, SQLAlchemy, Marshmallow, and MySQL. The project follows the Application Factory Pattern and demonstrates CRUD operations and database relationships.

---

## Features

### Customers

- Create a customer
- View all customers
- View a customer by ID
- Update customer information
- Delete a customer

### Mechanics

- Create a mechanic
- View all mechanics
- Update mechanic information
- Delete a mechanic

### Service Tickets

- Create a service ticket
- View all service tickets
- Assign a mechanic to a service ticket
- Remove a mechanic from a service ticket

---

## Technologies Used

- Python
- Flask
- SQLAlchemy
- Marshmallow
- MySQL
- Postman

---

## Project Structure

```
mechanic-shop-api/
│
├── application/
│   ├── blueprints/
│   ├── extensions.py
│   ├── models.py
│   └── __init__.py
│
├── app.py
├── config.py
├── requirements.txt
└── README.md
```

---

## API Endpoints

### Customers

- POST `/customers/`
- GET `/customers/`
- GET `/customers/<id>`
- PUT `/customers/<id>`
- DELETE `/customers/<id>`

### Mechanics

- POST `/mechanics/`
- GET `/mechanics/`
- PUT `/mechanics/<id>`
- DELETE `/mechanics/<id>`

### Service Tickets

- POST `/service-tickets/`
- GET `/service-tickets/`
- PUT `/service-tickets/<ticket_id>/assign-mechanic/<mechanic_id>`
- PUT `/service-tickets/<ticket_id>/remove-mechanic/<mechanic_id>`

---

## Testing

All API endpoints were tested using Postman.

---

## Author

**Matthew Shin**

Coding Temple Software Engineering Bootcamp


## Local setup and recording

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m flask --app "application:create_app()" run
```

The local Config defaults to a separate SQLite demo database. Existing MySQL data is not deleted or migrated. To use your existing database, export DATABASE_URL with its connection URI before starting. Do not commit credentials. Use disposable demo accounts only. 

Import `Mechanic Shop API.postman_collection.json` into Postman. Its base_url defaults to http://127.0.0.1:5000. Run requests in order: created IDs and login tokens are saved as collection variables. Use a fresh run_id for repeated demos. Customer creation is limited to three requests per hour in the advanced versions; restart the local demo server after rehearsing if needed. Do not reset a deployed service just for recording.

For a local `.env`, copy `.env.example` to `.env`, set your values, then load it in your shell with `set -a; source .env; set +a` before starting. Never commit `.env`.
