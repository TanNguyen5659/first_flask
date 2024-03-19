from flask import Flask, request

app = Flask(__name__)

cars = {
    1:{
        'id' : 1,
        'make': 'Tesla',
        'model' : 'S'
    },
    2:{
        'id' : 2,
        'make': 'Tesla',
        'model' : 'Cybertruck'
    },
    3:{
        'id' : 3,
        'make': 'Rivian',
        'model' : 'R1S'
    }
}

@app.route('/')
def land():
    return {
        "you've officially landed!" : "from run.py"
    }

@app.route('/cars')
def get_cars():
    return {
        'cars' : list(cars.values())
    }
    
@app.route('/cars/<int:id>')
def get_ind_user(id):
    if id in cars:
        return {
            'car' : cars[id]
        }
    return {
        'OU OH, something went wrong' : 'Invalid car id'
    }

@app.route('/car', methods = ["POST"])
def create_user():
    data = request.get_json()
    cars[data["id"]] = data
    return {
        'car created successfully' : cars[data["id"]]
    }    

@app.route('/car', methods = ["PUT"])
def update_user():
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
def delete_user():
    data=request.get_json()
    if data['id'] in cars:
        del cars[data["id"]]
        return {
            'car deleted' : f"{data['make']} is no more...."
        }
    return {
        'err' :"can't delete that user that they aren't there"
    }

    

