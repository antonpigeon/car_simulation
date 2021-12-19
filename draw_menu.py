import pygame
from menu import Menu


class DrawMenu(Menu):
    def __init__(self, surface):
        Menu.__init__(self, surface)
        self.button_next = pygame.Rect(2*self.mid_w - 100, 2*self.mid_h - 50, 70, 30)
        self.button_clear = pygame.Rect(2*self.mid_w - 200, 2*self.mid_h - 50, 70, 30)
        self.button_back = pygame.Rect(30, 2*self.mid_h - 50, 70, 30)
        self.buttons = [self.button_next, self.button_clear, self.button_back]
        self.texts = ["продолжить", "очистить", "назад"]

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
            i = 0
            for button in self.buttons:
                pygame.draw.rect(self.screen, (255, 255, 0), button)
                self.draw_text(self.texts[i], 15, button[0] + button[2]//2, button[1] + button[3]//2)
                i += 1

            if e.type == pygame.MOUSEBUTTONDOWN:
                button_pressed_index = -1
                for i in range(len(self.buttons)):
                    if self.buttons[i].collidepoint(*e.pos):
                        button_pressed_index = i
                        break
                print(button_pressed_index)
                if button_pressed_index == 0:
                    return 2
                elif button_pressed_index == 1:
                    pass  # кусок кода который очистит нарисованное
                elif button_pressed_index == 2:
                    return 1

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
