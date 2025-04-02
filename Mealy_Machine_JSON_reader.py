import json
class MealyMachine:
    def __init__(self, states, transitions, initial_state, input_sequence):
        self.states = states
        self.transitions = transitions
        self.initial_state = initial_state
        self.input_sequence = input_sequence
    def run_mealy_machine(self):
        path = [[],[]]
        path[0].append(self.initial_state)
        i = 0
        next = "next_state"
        literally_output = "output"
        current_state = self.initial_state
        while i < len(self.input_sequence):
            c = self.input_sequence[i]
            if c not in self.transitions[current_state]:
                break
            output = self.transitions[current_state][c][literally_output]
            current_state = self.transitions[current_state][c][next]
            path[0].append(current_state)
            path[1].append(output)
            i += 1
        return path
    def print_result(self):
        output = self.run_mealy_machine()
        path_str = "Path: "
        for i,state in enumerate(output[0]):
            path_str += state
            if i < len(output[0]) - 1:
                path_str += " -> "
        print(path_str)
        output_str = "Output: "
        for i,out in enumerate(output[1]):
            output_str += out
        print(output_str)
class JSONConverter:
    def convert_json_to_dict(file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
        return data
    def convert_dict_to_mealy_machine_class(data):
        return MealyMachine(data['states'], data['transitions'], data['initial_state'], data['input_sequence'])
    def convert_data_to_dict(data):
        data = {"states": data.states, "transitions": data.transitions, "initial_state" : data.initial_state,  "input_sequence": data.input_sequence}
        return data
    def convert_dict_to_json(data, file_path):
        with open(file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    # Example usage
    json_file_path = 'mealy_machine.json'
    data = JSONConverter.convert_json_to_dict(json_file_path)
    mealy_machine = JSONConverter.convert_dict_to_mealy_machine_class(data)
    mealy_machine.print_result()
    # Convert back to JSON
    dict_data = JSONConverter.convert_data_to_dict(mealy_machine)
    JSONConverter.convert_dict_to_json(dict_data, 'output.json')

