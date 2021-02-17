from flask import Flask, request, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db, Logging
import time
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/running'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()
migrate = Migrate(app, db)

CORS(app)

global competition_index

@app.route('/logging', methods= ['POST'])
def handle_logging():
    try:
        data = request.get_json()
        print(competition_index)
        new_logging = Logging(competition_index = competition_index , gate_id = data['gate_id'], tag_number = data['tag_number'], timestamp = data['timestamp'])
        db.session.add(new_logging)
        db.session.commit()
        return jsonify({'message' : 'RECEIVED!!'}), 200
    except:
        return jsonify({'message' : 'FAILED!!'}), 400


# @app.route('/command', methods= ['POST'])
# def handle_command():
#     url = 'http://raspberrypi.local:5000/command'

#     data = request.get_json()
#     payload = {}
#     payload["competition"] = data["competition"]
#     payload["command"] = data["command"]

#     print(payload)

#     while(True): 
#         try :
#             response = requests.post(url, json = payload)

#             if response.ok == True:
#                 return response.json()['message']
#                 break
#             else:
#                 return response.json()['message']
#         except(err):
#             # print(err)  
#             return jsonify({'message' : "Disconnect"}), 400

@app.route('/start', methods= ['POST'])
def handle_start():
    try:
        data = request.get_json()
        competition_index = data["competition"]
        return jsonify({'message' : 'START!!'}), 200
    except(err):
        print(err)
        return jsonify({'message' : 'FAILED!!'}), 400

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True, port=5000)