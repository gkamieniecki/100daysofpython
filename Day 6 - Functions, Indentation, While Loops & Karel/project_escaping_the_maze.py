def turn_right():
    turn_left()
    turn_left()
    turn_left()
     

while not at_goal(): 
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
            move()
    else:
        turn_left()
        
        
# once Day 15 is completed, come back to this exercise and try to debug the edge case
            
        
    





