from flask import Flask
from flask_cors import CORS
from routes import routes  # your fixed routes.py

app = Flask(__name__)
CORS(app)  

app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
