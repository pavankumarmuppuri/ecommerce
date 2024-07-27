# E-Commerce Website

## Overview

Welcome to the E-Commerce Website project. This is a web application built using Flask, SQLAlchemy, and Bootstrap, providing users with a platform to browse products, register, login, and manage their profile.

## Features

### User Authentication
- **Register**: Users can create a new account by providing their first name, last name, email, and password.
- **Login**: Registered users can log in to access their dashboard.
- **Logout**: Users can log out of their accounts.

### Dashboard
- **Product Listings**: Users can view a list of products, including product images, names, prices, and descriptions.
- **Product Filtering**: Products can be filtered by category and searched by title.
- **Product Details**: Clicking on a product takes users to a detailed view of that product.
- **Add to Cart**: Users can add products to their cart from the product listing page.
- **Cart Navigation**: Users can view their cart from the navbar and navigate to the cart page.

### Profile Management
- **Edit Profile**: Users can update their first name and last name.

### Responsive Design
- **Mobile Friendly**: The application is designed to be responsive and usable on various devices.

## Installation

### Prerequisites
- Python 3.x
- PostgreSQL

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/username/repo.git
   cd repo

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Set Up the Database**

Create a PostgreSQL database named ecommerce.
Configure the database URI in app.py with your database credentials.

5. **Run Database Migrations**

   ```bash
   flask db init
   flask db migrate
   flask db upgrade

6. **Run the Application**

   ```bash
   python app.py

### Configuration

Update app.py with the following placeholders:

<b>SECRET_KEY:</b> Replace 'your_secret_key' with a secure random key.<br>
<b>SQLALCHEMY_DATABASE_URI:</b> Replace with your PostgreSQL credentials.

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/ecommerce'

### File Structure
<li>app.py: Main application script.</li>
<li>templates/: Directory containing HTML templates.</li>
<li>static/: Directory for static files such as CSS, JavaScript, and images.</li>
<li>migrations/: Directory for database migration scripts.</li>
<li>requirements.txt: List of Python dependencies.</li>

### Example Data Files
products.json: Contains product data with fields like id, name, year, price, categories, brand, description, and imageUrl.
