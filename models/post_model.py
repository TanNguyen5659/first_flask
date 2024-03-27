from app import db
from datetime import datetime

class PostModel(db.Model):

    __table__name = 'posts'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.DateTime, default = datetime.utcnow)
    # author points to car model as car will be author
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'), nullable = False)
    author = db.relationship("CarModel", back_populates = 'posts')

    def save_post(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, a_dict):
        
        self.title = a_dict['title']
        setattr(self, 'body', a_dict['body'])
        setattr(self, 'car_id', int(a_dict['car_id']))

    # id = fields.Str(dump_only=True)
    # title = fields.Str()
    # body = fields.Str(required=True)
    # author = fields.Int(required=True)
        
    