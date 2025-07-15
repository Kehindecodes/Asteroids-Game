import pygame
from constant import *




def main ():
  pygame.init()
  time = pygame.time.Clock()
  dt = 0
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  print(screen)

  while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    pygame.Surface.fill(screen,(0,0,0))
    pygame.display.flip()
    time_passed = time.tick((60))
    dt = time_passed/1000






if __name__ == "__main__":
  main()