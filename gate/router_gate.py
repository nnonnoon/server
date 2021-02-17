from flask import Flask, request, jsonify
from  sendApi_gate import sendApi

app = Flask(__name__)

global command
global competition

# initial
command = "initial"
# competition = 1 

@app.route('/command', methods= ['POST'])
def handdle_command():
    try:
        while(True): 
            data = request.get_json()
            command = data['command']
            competition = data['competition']

            print("command is : ", competition )
            print("command is : ", command )

            if command == "initial":
                continue
            elif command == "start" :
                sendApi(competition)
                import initial
            elif command == "end" : 
                print("endddddd")
            else:
                print('COME')

            return jsonify({'message' : 'RECEIVED!!'}), 200
    except:
        return jsonify({'message' : 'FAILED!!'}), 400

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True, port=5001)

