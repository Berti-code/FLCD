import re


class ConstantValidator:
    def is_valid(self, string):
        return re.search('^(0|[+-]?[1-9][0-9]*)$', string) is not None


class IdentifierValidator:
    def is_valid(self, string):
        identifier = re.search(r"^[a-zA-Z]([a-zA-Z]|[0-9]){,20}$", string)
        if identifier:
            return True
        else:
            RuntimeError(-1, "Constant or identifier contains mistakes!")
        return False
