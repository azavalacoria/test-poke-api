from http import HTTPStatus
from flask import Blueprint, jsonify, request

from src.business.PokemonAbility import PokemonAbility
from utils.RequestDataInitializer import RequestDataInitializer
from utils.Text import TextValidation

root = '/api/v1/pokemons'
pokemons_base_page = Blueprint('pokemons_base_page', __name__, template_folder='/static')

@pokemons_base_page.route(root)
def action_list_all():
    return jsonify('UNIMPLEMENTED'), HTTPStatus.NOT_IMPLEMENTED

@pokemons_base_page.route(root + '/<name>/abilities', methods=['GET'])
def action_list_pokemon_abilities(name: str = ''):
    response_data = None
    response_code = HTTPStatus.NOT_ACCEPTABLE

    # rdi = RequestDataInitializer(data=request.args.to_dict())
    tv = TextValidation()

    # name = rdi.init_string_value(key='name')

    if tv.not_empty(string=name):
        print('pokemon name -> {}'.format(name))
        code, abilities = PokemonAbility().list(pokemon=name.lower())
        if code == HTTPStatus.OK:
            response_data = {'abilities': abilities}
            response_code = code
        else:
            response_code = code
            response_data = 'Pokemon name not found'
    else:
        response_data = 'Pokemon name is need to search'
        response_code = HTTPStatus.BAD_REQUEST

    return jsonify(response_data), response_code