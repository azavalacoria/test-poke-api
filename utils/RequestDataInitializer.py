# name of class RequestDataInitializer
import traceback

class RequestDataInitializer():

    def __init__(self, data: dict= None) -> None:
        self.data = data
    
    def init_string_value(self, key: str = '', default: str = '') -> str:
        string_value = default
        if self.data is not None:
            if key in self.data and self.data[key] is not None:
                if isinstance(self.data[key], str):
                    string_value = self.data[key]
                else:
                    try:
                        string_value = str(self.data[key])
                    except:
                        string_value = ''
                        traceback.print_exc()
        return string_value
    
    def has_key_value(self, key: str) -> bool:
        result = False
        if self.data and key is not None:
            result = True if key in self.data else False
        return result
    
    def get_value(self, key: str = '', default: any = None):
        value = default
        if self.has_key_value(key=key):
            value = self.data[key]
        return value