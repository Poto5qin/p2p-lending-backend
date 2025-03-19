from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend to call API

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.p2p_lending  # Database name

# API Route: Test if server is running
@app.route("/")
def home():
    return jsonify({"message": "Backend is running!"})

if __name__ == "__main__":
    app.run(debug=True)  # Run server
