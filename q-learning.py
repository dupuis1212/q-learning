#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Artificial intelligence for business
# Optimizing warehouse flow with Q-Learning


import numpy as np


# Parameters gamma  and alpha
gamma = 0.75
alpha = 0.9


# PART 1 - DEFINING THE ENVIRONMENT


# States
location_to_state = {'A': 0,
                     'B': 1,
                     'C': 2,
                     'D': 3,
                     'E': 4,
                     'F': 5,
                     'G': 6,
                     'H': 7,
                     'I': 8,
                     'J': 9,
                     'K': 10,
                     'L': 11}


state_to_location = {state: location for location, state in location_to_state.items()}

# Actions
actions = [0,1,2,3,4,5,6,7,8,9,10,11]

# rewards
R = np.array([[0,1,0,0,0,0,0,0,0,0,0,0],
              [1,0,1,0,0,1,0,0,0,0,0,0],
              [0,1,0,0,0,0,1,0,0,0,0,0],
              [0,0,0,1,0,0,0,1,0,0,0,0],
              [0,0,0,0,0,0,0,0,1,0,0,0],
              [0,1,0,0,0,0,0,0,0,1,0,0],
              [0,0,1,0,0,0,0,1,0,0,0,0],
              [0,0,0,1,0,0,1,0,0,0,0,1],
              [0,0,0,0,1,0,0,0,0,1,0,0],
              [0,0,0,0,0,1,0,0,1,0,1,0],
              [0,0,0,0,0,0,0,0,0,1,0,1],
              [0,0,0,0,0,0,0,1,0,0,1,0]])





# PART 3 - GOING INTO PRODUCTION



def route(starting_location, ending_location):
    
    Q = np.zeros([12,12])
    ending_state = location_to_state[ending_location]
    
    RCopy = R.copy()
    RCopy[ending_state,ending_state] = 1000
    
    for _ in range(1000):
    
        current_state = np.random.randint(0,12)
        playable_actions = []
    
    
        for j in range(12):
            
            if RCopy[current_state, j] > 0:
                playable_actions.append(j)
        
        next_state = np.random.choice(playable_actions)
        
        TD = RCopy[current_state, next_state] + gamma * Q[next_state, np.argmax(Q[next_state,])] - Q[current_state, next_state]
        
        Q[current_state, next_state] = Q[current_state, next_state] + alpha * TD
    
    route = [starting_location]
    next_location = starting_location
    
    while next_location != ending_location:
        starting_state = location_to_state[starting_location]
        next_state = np.argmax(Q[starting_state,])
        next_location = state_to_location[next_state]
        starting_location = next_location
        route.append(next_location)
    
    return route


def best_route(starting_location, middle_location, ending_location):
    
    one = route(starting_location,middle_location)
    
    two = route(middle_location,ending_location)
    print(two)
    return one

best_route('E', 'K', 'G')


























