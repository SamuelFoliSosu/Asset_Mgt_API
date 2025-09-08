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
- Ownership and status history logging 

---

## Authentication
1. **User Registration**: `POST /api/register/` 
2. **Login**: `POST /api/login/` → Returns a token 
3. **Logout**: `POST /api/logout/` 

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
| Users | `/api/users/` | GET | List all users (admin only) |
| User Detail | `/api/users/<id>/` | GET, PUT, PATCH, DELETE | Retrieve, update, or delete a user (self or admin) |
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
4. Set up environment variables for production:
```bash
    export DJANGO_SECRET_KEY='your-secure-secret-key-here'
    export DJANGO_DEBUG='False' # Or 'True' for local dev
```
5. Run migrations:
```bash
    python manage.py makemigrations
    python manage.py migrate
```
6. Create a superuser:
```bash
    python manage.py createsuperuser
```
7. Start the server:
```bash
    python manage.py runserver
```
8. Access API at http://127.0.0.1:8000/

---

## Sample Test Requests

### Register a User
**Request**
```http
POST /api/register/
Content-Type: application/json
```
```bash
{
  "username": "admin1",
  "email": "admin1@example.com",
  "first_name": "Admin",
  "last_name": "One",
  "password": "testpassword123"
}
```

**Response**
```json
{
  "message": "User registered successfully"
}
```

### User Login
**Request**
```http
POST /api/login/
Content-Type: application/json
```
```bash
{
  "username": "admin1",
  "password": "testpassword123"
}
```

**Response**
```json
{
  "token": "1234567890abcdef1234567890abcdef12345678",
  "user_id": 1,
  "username": "admin1",
  "email": "admin1@example.com"
}
```

### Create Role
**Request**
```http
POST /api/roles/
```
```bash
{
  "name": "Manager",
  "description": "Manages assets and users"
}
```

**Response**
```json
{
  "id": 1,
  "name": "Manager",
  "description": "Manages assets and users",
  "created_at": "2025-09-05T19:10:00Z",
  "updated_at": "2025-09-05T19:10:00Z"
}
```

### Create a Department
**Request**
```http
POST /api/departments/
```

Headers:
```bash
Authorization: Token 1234567890abcdef1234567890abcdef12345678
Content-Type: application/json
```

Body:
```bash
{
  "name": "IT Department"
}
```

**Response**
```json
{
  "id": 1,
  "name": "IT Department",
  "created_at": "2025-09-05T18:00:00Z",
  "updated_at": "2025-09-05T18:00:00Z"
}
```

### List Departments
**Request**
```http
GET /api/departments/
```

Headers:
```bash
Authorization: Token 1234567890abcdef1234567890abcdef12345678
```

**Response**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "name": "IT Department",
      "created_at": "2025-09-05T18:00:00Z",
      "updated_at": "2025-09-05T18:00:00Z"
    }
  ]
}
```

### Create a Location
**Request**
```http
POST /api/locations/
```
```bash
{
  "department": 1,
  "name": "Head Office - Accra"
}
```

**Response**
```json
{
  "id": 1,
  "department": 1,
  "name": "Head Office - Accra",
  "created_at": "2025-09-05T19:05:00Z",
  "updated_at": "2025-09-05T19:05:00Z"
}
```

### Update/Change a Location
**Request**
```http
PUT /api/locations/1/

where 1 is the <id>
```
```bash
{
  "department": 1,
  "name": "Warehouse - Kasoa"
}
```

**Response**
```json
{
  "id": 1,
  "department": 1,
  "name": "Head Office - Accra",
  "created_at": "2025-09-05T19:05:00Z",
  "updated_at": "2025-09-05T19:05:00Z"
}
```

### Asset Status
**Request**
```http
POST /api/asset-status/
```
```bash
{
  "status_name": "In Use",
  "description": "Asset is actively being used"
}
```

**Response**
```json
{
  "id": 1,
  "status_name": "In Use",
  "description": "Asset is actively being used",
  "created_at": "2025-09-05T19:40:00Z",
  "updated_at": "2025-09-05T19:40:00Z"
}
```

### Create an Asset Owner
**Request**
```http
POST /api/owners/
```
```bash
{
  "location": 1,
  "name": "IT Admin",
  "owner_type": "Staff",
  "contact_email": "itadmin@example.com",
  "phone": "+233200000000"
}
```

**Response**
```json
{
  "id":1,
  "location":1,
  "location_name":"Head Office - Accra",
  "department_name":"IT Department",
  "name":"IT Admin",
  "owner_type":"Staff",
  "contact_email":"itadmin@example.com",
  "phone":"+233200000000",
  "created_at":"2025-09-08T01:03:27.123506Z",
  "updated_at":"2025-09-08T01:03:27.123530Z"
}
```

### Create an Asset
**Request**
```http
POST /api/assets/
```

Headers:
```bash
Authorization: Token 1234567890abcdef1234567890abcdef12345678
Content-Type: application/json
```

Body:
```bash
{
  "asset_type": "Laptop",
  "asset_name": "Dell XPS 15",
  "location": 1,
  "owner": 1,
  "brand": "Dell",
  "model": "XPS 15 9500",
  "serial_number": "DX15-2025-001",
  "operating_system": "Windows 11",
  "cpu": "Intel i7",
  "memory": "16GB",
  "hard_disk_space": "512GB",
  "screen_size": "15.6",
  "ip_address": "192.168.1.50",
  "mac_address": "00:1A:2B:3C:4D:5E",
  "purchase_date": "2025-01-15",
  "purchase_price": 2000.00,
  "current_value": 1800.00,
  "useful_life_years": 5,
  "salvage_value": 500.00,
  "assigned_staff_name": "John Doe"
}
```

**Response**
```json
{
  "id": 1,
  "asset_type": "Laptop",
  "asset_name": "Dell XPS 15",
  "brand": "Dell",
  "model": "XPS 15 9500",
  "serial_number": "DX15-2025-001",
  "operating_system": "Windows 11",
  "cpu": "Intel i7",
  "memory": "16GB",
  "hard_disk_space": "512GB",
  "screen_size": "15.6",
  "ip_address": "192.168.1.50",
  "mac_address": "00:1A:2B:3C:4D:5E",
  "purchase_date": "2025-01-15",
  "purchase_price": 2000.0,
  "current_value": 1800.0,
  "useful_life_years": 5,
  "salvage_value": 500.0,
  "assigned_staff_name": "John Doe",
  "created_at": "2025-09-05T18:05:00Z",
  "updated_at": "2025-09-05T18:05:00Z",
  "location": 1,
  "owner": 1
}
```

### Search Assets
**Request**
```http
GET /api/assets/?search=Dell
```

Headers:
```bash
Authorization: Token 1234567890abcdef1234567890abcdef12345678
```

**Response**
```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "asset_name": "Dell XPS 15",
      "serial_number": "DX15-2025-001",
      "model": "XPS 15 9500"
    }
  ]
}
```

### Ownership History
**Request**
```http
POST /api/ownership-history/
```
```bash
{
  "asset": 2,
  "from_owner_id": 1,
  "to_owner_id": 2,
  "transfer_date": "2025-09-05",
  "condition_on_transfer": "Good",
  "comment": "Transferred to new staff"
}
```

**Response**
```json
{
  "id": 1,
  "asset": 2,
  "from_owner_id": 1,
  "to_owner_id": 2,
  "transfer_date": "2025-09-05",
  "return_date": null,
  "condition_on_transfer": "Good",
  "comment": "Transferred to new staff",
  "created_at": "2025-09-05T19:30:00Z",
  "updated_at": "2025-09-05T19:30:00Z"
}
```

### Maintenance Logs
**Request**
```http
POST /api/maintenance-logs/
```
```bash
{
  "asset": 2,
  "performed_by_user_id": 1,
  "maintenance_date": "2025-09-05",
  "maintenance_type": "Hardware Check",
  "status": "Completed",
  "next_due_date": "2025-12-05",
  "cost": 150.00,
  "action_taken": "Replaced thermal paste",
  "issue_description": "Overheating issue"
}
```

**Response**
```json
{
  "id": 1,
  "asset": 2,
  "performed_by_user_id": 1,
  "maintenance_date": "2025-09-05",
  "maintenance_type": "Hardware Check",
  "status": "Completed",
  "next_due_date": "2025-12-05",
  "cost": 150.0,
  "action_taken": "Replaced thermal paste",
  "issue_description": "Overheating issue",
  "created_at": "2025-09-05T19:35:00Z",
  "updated_at": "2025-09-05T19:35:00Z"
}
```

### Asset Status History
**Request**
```http
POST /api/asset-status-history/
```
```bash
{
  "asset": 2,
  "status": 1,
  "comment": "Assigned to staff member"
}
```

**Response**
```json
{
  "id": 1,
  "asset": 2,
  "status": 1,
  "changed_by_user_id": 1,
  "change_date": "2025-09-05T19:45:00Z",
  "comment": "Assigned to staff member",
  "created_at": "2025-09-05T19:45:00Z",
  "updated_at": "2025-09-05T19:45:00Z"
}
```