import pygame
from menus import Menu


class DrawMenu(Menu):
    def __init__(self, surface):
        Menu.__init__(surface)

    def roundline(self, color, start, end, radius=1):
        dx = end[0]-start[0]
        dy = end[1]-start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int(start[0]+float(i)/distance*dx)
            y = int(start[1]+float(i)/distance*dy)
            pygame.draw.circle(self.screen, color, (x, y), radius)

    def run(self):
        finished = False
        FPS = 30
        draw_on = False
        while finished is False:
            e = pygame.event.wait()
            pygame.display.update()
            pygame.time.Clock().tick(FPS)
            if e.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.circle(self.screen, (255, 0, 0), e.pos, 1)
                draw_on = True
            if e.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if e.type == pygame.MOUSEMOTION:
                if draw_on:
                    pygame.draw.circle(self.screen, (255, 0, 0), e.pos, 1)
                    self.roundline((255, 0, 0), e.pos, last_pos, 1)
                last_pos = e.pos

            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or \
                        (event.type == pygame.KEYDOWN and
                         event.key == pygame.K_ESCAPE):
                    return 0
