from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Placeholder for the secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/your_database'  # Placeholder for the database URIapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email address already exists')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('login'))
        
        session['user_id'] = user.id
        flash('Logged in successfully!')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'user_id' not in session:
        flash('You need to login first.')
        return redirect(url_for('login'))

    with open(os.path.join(app.root_path, 'products.json')) as f:
        products_data = json.load(f)

    categories = [
        "Electronics", "Fashion", "Home & Kitchen", "Beauty & Personal Care", 
        "Sports & Outdoors", "Books", "Toys & Games", "Automotive", 
        "Health & Wellness", "Baby Products", "Pet Supplies", "Office Supplies", 
        "Grocery & Gourmet Food", "Jewelry", "Shoes", "Furniture", "Garden & Outdoor", 
        "Tools & Home Improvement", "Music & Instruments", "Arts & Crafts", 
        "Travel Accessories"
    ]

    selected_category = request.form.get('category') if request.method == 'POST' else None

    if selected_category:
        filtered_products = [product for product in products_data['products'] if selected_category in product['categories']]
    else:
        filtered_products = products_data['products']

    user = db.session.get(User, session['user_id'])
    return render_template('dashboard.html', user=user, categories=categories, products=filtered_products)

@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = db.session.get(User, session['user_id'])
    
    if request.method == 'POST':
        user.first_name = request.form['first_name']
        user.last_name = request.form['last_name']
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('edit_profile.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
