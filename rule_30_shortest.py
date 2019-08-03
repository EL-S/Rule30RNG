current_state = [0,1,0]

while True:
    print(current_state)
    current_state = [0] + list(map(lambda c,p,n:p^(c|n), current_state, [0] + current_state, current_state[1:] + [0])) + [0]
