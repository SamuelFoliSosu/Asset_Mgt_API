#Asset Management API

##Overview

This project is an Asset Management API designed to help organizations track and manage their physical and digital assets efficiently. It covers asset registration, ownership, maintenance, status tracking, and history.

Built with Django and Django REST Framework, it provides RESTful API endpoints for asset lifecycle management.

##Current Status
- Project initialized with Django

- Created 10 Django apps aligned with core data models:

    - departments

    - locations

    - roles

    - users

    - owners

    - assets

    - ownership_history

    - maintenance_logs

    - asset_status

    - asset_status_history

- Models implemented for each app following the master schema

- SQLite database in use (default Django)

- Django REST Framework installed and configured

- Pagination set to 20 items per page

- JSON is the default response format

- Exception handling enabled with DRF default handler