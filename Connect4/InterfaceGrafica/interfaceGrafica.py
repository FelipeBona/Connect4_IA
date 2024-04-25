import pygame

pygame.init()

canvas = pygame.display.set_mode((500, 500)) 


pygame.display.set_caption("My Board") 
exit = False
  

color = (255,255,255) 
rect_color = (255,0,0) 

while not exit: 
    canvas.fill(color) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
  
    pygame.draw.rect(canvas, rect_color, 
                     pygame.Rect(30,30,60,60)) 
    pygame.display.update() 