import pygame
from constant import *
from player import Player

def main ():
  pygame.init()
  time = pygame.time.Clock()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  dt = 0
  updatable =  pygame.sprite.Group()
  drawables = pygame.sprite.Group()
  Player.containers = (updatable, drawables)
  Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
  while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    updatable.update(dt)
    pygame.Surface.fill(screen,( 0,0,0))
    for drawable in drawables:
         drawable.draw(screen)
    pygame.display.flip()
    time_passed = time.tick((60))
    dt = time_passed/1000






if __name__ == "__main__":
  main()