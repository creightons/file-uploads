from database import db
from datetime import datetime

class FileUploads(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    uploaded_date = db.Column(db.DateTime)
    filename = db.Column(db.String(100))

    def __init__(self, filename):
        self.filename = filename
        self.uploaded_date = datetime.utcnow()
