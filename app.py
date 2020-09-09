from flask import Flask, jsonify
from flask import request
from flask_cors import CORS, cross_origin
import os.path
import ast
import json
import pandas as pd

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app, resources={r'/*': {"origins": "*"}})


@app.route('/get_competitors')
@cross_origin(supports_credentials=True)
def get_competitors():
    with open('data/enemies.json') as f:
        load_data = f.read()
    return load_data


@app.route('/get_buildings')
@cross_origin(supports_credentials=True)
def get_buildings():
    with open('data/moscow_buildings.json') as f:
        load_data = json.load(f)
    return load_data


@app.route('/get_schools')
@cross_origin(supports_credentials=True)
def get_schools():
    with open('data/moscow_school.json') as f:
        load_data = json.load(f)
    return load_data


@app.route('/get_ratings')
@cross_origin(supports_credentials=True)
def get_ratings():
    with open('data/corr_ratings.json') as f:
        load_data = f.read()
    return load_data


def convert_map_to_json():
    df = pd.read_csv('data/school_data.csv', error_bad_lines=False)
  #  df = df.drop(columns='is_moscow')
    res = df.to_json(orient='index')
    res = json.loads(res)

  #  for i in res:
  #      res[i]['coords'] = ast.literal_eval(res[i]['coords'])
  #      res[i]['center'] = ast.literal_eval(res[i]['center'])

    with open('data/moscow_school.json', 'w') as f:
        print(json.dumps(res), file=f)

if __name__ == '__main__':
    app.run()
