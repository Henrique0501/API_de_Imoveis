from flask import Blueprint, request, make_response, jsonify
from app.database import db
from app.imovel_model import Imovel, ImovelSchema
from sqlalchemy.sql import and_
import requests
from flask_jwt_extended import jwt_required

api_localidades = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/distritos').json()
lista_localidades = [loc['nome'] for loc in api_localidades]

api = Blueprint("api_imoveis", __name__, url_prefix='/api/imoveis')


@api.route('/search', methods=['GET'])
def search():

    query = request.args

    place = query.get("place", type=str)

    id = query.get('id', type=int)
    area = query.get('area', type=int)
    area_bg_th = query.get('area_bg_th', type=int)
    area_sm_th = query.get('area_sm_th', type=int)

    rooms = query.get("rooms", type=int)
    rooms_bg_th = query.get('rooms_bg_th', type=int)
    rooms_sm_th = query.get('rooms_sm_th', type=int)

    garages = query.get('garages', type=int)
    garages_bg_th = query.get('garages_bg_th', type=int)
    garages_sm_th = query.get('garages_sm_th', type=int)

    price = query.get('price', type=float)
    price_bg_th = query.get('price_bg_th', type=float)
    price_sm_th = query.get('price_sm_th', type=float)

    list_equal = [Imovel.all_or_equal(Imovel.id, id),
                  Imovel.all_or_equal(Imovel.place, place),
                  Imovel.all_or_equal(Imovel.area, area),
                  Imovel.all_or_equal(Imovel.rooms, rooms),
                  Imovel.all_or_equal(Imovel.garages, garages),
                  Imovel.all_or_equal(Imovel.price, price)
                  ]

    list_bigger = [Imovel.all_or_bigger(Imovel.area, area_bg_th),
                   Imovel.all_or_bigger(Imovel.rooms, rooms_bg_th),
                   Imovel.all_or_bigger(Imovel.garages, garages_bg_th),
                   Imovel.all_or_bigger(Imovel.price, price_bg_th)
                   ]

    list_smaller = [Imovel.all_or_smaller(Imovel.area, area_sm_th),
                    Imovel.all_or_smaller(Imovel.rooms, rooms_sm_th),
                    Imovel.all_or_smaller(Imovel.garages, garages_sm_th),
                    Imovel.all_or_smaller(Imovel.price, price_sm_th)
                    ]

    list_conditions = list_equal + list_bigger + list_smaller

    im = ImovelSchema(many=True)
    resp_obj = Imovel.query.filter(and_(*list_conditions)).all()
    resp_dict = im.dump(resp_obj)
    resp_json = jsonify({'count': len(resp_dict), 'imoveis': resp_dict})
    return make_response(resp_json, 200)


@api.route('/register', methods=['POST'])
@jwt_required()
def register():
    body = request.json

    place = body['place']

    if place not in lista_localidades:
        resp = make_response(jsonify({'message': 'invalid location',
                                      'valid_locations': lista_localidades}),
                             404)
        return resp

    list_ids = [imovel.id for imovel in Imovel.query.all()]

    if 'id' in body and body['id'] in list_ids:
        resp = make_response(jsonify({'message': f"O id {body['id']} já está sendo usado. "
                                                 f"Para evitar esse erro, você pode enviar o body sem um id."}),
                             422)
        return resp

    im = ImovelSchema()
    body_obj = im.load(body)
    db.session.add(body_obj)
    db.session.commit()
    resp = make_response(jsonify(body), 200)
    return resp


@api.route('/update/<int:id>', methods=['PUT'])
@jwt_required()
def update(id):
    update_imovel = Imovel.query.filter_by(id=id).first()

    if not update_imovel:
        return make_response(jsonify({'message': f'O imóvel {id} não existe.'}), 404)

    body_json = request.json

    update_imovel.place = body_json['place']
    update_imovel.area = body_json['area']
    update_imovel.rooms = body_json['rooms']
    update_imovel.garages = body_json['garages']
    update_imovel.price = body_json['price']

    if body_json['place'] not in lista_localidades:
        resp = make_response(jsonify({'message': 'invalid location',
                                      'valid_locations': lista_localidades}),
                             404)
        return resp


    db.session.commit()

    im = ImovelSchema()
    resp_dic = im.dump(update_imovel)

    return make_response(jsonify(resp_dic), 200)


@api.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete(id):
    delete_imovel = Imovel.query.filter_by(id=id).first()

    if not delete_imovel:
        return make_response(jsonify({'message': f'O imóvel {id} não existe.'}), 404)

    db.session.delete(delete_imovel)
    db.session.commit()

    resp = make_response(jsonify({'message': f'Imóvel {id} deletado com sucesso.'}), 200)

    return resp
