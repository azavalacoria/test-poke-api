import traceback
import requests

from utils.RequestDataInitializer import RequestDataInitializer


class PokemonAbility():
    __base_url = 'https://pokeapi.co/api/v2/pokemon'
    def __init__(self) -> None:
        pass

    def list(self, pokemon: str = ''):
        data: list = None
        result = requests.get('{}/{}'.format(self.__base_url, pokemon))
        code = 0
        if result.status_code == 200:
            try:
                rdi = RequestDataInitializer(data=result.json())
                ab: list = rdi.get_value(key='abilities')
                if isinstance(ab, list):
                    data = []
                    for item in ab:
                        r = RequestDataInitializer(data=item)
                        a = r.get_value(key='ability')
                        if isinstance(a, dict):
                            data.append(a)
                code = result.status_code
            except:
                traceback.print_exc()
                code = 500
        else:
            code = result.status_code
        return code, data
