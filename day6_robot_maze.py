# link : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_rigth():
    turn_left()
    turn_left()
    turn_left()
flag = True



while flag:
    if front_is_clear() and right_is_clear() == False:
        move()
    elif front_is_clear() and right_is_clear():
        turn_rigth()
        move()
    elif right_is_clear() and front_is_clear() == False:
        turn_rigth()
        move()
    elif wall_in_front():
        turn_left()
    if at_goal():
        flag = False



