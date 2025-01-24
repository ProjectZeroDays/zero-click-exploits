from backend.app import db

class Adware(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    target_os = db.Column(db.String(255), nullable=False)
    persistence_method = db.Column(db.String(255), nullable=False)
    payload_id = db.Column(db.Integer, db.ForeignKey('payload.id'), nullable=False)
    deployment_method_id = db.Column(db.Integer, db.ForeignKey('deployment_method.id'), nullable=False)
    config = db.Column(db.JSON)

    payload = db.relationship('Payload', backref='adwares')
    deployment_method = db.relationship('DeploymentMethod', backref='adwares')
