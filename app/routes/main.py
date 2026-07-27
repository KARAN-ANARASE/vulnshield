from flask import Blueprint, request, render_template, render_template_string, send_file
from app.models.user import UserModel
from app.services.system import SystemService
import os

main_bp = Blueprint('main', __name__)
user_model = UserModel()
system_service = SystemService()

@main_bp.route('/')
def index():
    # DAST: Reflected XSS
    name = request.args.get('name', 'Guest')
    return render_template('index.html', name=name)

@main_bp.route('/search')
def search():
    # DAST: SQL Injection via URL parameter
    query = request.args.get('q', '')
    user = user_model.get_user(query)
    return f"Search Result: {user}"

@main_bp.route('/ping')
def ping():
    # DAST: Command Injection via URL parameter
    target = request.args.get('target', 'google.com')
    result = system_service.check_host(target)
    return f"<pre>{result}</pre>"

@main_bp.route('/profile/<int:user_id>')
def profile(user_id):
    # DAST: IDOR (Insecure Direct Object Reference)
    # No authentication or authorization check
    return f"User Profile for ID: {user_id}"

@main_bp.route('/download')
def download():
    # DAST: Path Traversal
    filename = request.args.get('file', 'info.txt')
    return send_file(os.path.join('static', filename))

@main_bp.route('/calc')
def calc():
    # DAST: Dangerous Eval
    formula = request.args.get('formula', '1+1')
    result = system_service.run_calculation(formula)
    return f"Result: {result}"
