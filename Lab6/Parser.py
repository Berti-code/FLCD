from enum import auto


class State:
    NORMAL = auto()
    ERROR = auto()
    BACK = auto()
    FINAL = auto()


class Parser:
    def __init__(self, grammar):
        self.state = State.NORMAL
        self.index = 0
        self.working_stack = []
        self.input_stack = [grammar.getStartSymbol()]
        self.grammar = grammar

    def momentary_insuccess(self):
        """
        The state has to be changed to "BACK" in this case.
        :return: none
        """
        print("Momentary insuccess\n")
        self.state = State.BACK
        print("Changing state to BACK\n")

    def success(self):
        """
        The state will become "FINAL" in this case.
        :return: none
        """
        print("Success!\n")
        self.state = State.FINAL
        print("Changing state to FINAL\n")

    def expand(self):
        """
        In the case of expanding, we have to take the nonterminal from the input stack and search for the first production corresponding to this nonterminal,
        then we append the nonterminal and the corresponding first production to the working stack, we pop the nonterminal from the input stack,
        and finally we have to push the first production to the imput stack.
        :return: none
        """
        print("Expand\n")
        non_terminal = self.input_stack[0]
        first_production = self.grammar.getFirstProduction(non_terminal)
        self.working_stack.append([non_terminal, first_production])
        self.input_stack = self.input_stack[1:]
        self.input_stack = first_production + self.input_stack

    def advance(self):
        """
        In the case of advancing, the index is incremented, the top element of the input stack gets pushed to the working stackand popped from the input stack.
        :return: none
        """
        print("Advance\n")
        self.index += 1
        self.working_stack.append(self.input_stack[0])
        self.input_stack = self.input_stack[1:]

    def back(self):
        """
        Back will be the opposite operation to advance, so the index will get decremented, and the element from the working stack will be popped and pushed back to the input stack.
        :return: none
        """
        print("Back\n")
        self.index -= 1
        terminal = self.working_stack.pop(-1)
        self.input_stack = [terminal] + self.input_stack

    def another_try(self):
        """
        In this case we have to get the element(production) on top of the working stack, get it's corresponding nonterminal and check all it's productions,
        then we check if the next production that we need exists, in which case we select it.
        :return: none
        """
        print("Another try\n")
        last = self.working_stack[-1]
        non_terminal = last[0]

        productions = self.grammar.printProductionsList(non_terminal)
        productions = [[non_terminal, production] for production in productions]
        next_production = self.grammar.getNextProduction(last, productions)

        if next_production is not None:
            print("Changing state to Normal...\n")
            self.state = State.NORMAL
            self.working_stack.pop(-1)
            self.working_stack.append([next_production[0], next_production[1]])
            self.input_stack = self.input_stack[len(last[1]):]
            self.input_stack = next_production[1] + self.input_stack
        elif self.index == 0 and last[0] == self.grammar.getStartSymbol():
            print("Changing state to Error...\n")
            self.state = State.ERROR
        else:
            self.working_stack.pop(-1)
            self.input_stack = [last[0]] + self.input_stack[len(last[1]):]
