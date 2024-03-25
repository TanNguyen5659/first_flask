from app import db

from werkzeug.security import generate_password_hash, check_password_hash



class CarModel(db.Model):
    
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key = True)
    carmake = db.Column(db.String(50))
    dealer = db.Column(db.String(50))
    model= db.Column(db.String(75))

    def save_car(self):
        db.session.add(self)
        db.session.commit()

    def del_car(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, car_dict):
        for k , v in car_dict.items():
            setattr(self, k, v)
            # else:
            #     setattr(self, 'password_hash', generate_password_hash(v))




    # id = fields.Str(dump_only=True)
    # username = fields.Str(required=True)
    # email = fields.Str(required=True)
    # password = fields.Str(required=True, load_only = True)
    # first_name= fields.Str()
    # last_name= fields.Str()


