from flask import Blueprint, jsonify
from models.interaction import Interaction
from sqlalchemy import func

analytics_bp = Blueprint('analytics', __name__)

@analytics_bp.route('/engagement', methods=['GET'])
@jwt_required()
def get_engagement_metrics():
    user_id = get_jwt_identity()
    interactions = Interaction.query.filter_by(user_id=user_id).all()
    return jsonify({
        'total_interactions': len(interactions),
        'types': db.session.query(
            Interaction.type, 
            func.count(Interaction.id)
        ).filter_by(user_id=user_id).group_by(Interaction.type).all()
    })
