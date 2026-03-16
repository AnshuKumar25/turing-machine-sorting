# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__)

# class TuringMachine:
#     def __init__(self, tape, blank='_'):
#         self.tape = list(tape) + [blank]  # Append blank to indicate end
#         self.blank = blank
#         self.states = []  # Stores simulation steps
#         self.transition_table = []  # Stores transition function table
    
#     def extract_numbers(self):
#         """Extracts numbers from the tape and returns them as a list."""
#         segments = ''.join(self.tape).split(self.blank)[0]  # Ignore blank
#         return [int(segment) for segment in segments.split('#') if segment.isdigit()]
    
#     def update_tape(self, numbers):
#         """Updates the tape with sorted numbers."""
#         return ' '.join(map(str, numbers))
    
#     def log_transition(self, state, read_symbol, next_state, write_symbol, move):
#         """Stores each transition in the transition table."""
#         self.transition_table.append({
#             "Current State": state,
#             "Read Symbol": read_symbol,
#             "Next State": next_state,
#             "Write Symbol": write_symbol,
#             "Move": move
#         })
    
#     def run(self):
#         numbers = self.extract_numbers()
#         self.states.append("Initial Tape: " + self.update_tape(numbers))
        
#         # Sorting logic using a Bubble Sort-like approach
#         state_counter = 0
#         for i in range(len(numbers)):
#             for j in range(len(numbers) - i - 1):
#                 current_state = f"q{state_counter}"
#                 next_state = f"q{state_counter+1}"
#                 self.log_transition(current_state, f"{numbers[j]} & {numbers[j+1]}", next_state, 
#                                     "Swapped" if numbers[j] > numbers[j+1] else "No Swap", "Right")

#                 if numbers[j] > numbers[j+1]:
#                     numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#                 self.states.append("Step {}: {}".format(state_counter+1, self.update_tape(numbers)))
#                 state_counter += 1
        
#         self.states.append("Final Sorted Tape: " + self.update_tape(numbers))
#         return self.update_tape(numbers), self.transition_table, self.states

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/sort', methods=['POST'])
# def sort_numbers():
#     data = request.json
#     tape_input = data.get("numbers", "")
#     tm = TuringMachine(tape_input)
#     sorted_tape, transition_table, states = tm.run()
#     return jsonify({
#         "sorted_tape": sorted_tape,
#         "transition_table": transition_table,
#         "simulation_steps": states
#     })

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

class TuringMachine:
    def __init__(self, tape, blank='_'):
        self.tape = list(tape) + [blank]  # Append blank to indicate end
        self.blank = blank
        self.states = []  # Stores simulation steps
        self.transition_table = []  # Stores transition function table
    
    def extract_numbers(self):
        """Extracts numbers from the tape and returns them as a list."""
        segments = ''.join(self.tape).split(self.blank)[0]  # Ignore blank
        return [int(segment) for segment in segments.split('#') if segment.isdigit()]
    
    def update_tape(self, numbers):
        """Updates the tape with sorted numbers."""
        return ' '.join(map(str, numbers))
    
    def log_transition(self, state, read_symbol, next_state, write_symbol, move):
        """Stores each transition in the transition table."""
        self.transition_table.append({
            "Current State": state,
            "Read Symbol": read_symbol,
            "Next State": next_state,
            "Write Symbol": write_symbol,
            "Move": move
        })
    
    def quicksort(self, numbers, left, right, state_counter):
        if left < right:
            pivot_index, state_counter = self.partition(numbers, left, right, state_counter)
            state_counter = self.quicksort(numbers, left, pivot_index - 1, state_counter)
            state_counter = self.quicksort(numbers, pivot_index + 1, right, state_counter)
        return state_counter
    
    def partition(self, numbers, left, right, state_counter):
        pivot = numbers[right]
        i = left - 1
        for j in range(left, right):
            current_state = f"q{state_counter}"
            next_state = f"q{state_counter + 1}"
            self.log_transition(current_state, f"Compare {numbers[j]} & {pivot}", next_state, 
                                "Swap" if numbers[j] < pivot else "No Swap", "Right")
            
            if numbers[j] < pivot:
                i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]
                self.states.append(f"Step {state_counter + 1}: {self.update_tape(numbers)}")
            
            state_counter += 1
        
        numbers[i + 1], numbers[right] = numbers[right], numbers[i + 1]
        self.states.append(f"Step {state_counter + 1}: {self.update_tape(numbers)}")
        return i + 1, state_counter + 1
    
    def run(self):
        numbers = self.extract_numbers()
        self.states.append("Initial Tape: " + self.update_tape(numbers))
        
        state_counter = self.quicksort(numbers, 0, len(numbers) - 1, 0)
        
        self.states.append("Final Sorted Tape: " + self.update_tape(numbers))
        return self.update_tape(numbers), self.transition_table, self.states

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort_numbers():
    data = request.json
    tape_input = data.get("numbers", "")
    tm = TuringMachine(tape_input)
    sorted_tape, transition_table, states = tm.run()
    return jsonify({
        "sorted_tape": sorted_tape,
        "transition_table": transition_table,
        "simulation_steps": states
    })

if __name__ == '__main__':
    app.run(debug=True)
