from flask import Flask, jsonify

''' BEGIN IMPORTS AREA '''
from controllers.PokemonController import pokemons_base_page
''' CLOSE IMPORTS AREA '''

SESSION_TYPE = 'memcache'
app = Flask(__name__, static_folder='/static')

app.register_blueprint(pokemons_base_page)

@app.route('/')
def hello():
    return jsonify({'message': 'hello'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)