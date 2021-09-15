'''
A rect animation where there are movements within the borders of a rect.
'''
import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

def get_borders(rect, rect_n, size):
    '''Returns a list of rects at the borders of a  rectangle
        size: width or height to the left or right.'''
    startx, starty = rect.topleft
    rects = []

    dx = (rect.width - size)/rect_n
    dy = (rect.height - size)/rect_n

    for i in range(rect_n * 4):
        if i < rect_n:
            r = [startx, starty, dx, size]
            startx += dx
        elif i < rect_n * 2:
            r = [startx, starty, size, dy]
            starty += dy
        elif i < rect_n * 3:
            r = [startx + size - dx, starty, dx, size]
            startx -= dx
        else:
            r = [startx, starty + size - dx, size, dy]
            starty -= dy
        rects.append(r)
    return rects

# Open a game window
WINSIZE = (600, 500)
WIN = pygame.display.set_mode(WINSIZE)
pygame.display.set_caption('Rect Animation')

# Create our rect
main_rect = pygame.Rect(100, 50, 400, 400)

# define its broken borders
dsize = 20
inset = main_rect.inflate(-dsize, -dsize)
divisions = 10
border_rects = get_borders(main_rect, divisions, dsize/2)

# important constants
WHITE       = (255, 255, 255)
BLACK       = (  0,   0,   0)
GREEN       = (  0, 255,   0)
DARKGREEN   = (  0, 100,   0)
BACKGROUND = GREEN

# important states
start = 0
end = 10
frames = 0
total_division = divisions * 4

# game loop
while True:
    # clear the window
    WIN.fill(BACKGROUND)

    # blit our rect and its borders
    pygame.draw.rect(WIN, DARKGREEN, main_rect, 0)
    pygame.draw.rect(WIN, BACKGROUND, inset, 0)

    # the animation
    frames += 1
    if frames % 4 == 0:
        end += 1
        if end == total_division:
            end = 0
    if frames % 12 == 0:
        start += 1
        if start == total_division:
            start = 0
        # end += 1
        # if end == total_division:
        #     end = 0

    start_in = min(start, end)  # start index
    end_in = max(start, end)  # end index
    for r in border_rects[start_in: end_in]:
        pygame.draw.rect(WIN, BLACK, r, 0)

    # receive events
    for event in pygame.event.get():
        if event.type == QUIT or \
            (event.type == KEYDOWN and event.key == K_ESCAPE):
            # print(border_rects)
            # print(len(border_rects))
            pygame.quit()
            sys.exit()

    # control our changes
    clock.tick(60)  # timing
    pygame.display.update()  # visibility
