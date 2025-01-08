from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User
from models.tasks import Task
from utils.email_utils import send_welcome_email
from app import db

onboarding_bp = Blueprint('onboarding', __name__)

@onboarding_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Check if user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email already registered'}), 400
    
    # Create new user
    user = User(
        company_name=data['company_name'],
        email=data['email'],
        contact_person=data['contact_person'],
        phone=data.get('phone'),
        industry=data.get('industry')
    )
    user.set_password(data['password'])
    
    # Create initial onboarding tasks
    tasks = [
        Task(user=user, title='Complete Company Profile', priority='high'),
        Task(user=user, title='Set Communication Preferences', priority='medium'),
        Task(user=user, title='Schedule Welcome Call', priority='high'),
        Task(user=user, title='Review Product Documentation', priority='medium')
    ]
    
    try:
        db.session.add(user)
        db.session.add_all(tasks)
        db.session.commit()
        
        # Send welcome email
        send_welcome_email(user.email, user.contact_person)
        
        return jsonify({
            'message': 'Registration successful',
            'user': user.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@onboarding_bp.route('/progress', methods=['GET'])
@jwt_required()
def get_onboarding_progress():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    
    tasks = Task.query.filter_by(user_id=user_id).all()
    completed_tasks = sum(1 for task in tasks if task.status == 'completed')
    total_tasks = len(tasks)
    
    return jsonify({
        'progress': (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0,
        'completed_tasks': completed_tasks,
        'total_tasks': total_tasks,
        'tasks': [task.to_dict() for task in tasks]
    })

@onboarding_bp.route('/update-status', methods=['PUT'])
@jwt_required()
def update_onboarding_status():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    
    data = request.get_json()
    user.onboarding_status = data.get('status', user.onboarding_status)
    
    try:
        db.session.commit()
        return jsonify({'message': 'Status updated successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
