from flask import Flask, request, jsonify 
#from flask_api import FlaskAPI, status, exceptions
import json
import os

#app = FlaskAPI(__name__)
app = Flask(__name__)


@app.route("/", methods=['GET'])
def notes_list():
    if request.headers.get('Autorization')=='42':        
    
        data = request.get_json()        
        return jsonify(data)
                
        #return data, status.HTTP_201_CREATED
        
    else:
        return jsonify({'messagem':'Você não está autorizado'})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(debug=True)