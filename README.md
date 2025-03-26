# Restaurant Menu Management API

## 📌 Overview
This is a **FastAPI-based RESTful API** for managing restaurant menus. It provides endpoints for restaurant owners to create and manage menus, handle extras, and process orders efficiently.

## 🚀 Features
- **JWT Authentication** for secure access.
- **CRUD operations** for Restaurants, Menus, and Extras.
- **One-to-Many & Many-to-Many Relationships** for proper menu structuring.
- **CORS support** to allow frontend integration.
- **Database persistence** using PostgreSQL with SQLAlchemy ORM.

## 🏗️ Project Structure
```
api/
 ├── routers/        # Route handlers (CRUD + Endpoints)
 │   ├── restaurant.py
 │   ├── menu.py
 │   ├── auth.py
 │   └── extras.py
 |   ├── table.py
 ├── models/         # Database models
 │   ├── restaurant.py
 │   ├── menu.py
 │   ├── extras.py
 │   ├── order.py
 │   ├── user.py
 │   ├── table.py
 |   ├── base.py
 ├── schemas/        # Pydantic schemas for validation
 │   ├── restaurant.py
 │   ├── menu.py
 │   ├── extras.py
 │   ├── order.py
 │   ├── user.py
 ├── services/       # Business logic for database operations
 │   ├── restaurant.py
 │   ├── menu.py
 │   ├── extras.py
 │   ├── order.py
 │   ├── user.py
 |   ├── 
 ├── core/           # Configuration & database setup
 │   ├── config.py
 │   ├── database.py
 ├── main.py         # FastAPI app entry point
 ├── requirements.txt # Dependencies
 ├── .env            # Environment variables
 ├── README.md       # Project documentation
```

### Installation and Collaboration
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/restaurant-menu-api.git
cd proj-menucard
```

### **2️⃣ Create and Activate a Virtual Environment**
```sh
# On Windows\python -m venv venv
venv\Scripts\activate

# On Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file and define the following:
```ini
DATABASE_URL=postgresql://user:password@localhost:5432/restaurant_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### **5️⃣ Run Database Migrations**
```sh
alembic upgrade head  # If using Alembic for migrations
```

### **6️⃣ Start the Application**
```sh
uvicorn main:app --reload
```
### Contributing to the Project

Create a new branch for your feature or fix:
```git checkout -b feature-branch-name```

Make changes and commit them:
```git add . ``` 
```git commit -m "Describe your changes"```

Push your branch to GitHub:
``` git push origin feature-branch-name ```

Create a Pull Request on GitHub and request a review.

### API Endpoints
### **Authentication**
- `POST /auth/register` → Register a new user
- `POST /auth/login` → Authenticate and get JWT token

### **Restaurants**
- `POST /restaurants/` → Create a restaurant
- `GET /restaurants/` → Get all restaurants
- `GET /restaurants/{id}` → Get a restaurant by ID
- `PUT /restaurants/{id}` → Update a restaurant
- `DELETE /restaurants/{id}` → Delete a restaurant

### **Menus**
- `POST /menus/` → Add a new menu item linked to a restaurant
- `GET /menus/` → Retrieve all menu items
- `PUT /menu/{id}` → Update a menu
- `DELETE /menu/{id}` → Delete a menu

### **Extras** 
- `POST /extras/` → Add a new extra item linked to a specific menu
- `GET /extras/` → Retrieve all extras
- `PUT /extras/{id}` → Update an extra
- `DELETE /extras/{id}` → Delete an extra

### **Table** 
- `POST /table/` → Add a new table linked to a specific restaurant
- `GET /table/` → Retrieve all table
- `PUT /table/{id}` → Update a table
- `DELETE /table/{id}` → Delete a table

### **Orders**
- `POST /orders/` → Create an order with selected menu & extras
- `GET /orders/` → View all orders

## 📌 Testing the API
You can test the API using **Postman**, **cURL**, or visit the auto-generated Swagger UI:
```
http://127.0.0.1:8000/docs 
```

### Authentication
Authentication is handled using JWT tokens. Ensure to include an Authorization: Bearer <token> header for protected routes

