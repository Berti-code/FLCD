import SymbolTable


class Analyzer:

    def __init__(self):
        self.symbol_table = SymbolTable()
        self.pif = []
        self.identifiers = []
        self.tokens = []
        self.constants = []

    def scan(self):
        pass

    def trim(self, line):
        line = str.lstrip(line)
        line = line.replace("\n", '')
        if ";" in line:
            line = line.replace(";", '')
            line += ' ' + ';'
        line = line.replace(",", ' ,')
        line = line.replace("(", ' ( ')
        line = line.replace(")", ' )')
        line = line.replace("{", ' {')
        line = line.replace("[", ' [ ')
        line = line.replace("]", ' ]')
        line = line.replace("++", ' ++')
        if line[0] != "}":
            line = line.replace("}", ' }')
        line = line.replace("  ", ' ')
        return line