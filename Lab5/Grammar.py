class Grammar:
    def __init__(self, non_terminals, terminals, starting_symbol, productions):
        self.non_terminals = non_terminals
        self.terminals = terminals
        self.starting_symbol = starting_symbol
        self.productions = productions

    @staticmethod
    def parseLine(line):
        equal_pos = line.index('=')

    @staticmethod
    def fromFile(fileName):
        with open(fileName) as file:
            non_terminals = Grammar.parseLine(file.readline())
            terminals = Grammar.parseLine(file.readline())
            starting_symbol = file.readline().split('=')[1].strip()
            productions = Grammar.parseLine([line.strip('\n').strip(',') for line in file][1:-1])

            return Grammar(non_terminals, terminals, starting_symbol, productions)

    @staticmethod
    def parseRules(rules):
        result = []
        for rule in rules:
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            rhs = [value.split() for value in rhs.split('|')]
            for value in rhs:
                result.append((lhs, value.split()))
        return result

    def isNonTerminal(self, value):
        return value in self.non_terminals

    def isTerminal(self, value):
        return value in self.terminals