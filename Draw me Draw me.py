import pygame


def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int(start[0]+float(i)/distance*dx)
        y = int(start[1]+float(i)/distance*dy)
        pygame.draw.circle(srf, color, (x, y), radius)


finished = False
FPS = 30
draw_on = False
screen = pygame.display.set_mode((700, 700))
while finished is False:
    e = pygame.event.wait()
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
    if e.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(screen, (255, 0, 0), e.pos, 1)
        draw_on = True
    if e.type == pygame.MOUSEBUTTONUP:
        draw_on = False
    if e.type == pygame.MOUSEMOTION:
        if draw_on:
            pygame.draw.circle(screen, (255, 0, 0), e.pos, 1)
            roundline(screen, (255, 0, 0), e.pos, last_pos, 1)
        last_pos = e.pos

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and
                 event.key == pygame.K_ESCAPE):
            finished = True
pygame.quit()
