


class badball:


    def move(self, bball_x, bball_y, x ,y):    
        dx = 10
        dy = 10
        if bball_x < x and bball_y <y:
            bball_x = bball_x + dx
            bball_y = bball_y + dy
            return bball_x,bball_y

        if bball_x > x and bball_y <y:
            bball_x = bball_x - dx
            bball_y = bball_y + dy
            return bball_x,bball_y

        if bball_x < x and bball_y >y:
            bball_x = bball_x + dx
            bball_y = bball_y - dy
            return bball_x,bball_y

        if bball_x > x and bball_y >y:
            bball_x = bball_x - dx
            bball_y = bball_y - dy
            return bball_x,bball_y

        if bball_x == x and bball_y >y:        
            bball_y = bball_y - dy
            return bball_x,bball_y

        if bball_x == x and bball_y <y:        
            bball_y = bball_y + dy
            return bball_x,bball_y

        if bball_x > x and bball_y == y:
            bball_x = bball_x - dx
            return bball_x,bball_y
            
        if bball_x < x and bball_y == y:
            bball_x = bball_x + dx
            return bball_x,bball_y

        if bball_x == x and bball_y == y:
            return bball_x,bball_y
            













            
