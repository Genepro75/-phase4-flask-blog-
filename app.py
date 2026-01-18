import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Database Configuration (Best Practice: Keep credentials in env vars)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# --- Models ---
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

# --- Routes ---
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Phase 4 Flask Blog API", "status": "running"}), 200

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    # Validation
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({"error": "Bad Request", "message": "Username and email are required"}), 400
    
    try:
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Conflict", "message": "User already exists"}), 409
