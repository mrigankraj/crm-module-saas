from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from config import config

# Initialize Flask application
app = Flask(__name__)
app.config.from_object(config)

# Configure CORS
CORS(app)

# Initialize JWT
jwt = JWTManager(app)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Register blueprints
from routes.onboarding import onboarding_bp
from routes.communication import communication_bp
from routes.analytics import analytics_bp

app.register_blueprint(onboarding_bp, url_prefix='/api/onboarding')
app.register_blueprint(communication_bp, url_prefix='/api/communication')
app.register_blueprint(analytics_bp, url_prefix='/api/analytics')

@app.route('/health')
def health_check():
    return {'status': 'healthy'}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=config.DEBUG)
