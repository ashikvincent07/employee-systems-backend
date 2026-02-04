# Employee API — Documentation

Base URL (local dev)
```
http://127.0.0.1:8000/
```

Authentication
- Registration is open: `POST /register/`
- All `/employee/` endpoints require HTTP Basic Authentication.
  - Use a valid username and password created via `/register/`.
  - Example with curl: `curl -u user5:user123 ...`
  - Note: The raw header `Authorization: Basic user:pass` is not valid — Basic auth requires the credentials to be base64-encoded. Use `-u` or encode as `Authorization: Basic BASE64(user:pass)`.

Common response formats: JSON.

Endpoints

1) Register (create user)
- URL: `POST /register/`
- Description: Create a new user account (used for subsequent authentication).
- Request headers:
  - `Content-Type: application/json`
- Request body (example):
```json
{
  "username": "user5",
  "password": "user123",
  "email": "user@gmail.com"
}
```
- Success response:
  - Status: `201 Created`
  - Body (example):
```json
{
  "id": 7,
  "username": "user5",
  "email": "user@gmail.com"
}
```
- Error responses:
  - `400 Bad Request` — validation errors (missing fields, password too short, email invalid, username already exists).

2) Create employee
- URL: `POST /employee/`
- Description: Create a new employee record. Requires Basic Auth.
- Request headers:
  - `Content-Type: application/json`
  - Authorization: HTTP Basic (e.g. `curl -u user5:user123`)
- Request body (example):
```json
{
  "name": "James Wilson",
  "department": "Finance",
  "designation": "Financial Analyst",
  "salary": 80000,
  "email": "j.wilson@company.com",
  "date_of_joining": "2023-05-22"
}
```
- Example curl:
```bash
curl -u user5:user123 -X POST "http://127.0.0.1:8000/employee/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "James Wilson",
    "department": "Finance",
    "designation": "Financial Analyst",
    "salary": 80000,
    "email": "j.wilson@company.com",
    "date_of_joining": "2023-05-22"
  }'
```
- Success response:
  - Status: `201 Created`
  - Body (example):
```json
{
  "id": 12,
  "name": "James Wilson",
  "department": "Finance",
  "designation": "Financial Analyst",
  "salary": 80000,
  "email": "j.wilson@company.com",
  "date_of_joining": "2023-05-22"
}
```
- Error responses:
  - `400 Bad Request` — validation errors (missing or invalid fields)
  - `401 Unauthorized` — authentication missing or invalid

3) List employees
- URL: `GET /employee/`
- Description: Retrieve a list of employees. Requires Basic Auth.
- Request headers:
  - `Accept: application/json`
  - Authorization: HTTP Basic (e.g. `curl -u user3:user123`)
- Example curl:
```bash
curl -u user3:user123 -X GET "http://127.0.0.1:8000/employee/" \
  -H "Accept: application/json"
```
- Success response:
  - Status: `200 OK`
  - Body (example):
```json
[
  {
    "id": 1,
    "name": "Alice Smith",
    "department": "Engineering",
    "designation": "Backend Engineer",
    "salary": 95000,
    "email": "alice@company.com",
    "date_of_joining": "2022-03-10"
  },
  {
    "id": 2,
    "name": "James Wilson",
    "department": "Finance",
    "designation": "Financial Analyst",
    "salary": 80000,
    "email": "j.wilson@company.com",
    "date_of_joining": "2023-05-22"
  }
]
```
- Pagination: If your API implements pagination, responses may include pagination metadata. If not, a plain array is returned.

4) Get specific employee
- URL: `GET /employee/{id}/`
- Description: Retrieve a single employee by ID. Requires Basic Auth.
- Request headers:
  - `Accept: application/json`
  - Authorization: HTTP Basic
- Example curl:
```bash
curl -u user3:user123 -X GET "http://127.0.0.1:8000/employee/2/" \
  -H "Accept: application/json"
```
- Success response:
  - Status: `200 OK`
  - Body (example):
```json
{
  "id": 2,
  "name": "James Wilson",
  "department": "Finance",
  "designation": "Financial Analyst",
  "salary": 80000,
  "email": "j.wilson@company.com",
  "date_of_joining": "2023-05-22"
}
```
- Error responses:
  - `404 Not Found` — employee with given ID does not exist
  - `401 Unauthorized` — invalid/missing auth

5) Update employee
- URL: `PUT /employee/{id}/`
- Description: Replace an employee record. Requires Basic Auth.
- Request headers:
  - `Content-Type: application/json`
  - Authorization: HTTP Basic
- Request body (example):
```json
{
  "name": "David Rodriguez Jose",
  "department": "Engineering",
  "designation": "Cloud Engineer",
  "salary": 105000,
  "email": "david.r@company.com",
  "date_of_joining": "2023-06-20"
}
```
- Example curl:
```bash
curl -u user3:user123 -X PUT "http://127.0.0.1:8000/employee/4/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "David Rodriguez Jose",
    "department": "Engineering",
    "designation": "Cloud Engineer",
    "salary": 105000,
    "email": "david.r@company.com",
    "date_of_joining": "2023-06-20"
  }'
```
- Success response:
  - Status: `200 OK`
  - Body: updated employee object (same shape as GET)
- Error responses:
  - `400 Bad Request` — validation errors
  - `404 Not Found` — no employee with that ID
  - `401 Unauthorized`

6) Delete employee
- URL: `DELETE /employee/{id}/`
- Description: Delete an employee. Requires Basic Auth.
- Request headers:
  - Authorization: HTTP Basic
- Example curl:
```bash
curl -u user3:user123 -X DELETE "http://127.0.0.1:8000/employee/4/"
```
- Success response:
  - Status: `204 No Content` (empty body)
- Error responses:
  - `404 Not Found`
  - `401 Unauthorized`

Field definitions and validation
- id: integer (assigned by server)
- name: string, required
- department: string, required
- designation: string, required
- salary: number (integer or float), required, >= 0
- email: string, required, must be valid email format
- date_of_joining: string, required, format `YYYY-MM-DD` (ISO date)

HTTP Status Summary
- 201 Created — resource successfully created (register, create employee)
- 200 OK — successful GET or successful update (PUT)
- 204 No Content — successful DELETE
- 400 Bad Request — validation errors
- 401 Unauthorized — missing or invalid credentials
- 403 Forbidden — authenticated but not allowed (if applicable)
- 404 Not Found — resource does not exist

Notes and recommendations
- Use `curl -u username:password` or properly encoded `Authorization: Basic` header for Basic Auth.
- Consider adding token-based authentication (JWT or token) for better security in production.
- For partial updates, consider supporting `PATCH /employee/{id}/`.
- Add rate limiting, input sanitization, and strict validation for production use.

