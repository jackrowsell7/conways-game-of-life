import time
import pygame
import numpy as np
import random

COLOUR_BG = (10, 10, 20)
COLOUR_GRID = (45, 45, 45)
COLOUR_DIE_NEXT = (252, 186, 3)
COLOUR_ALIVE_NEXT = (255, 255, 255)
FPS = 60
clock = pygame.time.Clock()

#CONTROLS
# DELETE/BACKSPACE = DELETE
# R = RANDOM
# MB0 = SPAWN CELL

def update(screen, cells, size, with_progress=False):
  generation = 0
  
  

  
  updated_cells = np.zeros((cells.shape[0], cells.shape[1]))  


  for row, col in np.ndindex(cells.shape):
    
    alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row,col]
    colour = COLOUR_BG if cells[row,col] == 0 else COLOUR_ALIVE_NEXT

    if cells[row,col] == 1:
      # Array is made up of 0s so no need to set it to 0
      if alive < 2 or alive > 3:
        if with_progress:
          colour = COLOUR_DIE_NEXT
      elif 2 <= alive <= 3:
        updated_cells[row,col] = 1
        if with_progress:
          colour = COLOUR_ALIVE_NEXT
    else:
      if alive == 3:
        updated_cells[row,col] = 1
        if with_progress:
          colour = COLOUR_ALIVE_NEXT

    pygame.draw.rect(screen, colour, (col * size, row * size, size - 1, size - 1))
    generation += 1
    
    
  print(updated_cells)


  return updated_cells


  
      
      
    #+2 not included - python string slicing
    

    

  


def main():
  pygame.init()
  screen = pygame.display.set_mode((1200,1000))
  cells = np.zeros((100,120))
  screen.fill(COLOUR_GRID)
  update(screen, cells, 10)
  clock.tick(FPS)

  pygame.display.flip()
  pygame.display.update()
  
  running = False

  while True:
    

    for event in pygame.event.get():
      

      if event.type == pygame.QUIT:
        pygame.quit()
        return
      elif event.type == pygame.KEYDOWN:
        print(event.key)
        if event.key == pygame.K_SPACE:
          
          running = not running
          update(screen, cells, 10)
          
          pygame.display.update()
          
        
        if event.key == pygame.K_r:
          print("RANDOM_")
          for row, col in np.ndindex(cells.shape):
            num = random.randint(0,1)
            if num == 1 and running == False:
              
              cells[row, col] = 1
            
          update(screen, cells, 10)
          pygame.display.update()

        if event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE: #Find more efficient delete method 
          deleted = 0
          print("DELETE_")
          for row, col in np.ndindex(cells.shape):
            
            if cells[row,col] == 1:
              deleted += 1
              
              
              cells[row,col] = 0
          
          update(screen, cells, 10)
          pygame.display.update()
          print("| Deleted", deleted, "cells")

        if event.key == pygame.K_q:
          print("QUITTING")
          pygame.quit()

        


          

      if pygame.mouse.get_pressed()[0]:
        
        
      
        pos = pygame.mouse.get_pos()
        
        cells[pos[1] // 10, pos[0] // 10] = 1

      
      
      
        
        
        
        
        update(screen, cells, 10)
        pygame.display.update()
     

    screen.fill(COLOUR_GRID)
    if running:
      cells = update(screen, cells, 10, with_progress=True)
      pygame.display.update()
      
    


        

if __name__ == '__main__':
  print("CONTROLS: Q = QUIT | DELETE = DELETE | R = RANDOM | MB0 = SPAWN CELL")
  main()
