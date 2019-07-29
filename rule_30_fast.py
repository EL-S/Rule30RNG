current_state = [0,1,0]

def next_state(current_state):
    current_state, new_state = [0] + current_state + [0], []
    for i, cell in enumerate(current_state[1:-1]):
        new_state += [current_state[i] ^ (cell | current_state[i+2])]
    return [0] + new_state + [0]

results = []

while True:
    for i in range(100):
        current_state = next_state(current_state)
        results.extend([current_state[round(len(current_state)/2)]])
    print(results)
    results = []
