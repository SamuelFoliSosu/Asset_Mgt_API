# Asset Management API

## Overview
The **Asset Management API** is a Django REST Framework (DRF) project designed to help organizations efficiently track and manage both physical and digital assets. It provides RESTful endpoints to manage:

- Departments, Locations, and Roles
- Users
- Assets and Owners
- Ownership history
- Maintenance logs
- Asset status and status history

The API supports **token-based authentication**, **pagination**, and **role-based access control**.

---

## Tech Stack
- **Backend:** Django 5.2, Django REST Framework  
- **Authentication:** DRF Token Authentication  
- **Database:** SQLite (default Django)  
- **Documentation:** Swagger & Redoc via drf-yasg  

---

## Project Structure
| App | Purpose |
|-----|---------|
| departments | Manage departments and locations |
| locations | Manage location-specific details |
| roles | Manage user roles |
| users | Manage user accounts and authentication |
| owners | Manage asset owners |
| assets | Manage asset records |
| ownership_history | Track asset transfers between owners |
| maintenance_logs | Track maintenance activities for assets |
| asset_status | Manage asset status definitions |
| asset_status_history | Track status changes over time |

---

## Key Features
- RESTful CRUD endpoints for all models  
- Pagination (20 items per page) for list endpoints  
- Token-based authentication  
- Role-based permissions for sensitive actions  
- Filtering and searching for assets  
- Automated ownership and status history logging  
- Swagger and Redoc API documentation

---

## Authentication
1. **User Registration**: `POST /api/users/register/`  
2. **Login**: `POST /api/users/login/` → Returns a token  
3. **Logout**: `POST /api/users/logout/`  

Include the token in the header for protected endpoints:
 - Authorization: Token <your_token_here>


---

## API Endpoints

| Resource | Endpoint | Method | Description |
|----------|---------|--------|-------------|
| Departments | `/api/departments/` | GET, POST | List all departments / Create a department |
| Department Detail | `/api/departments/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a department |
| Locations | `/api/locations/` | GET, POST | List all locations / Create a location |
| Location Detail | `/api/locations/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a location |
| Roles | `/api/roles/` | GET, POST | List all roles / Create a role |
| Role Detail | `/api/roles/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a role |
| Users | `/api/users/` | GET, POST | List all users / Create a user |
| User Detail | `/api/users/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a user |
| Owners | `/api/owners/` | GET, POST | List all owners / Create an owner |
| Owner Detail | `/api/owners/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete an owner |
| Assets | `/api/assets/` | GET, POST | List all assets / Create an asset |
| Asset Detail | `/api/assets/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete an asset |
| Ownership History | `/api/ownership-history/` | GET, POST | List or create ownership transfers |
| Ownership Detail | `/api/ownership-history/<id>/` | GET | View a specific transfer |
| Maintenance Logs | `/api/maintenance-logs/` | GET, POST | List or log maintenance activities |
| Maintenance Detail | `/api/maintenance-logs/<id>/` | GET, PUT, PATCH, DELETE | View or update a maintenance log |
| Asset Status | `/api/asset-status/` | GET, POST | List or create asset status types |
| Asset Status Detail | `/api/asset-status/<id>/` | GET, PUT, PATCH, DELETE | Retrieve or update a status type |
| Asset Status History | `/api/asset-status-history/` | GET, POST | List or create status change records |
| Status History Detail | `/api/asset-status-history/<id>/` | GET | Retrieve a specific status change |

---

## API Documentation
- Swagger UI: `/swagger/`  
- Redoc: `/redoc/`  

---

## Pagination
- Default page size: 20 items per list endpoint  
- Query param: `?page=<number>`

---

## Error Handling
- **404 Not Found** – Resource does not exist  
- **400 Bad Request** – Validation errors  
- **401 Unauthorized** – Missing or invalid token  
- **403 Forbidden** – Access denied for your role  

---

## Setup Instructions
1. Clone the repo  
2. Create and activate a virtual environment  
3. Install dependencies:  
```bash
    pip install -r requirements.txt
```
4. Run migrations:
```bash
    python manage.py makemigrations
    python manage.py migrate
```
5. Create a superuser:
```bash
    python manage.py createsuperuser
```
6. Start the server:
```bash
    python manage.py runserver
```
7. Access API at http://127.0.0.1:8000/

