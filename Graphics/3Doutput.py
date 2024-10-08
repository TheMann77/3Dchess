import pygame
import math

def rotateX(radians):
    for a in range(len(squares)):
        for b in range(4):
            y = squares[a][b][1] - 300
            z = squares[a][b][2] - 300
            d = math.hypot(y, z)
            theta = math.atan2(y, z) + radians
            squares[a][b][2] = 300 + d * math.cos(theta)
            squares[a][b][1] = 300 + d * math.sin(theta)
def rotateY(radians):
    for a in range(len(squares)):
        for b in range(4):
            x = squares[a][b][0] - 300
            z = squares[a][b][2] - 300
            d = math.hypot(x, z)
            theta = math.atan2(x, z) + radians
            squares[a][b][2] = 300 + d * math.cos(theta)
            squares[a][b][0] = 300 + d * math.sin(theta)       
def rotateZ(radians):
    for a in range(len(squares)):
        for b in range(4):
            x = squares[a][b][0] - 300
            y = squares[a][b][1] - 300
            d = math.hypot(x, y)
            theta = math.atan2(x, y) + radians
            squares[a][b][0] = 300 + d * math.cos(theta)
            squares[a][b][1] = 300 + d * math.sin(theta)



squares = []
for a in range(3):
    for b in range(8):
        for c in range(8):
            d = [[c*50+100+50*x[0], a*200+100, b*50+100+50*x[1]] for x in [[0,0], [0,1], [1,1], [1,0]]]
            d.append((245,245,200) if (a+b+c)%2 == 0 else (225,198,153))
            squares.append(d)
screen = pygame.display.set_mode((600,600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rotateY(math.pi/90)
            elif event.key == pygame.K_RIGHT:
                rotateY(-math.pi/90)
            elif event.key == pygame.K_UP:
                rotateX(math.pi/90)
            elif event.key == pygame.K_DOWN:
                rotateX(-math.pi/90)
    screen.fill((255,255,255))
    for square in squares:
        pygame.draw.polygon(screen, square[4], [point[0:2] for point in square[0:4]])
    pygame.display.flip()