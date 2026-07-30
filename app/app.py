from flask import Flask
from app.routes.main import main_bp
import os

app = Flask(__name__)
app.register_blueprint(main_bp)

# DAST: Sensitive Information Exposure (Debug Mode)
if __name__ == '__main__':
    # Flask Debug mode enabled is a SAST finding
    app.run(host='0.0.0.0', port=5000, debug=True)
