import sys, pygame

pygame.init()

screen = pygame.display.set_mode((240, 780))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((255,255,255))

    print(pygame.mouse.get_pressed()[0])
    
    pygame.draw.rect(screen, (245,245,200), (0,0,30,30))

    pygame.display.flip()

