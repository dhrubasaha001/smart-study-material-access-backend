from flask import Blueprint, request, jsonify
import requests
from dotenv import load_dotenv
import os

load_dotenv()

routes = Blueprint("routes", __name__)

FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")

@routes.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True)
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "status": "error",
            "error": "Missing email or password"
        }), 400

    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    try:
        res = requests.post(url, json=payload)
        res_data = res.json()

        if "error" in res_data:
            error_msg = res_data["error"].get("message", "Authentication failed")
            return jsonify({
                "status": "error",
                "error": error_msg
            }), 401

        return jsonify({
            "status": "success",
            "msg": "Login successful",
            "uid": res_data.get("localId"),
            "idToken": res_data.get("idToken"),
            "email": res_data.get("email")
        }), 200

    except requests.exceptions.RequestException as e:
        return jsonify({
            "status": "error",
            "error": f"Request error: {str(e)}"
        }), 500
    except Exception as e:
        return jsonify({
            "status": "error",
            "error": f"Server error: {str(e)}"
        }), 500
