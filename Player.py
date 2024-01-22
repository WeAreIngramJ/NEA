import pygame

class Player():
    # Building the player from the initial conditions
    def __init__(self, x: int, y: int, width: int, height:int, colour) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        # This is what is displayed on screen
        self.rect = (x, y, width, height)
        self.speed = 5
        self.vel = [0,0]

    def draw(self, win):
        pygame.draw.rect(win, self.colour, self.rect)
    
    def move(self):
        # This is the movement input system for the player 
        # It maps the key pressed to a change in velocity
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.vel[0] -= self.speed if self.vel[0] >= 0 else 0
            # This speed change is done so that directions don't get 
            # prioritised if opposing directions are pressed at once

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.vel[0] += self.speed if self.vel[0] <= 0 else 0

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.vel[1] -= self.speed if self.vel[1] >= 0 else 0

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.vel[1] += self.speed if self.vel[1] <= 0 else 0

        if 0 not in self.vel:
            self.vel[0] /= 1.414
            self.vel[1] /= 1.414
        
        self.x += self.vel[0]
        self.y += self.vel[1]

        self.update()

        self.vel = [0,0]

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)