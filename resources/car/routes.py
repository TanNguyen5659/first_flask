from flask import request
from app import app

from db import cars


@app.route('/cars')
def get_cars():
    return {
        'cars' : list(cars.values())
    }
    
@app.route('/cars/<int:id>')
def get_ind_car(id):
    if id in cars:
        return {
            'car' : cars[id]
        }
    return {
        'OU OH, something went wrong' : 'Invalid car id'
    }

@app.route('/car', methods = ["POST"])
def create_car():
    data = request.get_json()
    cars[data["id"]] = data
    return {
        'car created successfully' : cars[data["id"]]
    }    

@app.route('/car', methods = ["PUT"])
def update_car():
    data=request.get_json()
    if data['id'] in cars:
        cars[data['id']] = data
        return {
            'car updated' : cars[data["id"]]
        }
    return {
        'err' :'err'
    }

@app.route('/car', methods = ["DELETE"])
def delete_car():
    data=request.get_json()
    if data['id'] in cars:
        del cars[data["id"]]
        return {
            'car deleted' : f"{data['make']} is no more...."
        }
    return {
        'err' :"can't delete that car that they aren't there"
    }
