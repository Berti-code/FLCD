class FiniteAutomata:
    def __init__(self):
        self.states = None
        self.alphabet = None
        self.initial_state = None
        self.transitions = None
        self.final_states = None
        self.read_from_file("FA.in")

    @staticmethod
    def parse_line(line):
        return [value.strip() for value in line.strip().split(',')]

    def read_from_file(self, file_name):
        with open(file_name) as file:
            self.states = FiniteAutomata.parse_line(file.readline())
            self.alphabet = FiniteAutomata.parse_line(file.readline())
            self.initial_state = file.readline()
            self.final_states = FiniteAutomata.parse_line(file.readline())
            self.transitions = []
            i = -1
            with open(file_name) as fileobject:
                for line in fileobject:
                    i = i + 1
                    if i > 3:
                        self.transitions.append(line.strip())
            self.transitions = FiniteAutomata.parse_transitions(self.transitions)

    @staticmethod
    def parse_transitions(parts):
        result = {}
        for line in parts:
            key = line.split(",")
            value = key[1].split("=")
            key = key[0]
            if key in result.keys():
                result[key].append({value[0]: value[1]})
            else:
                result[key] = [{value[0]: value[1]}]

        print(result)
        return result

    def print_states(self):
        print(self.states)

    def print_alphabet(self):
        print(self.alphabet)

    def print_transition(self):
        print(self.transitions)

    def print_final_states(self):
        print(self.final_states)

    def is_final_state(self, state):
        if state in self.final_states:
            return True
        return False

    def eval_sequence(self, sequence):
        current_state = self.initial_state[0]
        dictionary = self.transitions
        for value in sequence:
            if value not in self.alphabet:
                return False
            elif current_state not in dictionary.keys():
                return False
            else:
                for element in dictionary[current_state]:
                    for key, v in element.items():
                        v = v.strip()
                        if int(key) == int(value):
                            current_state = v
                            break
        if self.is_final_state(current_state):
            return True
        else:
            return False


    def menu(self):
        try:
            print("\nSelect your choice")
            print("Press 1 to see the set of states")
            print("Press 2 to see the alphabet")
            print("Press 3 to see the transitions")
            print("Press 4 to see the final states")
            print("Press 5 to see if a sequence is accepted by the FA\n")

            choice = input("Please enter the number that corresponds to your choice: ")
            if int(choice) == 1:
                self.print_states()
            elif int(choice) == 2:
                self.print_alphabet()
            elif int(choice) == 3:
                self.print_transition()
            elif int(choice) == 4:
                self.print_final_states()
            elif int(choice) == 5:
                input_sequence = input("Input the sequence:\n")
                result = self.eval_sequence(input_sequence)
                if result == True:
                    print("The sequence is accepted by the FA!\n")
                else:
                    print("The sequence is not accepted by the FA!\n")
            else:
                print("Wrong input!")
        except Exception as e:
            print(e.with_traceback())


if __name__ == "__main__":
    fa = FiniteAutomata()
    while True:
        fa.menu()