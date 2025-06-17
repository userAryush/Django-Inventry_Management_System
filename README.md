# 🧾 Inventory Management System API (Django + DRF)

This is a RESTful Inventory Management System built using **Django** and **Django REST Framework**. It provides endpoints for managing product types, products, departments, purchases, and sales. It also includes **user authentication**, **group-based permissions**, and **token-based login/registration**.

---

## 🔧 Tech Stack

- Django
- Django REST Framework (DRF)
- SQLite
- Token Authentication
- Group-based Permissions

---

## 🚀 Features

- 🔐 **User Registration & Login** (Token-based)
- 🧑‍🤝‍🧑 Group Assignment via API
- 📦 **CRUD operations** for:
  - Product Types
  - Products (with filter & search support)
  - Departments
  - Sales
  - Purchases
- 🛡️ Custom permissions for REST actions (GET, POST, PUT, DELETE)

---

## 📁 API Endpoints

| Endpoint | Methods | Description |
|----------|---------|-------------|
| `/register/` | POST | Register a new user |
| `/login/` | POST | Authenticate user & return token |
| `/group/` | GET | List available user groups |
| `/product-type/` | GET, POST | List or create product types |
| `/product-type/<id>/` | GET, PUT, DELETE | Retrieve, update, or delete a product type |
| `/product/` | GET, POST | List or create products (filterable by type/department) |
| `/product/<id>/` | GET, PUT, DELETE | Manage individual product |
| `/department/` | GET, POST | List or create departments |
| `/sell/`, `/purchase/` | Full CRUD on sales and purchases |

---

## 🔐 Authentication

- Implemented **Token-Based Authentication** using Django REST Framework.
- On successful registration or login, a token is generated and returned.
- Include this token in request headers to access protected endpoints:

## 🛂 Permissions

- Only **authenticated users** can access the API.
- **Group-based permissions** restrict access:

  - **Manager** group: Can `POST`, `PUT`, or `DELETE` products.
  - **Viewer** group: Has **read-only** access.

---

## 🧪 Filtering & Searching

- Products can be filtered by `product_type` and `department`:

  ```http
  GET /product/?product_type=1&department=2
---

## 🧑‍🤝‍🧑 Group Assignment via API

- Users can be assigned to groups via the **API** or **Django admin panel**.
- Each group has specific permission levels:

  - **Admin**: Full access
  - **Manager**: Add/update products, view sales and purchases
  - **Viewer**: Read-only access

---

## 📌 Summary

✅ Built with **Django + DRF**  
🔐 Token authentication with **group-based access**  
🧩 Modular **CRUD-based inventory system**  
🔍 Filter and search support for **efficient product lookup**  
👥 **Role-based access** using Django groups
