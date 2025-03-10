# Expense Tracker API

![Flask](https://img.shields.io/badge/Flask-2.3.2-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-green)
![JWT](https://img.shields.io/badge/JWT-Authentication-orange)
![Swagger](https://img.shields.io/badge/Swagger-API%20Documentation-brightgreen)

A **Flask-based Expense Tracker API** that allows users to manage their expenses securely. This project demonstrates best practices in backend development, including authentication, error handling, database management, and API documentation.

---

## Features

- **User Authentication**:
  - Register and log in with JWT (JSON Web Tokens).
  - Protected endpoints for authenticated users only.
- **Expense Management**:
  - Create, read, update, and delete expenses.
  - Each expense is tied to a specific user.
- **Error Handling**:
  - Custom error messages for invalid requests.
  - Proper HTTP status codes for errors.
- **API Documentation**:
  - Interactive Swagger UI for testing and documentation.
- **Best Practices**:
  - RESTful API design.
  - Environment variable configuration.
  - Modular code structure.

---

## Technologies Used

- **Backend**: Flask, Flask-RESTx, Flask-SQLAlchemy, Flask-JWT-Extended.
- **Database**: PostgreSQL.
- **API Documentation**: Swagger UI.

---
### Prerequisites

- Python 3.9+
- PostgreSQL
- Docker (for local database setup) run the docker-compose file

