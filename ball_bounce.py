import pygame, sys
from pygame.locals import *
clock = pygame.time.Clock()

WIN = pygame.display.set_mode((900, 500))
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

ball_radius = 10
ball_pos = [450, 20]
ball_vel = pygame.math.Vector2((0, 0))
GRAVITY = 0.1

while True:
    WIN.fill(WHITE)
    
    ball_pos[0] += ball_vel.x
    ball_pos[1] += ball_vel.y
    ball_vel.y += GRAVITY
    if ball_pos[1] + ball_radius > 500:
        ball_vel.y = -ball_vel.y + GRAVITY
    pygame.draw.circle(WIN, BLACK, ball_pos, ball_radius, 0)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)
    pygame.display.update()