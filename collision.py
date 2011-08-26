def collision(listbball, x, y):
    #If the bball is hits your ball, existball = False, otherwise its True
    for coordinate in listbball:
        if abs(coordinate[0] - x) < 35 and abs(coordinate[1]-y)<35:
            return False
        
    return True
