import os
from flask import Flask
from flask_cors import CORS
from routes import routes  # your fixed routes.py

app = Flask(__name__)
CORS(app)  

# Register routes
app.register_blueprint(routes)

# Use PORT environment variable (Render sets this)
port = int(os.getenv("PORT", 5000))
debug = os.getenv("DEBUG", "False").lower() == "true"

if __name__ == "__main__":
    print(f"Starting Flask server on port {port}, debug={debug}")
    app.run(
        host="0.0.0.0",  
        port=port,
        debug=debug
    )
