from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from main.python.ua.lviv.iot.models.AbstractShoes import AbstractShoes
from main.python.ua.lviv.iot.models.Sex import Sex
import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"])

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Slippers(AbstractShoes, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    size_eur_standard = db.Column(db.Integer, unique=False)
    price_in_uah = db.Column(db.Float, unique=False)
    assignment = db.Column(db.String(32), unique=False)
    sex = db.Column(db.String(32), unique=False)
    brand = db.Column(db.String(32), unique=False)
    color = db.Column(db.String(32), unique=False)
    material_of_vamp = db.Column(db.String(32), unique=False)
    material_of_lining = db.Column(db.String(32), unique=False)
    toecap_type = db.Column(db.String(32), unique=False)
    presence_of_pompom = db.Column(db.Boolean, unique=False)

    def __init__(self, size_eur_standard=39, price_in_uah=200, assignment="home", sex="FEMALE", brand="ZaraHome", color="blue",
                 material_of_vamp="cotton", material_of_lining="cotton", toecap_type="oval", presence_of_pompom=False):
        AbstractShoes.__init__(self, size_eur_standard, price_in_uah, assignment, sex, brand, color, material_of_vamp,
                               material_of_lining, toecap_type)
        self.presence_of_pompom = presence_of_pompom


class SlippersSchema(ma.Schema):
    class Meta:
        fields = ('size_eur_standard', 'price_in_uah', 'assignment', 'sex', 'brand', 'color', 'material_of_vamp',
                  'material_of_lining', 'toecap_type', 'presence_of_pompom', 'id')


slipper_schema = SlippersSchema()
slippers_schema = SlippersSchema(many=True)


@app.route("/slippers", methods=["POST"])
def add_slipper():
    size_eur_standard = request.json['size_eur_standard']
    price_in_uah = request.json['price_in_uah']
    assignment = request.json['assignment']
    sex = request.json['sex']
    brand = request.json['brand']
    color = request.json['color']
    material_of_vamp = request.json['material_of_vamp']
    material_of_lining = request.json['material_of_lining']
    toecap_type = request.json['toecap_type']
    presence_of_pompom = request.json['presence_of_pompom']
    slipper = Slippers(size_eur_standard, price_in_uah, assignment, sex, brand, color, material_of_vamp,
                       material_of_lining, toecap_type, presence_of_pompom)
    db.session.add(slipper)
    db.session.commit()
    return slipper_schema.jsonify(slipper)


@app.route("/slippers", methods=["GET"])
def get_slipper():
    all_slippers = Slippers.query.all()
    result = slippers_schema.dump(all_slippers)
    return jsonify({'slippers': result})


@app.route("/slippers/<id>", methods=["GET"])
def slippers_detail(id):
    slipper = Slippers.query.get(id)
    if not slipper:
        abort(404)
    return slipper_schema.jsonify(slipper)


@app.route("/slippers/<id>", methods=["PUT"])
def slippers_update(id):
    slipper = Slippers.query.get(id)
    if not slipper:
        abort(404)
    old_slipper = copy.deepcopy(slipper)
    slipper.size_eur_standard = request.json['size_eur_standard']
    slipper.price_in_uah = request.json['price_in_uah']
    slipper.assignment = request.json['assignment']
    slipper.sex = request.json['sex']
    slipper.brand = request.json['brand']
    slipper.color = request.json['color']
    slipper.material_of_vamp = request.json['material_of_vamp']
    slipper.material_of_lining = request.json['material_of_lining']
    slipper.toecap_type = request.json['toecap_type']
    slipper.presence_of_pompom = request.json['presence_of_pompom']
    db.session.commit()
    return slipper_schema.jsonify(old_slipper)


@app.route("/slippers/<id>", methods=["DELETE"])
def slippers_delete(id):
    slipper = Slippers.query.get(id)
    if not slipper:
        abort(404)
    db.session.delete(slipper)
    db.session.commit()
    return slipper_schema.jsonify(slipper)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')



