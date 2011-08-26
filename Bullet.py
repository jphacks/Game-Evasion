

class Bullet:

    def shoot(self, bullet_x, posx, posy):        
        """bullet_x is the variable changing the location of the bullet.
        posx and posy are the position of the mouse when it was clicked"""        

        if posx < 500:
            bullet_x = bullet_x + 25
            bullet_y = posy
            return bullet_x, bullet_y
        
        else:
            bullet_x = bullet_x - 25
            bullet_y = posy
            return bullet_x, bullet_y

        
        
    
