import pygame, sys, random, time
from pygame.locals import *

pygame.init()
veci = pygame.math.Vector2(1, 0)
vecj = pygame.math.Vector2(0, 1)

# Open Window
WINSIZE = (600, 500)
WIN = pygame.display.set_mode(WINSIZE)
pygame.display.set_caption('Clock')

# Get the current time
now = time.localtime()
start_time = now.tm_sec + time.time()
hour = now.tm_hour
minutes =  now.tm_min
seconds = time.time() - start_time

# Store the position of the Clock
rect = pygame.Rect(100, 25, 400, 400)
center = list(rect.center)
radius = 200 # Store the radius of the clock

# constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont('monospace', 32)

# game loop
while True:
    WIN.fill(WHITE)

    # render the clock
    pygame.draw.circle(WIN,  BLACK, center, radius, 1)
    pygame.draw.circle(WIN, BLACK, center, 2, 0)
    for i in range(12):
        p1 = veci.rotate(30 * i) * (radius - 3) + center
        p2 = veci.rotate(30 * i) * (radius - 10) + center
        pygame.draw.line(WIN, BLACK, p1, p2, 2)
    
    hour_angle = hour * 30 + minutes * 0.5
    min_angle = minutes * 6
    sec_angle = seconds * 6
    p1 = -vecj.rotate(hour_angle) * (radius - 70) + center
    p2 = -vecj.rotate(min_angle) * (radius - 30) + center
    p3 = -vecj.rotate(sec_angle) * (radius - 20) + center
    pygame.draw.line(WIN, BLACK, center, p1, 2)
    pygame.draw.circle(WIN, BLACK, p1, 2, 0)
    pygame.draw.line(WIN, BLACK, center, p2, 2)
    pygame.draw.circle(WIN, BLACK, p2, 2, 0)
    pygame.draw.line(WIN, BLACK, center, p3, 2)
    pygame.draw.circle(WIN, BLACK, p3, 2, 0)

    # render time in words
    text = ('0' + str(int(hour)) if hour < 10 else str(int(hour))) + \
        ' : ' + \
        ('0' + str(int(minutes)) if minutes < 10 else str(int(minutes)))
    text_surf = FONT.render(text, True, BLACK)
    posx = WINSIZE[0]/2 - text_surf.get_width()/2
    posy = center[1] + radius + 10
    WIN.blit(text_surf, (posx, posy))

    # update the time
    dt = (time.time() - start_time) - seconds
    seconds = seconds + dt
    minutes = minutes + dt/60
    hour = hour + dt/3600
    if seconds >= 60:
        seconds = seconds - 60
    if minutes >= 60:
        minutes = minutes - 60
    if hour > 12:
        hour = hour - 12

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()