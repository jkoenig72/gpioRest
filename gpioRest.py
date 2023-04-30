import subprocess
from flask import Flask, request
from flask_restful import Resource, Api

gpioRest = Flask(__name__)
api = Api(gpioRest)

data_storage = {
    "1": "out",
    "11": "out",
}


for key, value in data_storage.items():
    #print(f"{key}: {value}")
    result = subprocess.run(["gpio", "mode", key, value], capture_output=True, text=True)
    


class DataResource(Resource):
    def get(self, key):
        if key in data_storage:
            #print(type(key))
            result = subprocess.run(["gpio", "read", key], capture_output=True, text=True)
            result = result.stdout.strip()
            return {"value": result}
        else:
            return {"error": "Key not found"}, 404

    def put(self, key):
        value = request.form.get("value")
        if value:
            #print(type(key))
            #print(type(value))
            result = subprocess.run(["gpio", "write", key, value], capture_output=True, text=True)
            result = result.stdout.strip()
            return {"value": value}
        else:
            return {"error": "Missing value parameter"}, 400

api.add_resource(DataResource, "/gpio/<string:key>")

if __name__ == "__main__":
    gpioRest.run(debug=False, host='0.0.0.0', port=9090)
