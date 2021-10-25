from SymbolTable import SymbolTable

if __name__ == "__main__":
    _symbolTable = SymbolTable()

    _symbolTable.add("var")
    _symbolTable.add("int")
    _symbolTable.add("bool")
    _symbolTable.add("char")
    _symbolTable.add("array")
    _symbolTable.add("while")

    _symbolTable.print()