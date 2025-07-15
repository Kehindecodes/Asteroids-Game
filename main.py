import pygame
from constant import *




def main ():
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  print(screen)

  while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    pygame.Surface.fill(screen,(0,0,0))
    pygame.display.flip()






if __name__ == "__main__":
  main()