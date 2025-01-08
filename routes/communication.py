from flask import Blueprint, request, jsonify
from models.interaction import Interaction

communication_bp = Blueprint('communication', __name__)

@communication_bp.route('/send', methods=['POST'])
@jwt_required()
def send_communication():
    data = request.get_json()
    interaction = Interaction(
        user_id=get_jwt_identity(),
        type=data['type'],
        subject=data['subject'],
        content=data['content']
    )
    db.session.add(interaction)
    db.session.commit()
    return jsonify({'message': 'Communication sent'})
