input_state = [1]

def get_neighbours(i, current_state):
    if i-1 < 0:
        prev_cell = 0
    else:
        prev_cell = current_state[i-1]
    if i < 0 or i > len(current_state)-1:
        current_cell = 0
    else:
        current_cell = current_state[i]
    if i+1 < 0 or i+1 > len(current_state)-1:
        next_cell = 0
    else:
        next_cell = current_state[i+1]

    return [prev_cell, current_cell, next_cell]

def get_cell_step(prev_cell, current_cell, next_cell):

    new_cell = prev_cell ^ (current_cell | next_cell)

    return new_cell

def next_step(current_state):
    new_state_cell_count = len(current_state)+1
    new_state = []
    for i in range(-1,new_state_cell_count):
        prev_cell, current_cell, next_cell = get_neighbours(i, current_state)
        new_cell = get_cell_step(prev_cell, current_cell, next_cell)
        new_state.append(new_cell)
    return new_state

current_state = input_state
results = []

while True:
    for i in range(100):
        current_state = next_step(current_state)
        #print(current_state[round(len(current_state)/2)])
        random_num = current_state[round(len(current_state)/2)]
        results.append(random_num)
    print(results)
    results = []
