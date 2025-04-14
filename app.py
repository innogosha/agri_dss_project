from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import random

app = Flask(__name__)

# Initialize Firebase
cred = credentials.Certificate('firebase-key.json')  # Path to your service account key
firebase_admin.initialize_app(cred)
db = firestore.client()

# Route to render homepage
@app.route('/')
def index():
    return render_template('index.html')

# Recommendation logic API
@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    location = data.get('location')
    soil_type = data.get('soil_type')
    user_email = data.get('email', 'anonymous')

    # Sample crop recommendations
    crop_recommendations = {
        'clay': ['Maize', 'Cassava', 'Beans'],
        'sandy': ['Groundnuts', 'Watermelon', 'Onions'],
        'loam': ['Rice', 'Bananas', 'Tomatoes']
    }

    # Sample irrigation advice
    irrigation_recommendations = {
        'clay': 'Low frequency, high volume',
        'sandy': 'High frequency, low volume',
        'loam': 'Moderate frequency and volume'
    }

    # Sample fertilization guidance
    fertilization_recommendations = {
        'clay': 'Add compost and organic matter',
        'sandy': 'Use nitrogen-rich fertilizers frequently',
        'loam': 'Balanced NPK fertilizer recommended'
    }

    result = {
        'location': location,
        'soil_type': soil_type,
        'recommended_crops': crop_recommendations.get(soil_type.lower(), ['Maize']),
        'irrigation': irrigation_recommendations.get(soil_type.lower(), 'Use local advisory'),
        'fertilization': fertilization_recommendations.get(soil_type.lower(), 'Use soil test results'),
        'user_email': user_email
    }

    # Store in Firebase Firestore
    db.collection('recommendations').add(result)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
