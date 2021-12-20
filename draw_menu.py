from menu import Menu, InputBox, FONT, white
import pygame


class DrawMenu(Menu):
    def __init__(self, surface):
        Menu.__init__(self, surface)

        self.button_next = pygame.Rect(2*self.mid_w - 100, 2*self.mid_h - 50, 70, 30)
        self.button_clear = pygame.Rect(2*self.mid_w - 200, 2*self.mid_h - 50, 70, 30)
        self.button_back = pygame.Rect(30, 2*self.mid_h - 50, 70, 30)
        self.buttons = [self.button_next, self.button_clear, self.button_back]
        self.texts = ["продолжить", "очистить", "назад"]
        self.width_box = InputBox(self.mid_w, 2*self.mid_h - 50, 140, 25)
        self.road_width = 30
        self.color = 255, 0, 0
        self.pixel_list = [[False]*700]*700
        self.fitness_list = []

    def roundline(self, color, start, end, radius):
        dx = end[0]-start[0]
        dy = end[1]-start[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            x = int(start[0]+float(i)/distance*dx)
            y = int(start[1]+float(i)/distance*dy)

            pygame.draw.circle(self.screen, color, (x, y), radius)
            self.fitness_list.append([x, y])

    def run(self):
        finished = False
        FPS = 30
        draw_on = False
        while finished is False:
            pygame.display.update()
            pygame.time.Clock().tick(FPS)
            pygame.draw.rect(self.screen, (30, 30, 30), (0, 2*self.mid_h - 50, 2*self.mid_w, 50))
            i = 0
            for button in self.buttons:
                pygame.draw.rect(self.screen, (255, 255, 0), button)
                self.draw_text(self.texts[i], 15, button[0] + button[2]//2, button[1] + button[3]//2)
                i += 1
            e = pygame.event.wait()
            self.width_box.handle_event(e)
            try:
                self.road_width = int(self.width_box.get_data())
            except ValueError:
                pass
            pygame.draw.circle(self.screen, self.color, (40, 320), self.road_width, 4)
            self.width_box.draw(self.screen)
            text = FONT.render('Ширина трассы:', True, white)
            self.screen.blit(text,
                             (self.width_box.rect[0] - 100, self.width_box.rect[1] + 7))

            if e.type == pygame.MOUSEBUTTONDOWN:
                button_pressed_index = -1
                for i in range(len(self.buttons)):
                    if self.buttons[i].collidepoint(*e.pos):
                        button_pressed_index = i
                        break
                print(button_pressed_index)
                if button_pressed_index == 0:
                    self.check_pixels()
                    return 2  # К меню выбора параметров
                elif button_pressed_index == 1:
                    self.screen.fill((30, 30, 30))  # кусок кода который очистит нарисованное
                    self.fitness_list = []
                elif button_pressed_index == 2:
                    return 1  # К главному меню

                draw_on = True
            if e.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if e.type == pygame.MOUSEMOTION:
                if draw_on:
                    self.roundline(self.color, e.pos, last_pos, self.road_width)

                last_pos = e.pos
            if e.type == pygame.QUIT or \
                    (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                return 0

        pygame.display.flip()

    def check_pixels(self):
        for i in range(700):
            for j in range(700):
                if self.screen.get_at((i, j)) == self.color:
                    self.pixel_list[i][j] = True
                else:
                    self.pixel_list[i][j] = False

    def is_alive(self, car_x, car_y):
        return self.pixel_list[car_x][car_y]

    def fitness(self, car_x, car_y):
        for n in range(len(self.fitness_list)):
            (circle_x, circle_y) = self.fitness_list[n]
            if ((car_x - circle_x)**2 + (car_y - circle_y)**2)**0.5 <= self.road_width:
                return n
        return 0
