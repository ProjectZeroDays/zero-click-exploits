from backend.app import db

class DeploymentMethod(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    config_schema = db.Column(db.JSON)
