from flask import Flask, request, render_template, jsonify
import argparse
import requests
import os
import sys
dir = os.path.dirname
src_path = dir(dir(__file__))
sys.path.append(src_path)
from dashboard.apis_tb import read_json
from flask import send_from_directory


# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------
@app.route("/")  # @ --> esto representa el decorador de la función
def home():
    """ Default path """
    #return app.send_static_file('greet.html')
    return "Waste_Management_EDA_proyect"


# localhost:6060/token_id?token_id=Y4290783D
@app.route('/token_id', methods=['GET'])                                                                                                                                                                          
def give_tokenid():
    s = request.args['token_id']
    json_file = read_json(fullpath=settings_json)
    if s == "Y4290783D":
        return json_file
    else:
        return "Wrong password"
     
settings_json = dir(dir(os.path.dirname(__file__))) + os.sep + 'reports' + os.sep + "waste_management_cleaned.json"


@app.route("/recibe_informacion")
def recibe_info():
    pass 

#---------- Other functions ----------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-x", "--x", type=int, help="the argument", required=True)
    args = vars(parser.parse_args())
    argument = args["x"]



    #argument =  input('Insert an argument to start the process')
    if argument == 8642:

        print("---------STARTING PROCESS---------")
        print(__file__)
        
        # Get the settings fullpath
        # \\ --> WINDOWS
        # / --> UNIX
        # Para ambos: os.sep
        settings_file = os.path.dirname(__file__) + os.sep + "settings.json"
        print(settings_file)
        # Load json from file
        json_readed = read_json(fullpath=settings_file)
        
        # Load variables from jsons
        DEBUG = json_readed["debug"]
        HOST = json_readed["host"]
        PORT_NUM = json_readed["port"]
        # Dos posibilidades:
        # HOST = "0.0.0.0"
        # HOST = "127.0.0.1"  --> localhost
        app.run(debug=DEBUG, host=HOST, port=PORT_NUM)
    else:
        print('wrong password')

if __name__ == "__main__":
    main()