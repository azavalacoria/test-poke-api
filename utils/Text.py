class TextValidation():    
    def not_empty(self, string: str = None) -> bool:
        if isinstance(string, str) and len(string) > 0:
            if len(string.strip()) > 0:
                return True
            else:
                return False
        else:
            return False