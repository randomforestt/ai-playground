class FrozenLakeState(object):
    def __init__(self, state_number, env):
        self.n = state_number
        self.env = env
        self.row, self.column = env.n_to_location(self.n)
        self.char = env.n_to_char(self.n)
        self.reward = env.reward[self.char]
        self.icon = env.icons[self.char]
        self.is_terminal = env.is_terminal[self.char]
        self.probability = None
    
    def up(self):
        row = max(0, self.row - 1)
        n = self.env.location_to_n(row, self.column)
        return FrozenLakeState(n, self.env)
    
    def down(self):
        row = min(self.row + 1, self.env.rows - 1)
        n = self.env.location_to_n(row, self.column)
        return FrozenLakeState(n, self.env)
        
    def left(self):
        column = max(0, self.column - 1)
        n = self.env.location_to_n(self.row, column)
        return FrozenLakeState(n, self.env)
    
    def right(self):
        column = min(self.column + 1, self.env.columns - 1)
        n = self.env.location_to_n(self.row, column)
        return FrozenLakeState(n, self.env)
    
    def next_possible_states(self, action):
        
        if self.is_terminal:
            self.reward = 0.0
            return [self]
        
        if action == 'up':
            return [self.up(), self.left(), self.right()]                        
        elif action == 'down':
            return [self.down(), self.left(), self.right()]        
        elif action == 'left':
            return [self.left(), self.up(), self.down()]        
        elif action == 'right':
            return [self.right(), self.up(), self.down()]               
        else:
            raise ValueError("error: invalid action", action)
            
    def __repr__(self):
        s = "*FrozenLakeState (TYPE) \n"
        n = "--> State Number: " + str(self.n) + "\n"
        r = "--> Reward: " + str(self.reward) + "\n"

        t = None
        if self.is_terminal is True:
            t = "--> A terminal state. \n"
        else:
            t = "--> Not a terminal state. \n"
        if self.probability is not None:
            p = "--> (Transition) Probability (given state_number and action): " + str(self.probability) + "\n"
        else:
            p = "--> Transition probability is not yet defined \n"
        
        i = "--> Icon: " + self.icon + "\n"
        c = "--> Character representation of state condition: '" + self.char + "'\n"
        l = "--> Location: (" + str(self.row) + "," + str(self.column) + ") \n"
        
        final = "\n" + s + n + r + t + p + i + c + l + "\n"
        return final 
    
class SlipperyFrozenLake(object):
    def __init__(self, my_map):
        self.map = my_map
        # Assumes all rows have the same length
        self.rows = len(self.map)
        self.columns = len(self.map[1])
        self.number_of_states = self.rows * self.columns
        self.reward = {'S': 0.0, 'F': 0.0, 'H': 0.0, 'G': 1.0}
        self.is_terminal = {'S': False, 'F': False, 'H': True, 'G': True}
        self.icons = {'S': '👩', 'F': '▫️', 'H': '💥', 'G': '🎯'}
        self.actions = ['up', 'down', 'left', 'right']
        self.n_map = []
        
        for row in range(self.rows):
            new_row = []
            for column in range(self.columns):
                new_row.append(row*self.rows + column)
            self.n_map.append(new_row)
                        
    def n_to_char(self, n):
        row, column = self.n_to_location(n)
        return self.map[row][column]
        
    def n_to_location(self, n):
        row = n // self.rows
        columns = n % self.columns
        return (row, columns)
        
    def location_to_n(self, row, column):
        return row * self.rows + column
    
    def get_possibilities(self, state_number, action, debug=False):
        
        n = state_number
        if action not in self.actions: 
            raise ValueError("error: invalid action", action)
        if n >= self.number_of_states: 
            raise ValueError("error: invalid state", n)
        
        state = FrozenLakeState(n, self)
        possibilities = state.next_possible_states(action)
        probability = 1.0 / len(possibilities)
        
        for state in possibilities:
            state.probability = probability
            
        if debug:
            print("***")
            print('From state: ', n, ' do action: ', action, "!")
            print("***")
            
            for i, state in enumerate(possibilities): 
                print()
                print("#", i + 1)
                print('--> next state: ',state.n)
                print('--> reward:', state.reward)
                print('--> probability: ', state.probability)
                print('--> is terminal: ', state.is_terminal)
                print()

        return possibilities 


def a_few_tests(): 
    
    frozen_lake_map = [
        ['S', 'F', 'F', 'F'], 
        ['F', 'H', 'F', 'H'],
        ['F', 'F', 'F', 'H'],
        ['H', 'F', 'F', 'G']]
    
    env = SlipperyFrozenLake(frozen_lake_map)
    # n to char, loc to n, n to loc
    ntochar = {
        0: 'S',
        1: 'F',
        2: 'F', 
        3: 'F',
        4: 'F',
        5: 'H',
        6: 'F',
        7: 'H',
        8: 'F',
        9: 'F',
        10: 'F',
        11: 'H',
        12: 'H',
        13: 'F',
        14: 'F',
        15: 'G',
    }

    ntor = {
        0: 0,
        1: 0,
        2: 0, 
        3: 0,
        4: 1,
        5: 1,
        6: 1,
        7: 1,
        8: 2,
        9: 2,
        10: 2,
        11: 2,
        12: 3,
        13: 3,
        14: 3,
        15: 3,
    }

    ntoc = {
        0: 0,
        1: 1,
        2: 2, 
        3: 3,
        4: 0,
        5: 1,
        6: 2,
        7: 3,
        8: 0,
        9: 1,
        10: 2,
        11: 3,
        12: 0,
        13: 1,
        14: 2,
        15: 3,
    }
    
    for i in range(env.rows * env.columns): 
        char = env.n_to_char(i)
        r, c = env.n_to_location(i)
        
        if char != ntochar[i]:
            raise ValueError('ERROR incorrect n to char mapping:', i, char)
            
        if r != ntor[i]:
            raise ValueError('ERROR incorrect n to r mapping:', i, r)

        if c != ntoc[i]:
            raise ValueError('ERROR incorrect n to c mapping:', i, c)
            
    print("PASSED! :) ")