current_state = [0,1,0]

results = []

while True:
    for i in range(100):
        current_state = [0] + list(map(lambda c,p,n:p^(c|n), current_state, [0] + current_state, current_state[1:] + [0])) + [0]
        results.extend([current_state[round(len(current_state)/2)]])
    print(results)
    results = []
    
