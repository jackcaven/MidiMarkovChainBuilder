"""
Builds markov chain from array of floats
"""
# Import libraries
import numpy as np

# Define classes
class MIDIMarkovChain():
    """
    Builds markov chain and holds transition matrix
    """
    # Constructor
    def __init__(self, input_array):
        # Properties
        self.transition_matrix = self._build_transition_matrix(input_array)
        # Fields
        self._current_state = np.random.randint(0, 127)
        self._choice_array = [value for value in range(0, 127)]
    
    # Public Methods
    def get_next_state(self):
        probability_row = self.transition_matrix[self._current_state]
        
        if(np.count_nonzero(probability_row) == 0):
            self._current_state = np.random.randint(0, 127)
        else:
            self._current_state = np.random.choice(self._choice_array, p=probability_row)
        
        return self._current_state
    
    # Private Methods  
    def _build_transition_matrix(self, input_array):
        prob_matrix = []
        
        for i in range(0, 127):
            prob_matrix.append(self._build_transition_row(i, input_array))    
        
        return prob_matrix
    
    def _build_transition_row(self, _val, input_array):
        transition_row = [0] * 127
        index_of_values = [i for i, n in enumerate(input_array) if n == _val]
        
        if len(index_of_values) == 0:
            return transition_row
        
        for _index in index_of_values:
            if _index >= len(input_array) - 1:
                continue
            
            transition_row[input_array[_index + 1]] += 1
        
        prob_array = [round(_item / len(index_of_values), 2) for _item in transition_row]
        
        if sum(prob_array) != 1:
            _difference = 1 - sum(prob_array)
            # no_of_non_zero_values = np.count_nonzero(prob_array)
            # _adjustment = _difference / no_of_non_zero_values
            # for _item in prob_array:
            #     if _item != 0:
            #         _item += _adjustment
            prob_array[prob_array.index(max(prob_array))] += _difference
        
        return prob_array