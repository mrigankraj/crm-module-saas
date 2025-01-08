from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    contact_person = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    industry = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    onboarding_status = db.Column(db.String(50), default='pending')
    subscription_tier = db.Column(db.String(50), default='basic')
    
    # Relationships
    tasks = db.relationship('Task', backref='user', lazy=True)
    interactions = db.relationship('Interaction', backref='user', lazy=True)
    analytics = db.relationship('Analytics', backref='user', lazy=True)
    communication_preferences = db.relationship('CommunicationPreferences', 
                                             backref='user', 
                                             lazy=True, 
                                             uselist=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'email': self.email,
            'contact_person': self.contact_person,
            'phone': self.phone,
            'industry': self.industry,
            'created_at': self.created_at.isoformat(),
            'onboarding_status': self.onboarding_status,
            'subscription_tier': self.subscription_tier
        }
