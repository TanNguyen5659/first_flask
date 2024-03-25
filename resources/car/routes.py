from flask import request
from flask.views import MethodView
from uuid import uuid4
from flask_smorest import abort

from schemas import CarSchema
from . import bp

from db import cars
from models.car_model import CarModel

@bp.route('/car/')
class CarList(MethodView):
    
    @bp.response(200, CarSchema(many=True))
    def get(self):
        return CarModel.query.all()

    
    @bp.arguments(CarSchema)
    @bp.response(201, CarSchema)
    def post(self, data):
        try:
            car = CarModel()
            car.from_dict(data)
            car.save_car()
            return {
                'message' : f'car {data["carmake"]}'}, 201
        except:
            return {
                'error' : "car make already taken, please try a different one!"
            }, 400
        

@bp.route('/car/<int:id>')
class Car(MethodView):
    
    @bp.response(200, CarSchema)
    def get(self, id):
        car = CarModel.query.get(id)
        if car:
            return car
        else:
            abort(400, message="not a valid car")


    @bp.arguments(CarSchema)
    def put(self, data, id):
        car = CarModel.query.get(id)
        if car:
            car.from_dict(data)
            car.save_car()
            return { "message": "car updated"}, 200
        else:
            abort(400, message="not a valid car")          


    def delete(self, id):
        car = CarModel.query.get(id)
        if car:
            car.del_car()
            return { "message": "car GONE GONE GONE"}, 200
        abort(400, message="not a valid car")
        
        # if id in cars:
        #     del cars[id]
        #     return { 'car gone': f" is no more. . . " }, 202
        # return { 'err' : "can't delete that car they aren't there. . . " } , 400

