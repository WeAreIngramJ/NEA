import pygame
import pickle
from Network import Network

width = 1440
height = 960

#Setting up the pygame screen
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def redrawWindow(win, player1, player2):
    win.fill((255,255,255))
    player1.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True

    net = Network()
    
    player = net.getPos()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        player2 = net.send(player)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
        player.move()
        redrawWindow(win, player, player2)

main()