from flask import Flask
from flask_cors import CORS
from routes import routes  # your fixed routes.py

app = Flask(__name__)
CORS(app)  

app.register_blueprint(routes)

if __name__ == "__main__":
    aport = int(os.getenv('PORT', 5000))
    debug = os.getenv('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting Flask server on port {port}")
    logger.info(f"Debug mode: {debug}")
    
    app.run(
        host='0.0.0.0',  
        port=port,
        debug=debug
    )
