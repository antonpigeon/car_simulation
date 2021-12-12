import pygame

from car import *
pygame.font.init()

red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
colors = [red, blue, yellow, green, magenta, cyan]

COLOR_INACTIVE = cyan
COLOR_ACTIVE = blue
COLOR_ERROR = red
TITLE = pygame.font.Font(None, 27)
FONT = pygame.font.Font(None, 18)


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Если пользователь нажал на прямоугольник input_box.
            if self.rect.collidepoint(event.pos):
                # Переключение активной переменной.
                self.active = not self.active
            else:
                self.active = False

            # Изменение цвета поля ввода.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(f'Параметр {self.text}')
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

                # Перерисовка текста.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Изменение размера поля, если текст слишком длинный.
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def get_data(self):
        return self.text

    def draw(self, screen):
        # Отрисовка текста
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Отрисовка поля для ввода
        pygame.draw.rect(screen, self.color, self.rect, 1)


class Menu:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.mid_w, self.mid_h = self.screen.get_width() / 2, self.screen.get_height() / 2
        self.clock = pygame.time.Clock()

        self.run_display = True
        self.offset = - 100

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def blit_screen(self):
        self.screen.blit(self.screen, (0, 0))
        pygame.display.update()

    def run(self):
        self.draw_text('Attempt to run an empty menu! WTF?', 20, 100, 100)
        print('Attempt to run an empty menu! WTF?')
        return 0


class MainMenu(Menu):
    def __init__(self, screen: pygame.Surface):
        Menu.__init__(self, screen)
        print('Running main menu')

        self.button_options = pygame.Rect(self.screen.get_width()//2 - 100, self.screen.get_height()//2 - 13, 200, 25)
        self.button_quit = pygame.Rect(self.screen.get_width()//2 - 100, 5*self.screen.get_height()//8 - 13, 200, 25)

    def run(self):
        while True:  # да простят меня боги
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_options.collidepoint(event.pos):
                        return 2
                    if self.button_quit.collidepoint(event.pos):
                        return 0
            self.screen.fill((30, 30, 30))
            text = TITLE.render('Машины хаха', True, white)
            text_ = text.get_rect()
            text_.center = (self.mid_w, self.mid_h - 150)
            self.screen.blit(text, text_)

            pygame.draw.rect(self.screen, yellow, self.button_options)
            text = FONT.render('Задать параметры', True, black)
            self.screen.blit(text, (self.button_options.x + 45, self.button_options.y + 7))

            pygame.draw.rect(self.screen, yellow, self.button_quit)
            text = FONT.render('Выйти из игры', True, black)
            self.screen.blit(text, (self.button_quit.x + 55, self.button_quit.y + 7))

            pygame.display.update()
            self.clock.tick(30)


class OptionsMenu(Menu):
    def __init__(self, screen, data):
        print('running options menu')
        Menu.__init__(self, screen)
        self.button_start = pygame.Rect(self.screen.get_width()//2 - 100, self.screen.get_height()//2 - 13, 200, 25)

        self.button_back = pygame.Rect(self.screen.get_width()//2 - 100, 5*self.screen.get_height()//8 - 13, 200, 25)

        input_box1 = InputBox(100, 130, 140, 25, str(data[0]))
        input_box2 = InputBox(100, 200, 140, 25, str(data[1]))
        input_box3 = InputBox(100, 270, 140, 25, str(data[2]))
        self.input_boxes = [input_box1, input_box2, input_box3]

        self.data = data
        assert type(self.data) is list
        assert len(self.data) == 3

    def data_str_to_value(self):
        for i in range(len(self.data)):
            try:
                self.data[i] = float(self.data[i]) if i == 1 else int(self.data[i])
                print(type(self.data[i]))
            except ValueError:
                self.input_boxes[i].color = COLOR_ERROR
                self.draw_text('Это значение должно быть ' + ('десятичной дробью!' if i == 1 else 'целым!'),
                               self.input_boxes[i].rect[3] - 5, self.input_boxes[i].rect[0]
                               + self.input_boxes[i].rect[2] + 175,
                               self.input_boxes[i].rect[1] + 10)
                pygame.display.update((self.input_boxes[i].rect[0] + self.input_boxes[i].rect[2],
                                      self.input_boxes[i].rect[1] - 30, 1000, 60))
                return False
        if self.data[1] > 1 or self.data[1] < 0:
            self.draw_text('Это значение должно быть между 0 и 1!',
                           self.input_boxes[1].rect[3] - 5, self.input_boxes[1].rect[0]
                           + self.input_boxes[1].rect[2] + 175,
                           self.input_boxes[1].rect[1])
            pygame.display.update((self.input_boxes[1].rect[0] + self.input_boxes[1].rect[2],
                                   self.input_boxes[1].rect[1] - 30, 1000, 60))
            return False
        for i in 0, 2:
            if self.data[i] < 2:
                self.input_boxes[i].color = COLOR_ERROR
                self.draw_text('Это значение должно быть не меньше 2!',
                               self.input_boxes[i].rect[3] - 5, self.input_boxes[i].rect[0]
                               + self.input_boxes[i].rect[2] + 175,
                               self.input_boxes[i].rect[1] + 10)
                pygame.display.update((self.input_boxes[i].rect[0] + self.input_boxes[i].rect[2],
                                       self.input_boxes[i].rect[1] - 30, 1000, 60))
                return False
        return True

    def run(self):
        while True:  # да простят меня боги
            for event in pygame.event.get():
                self.screen.fill((30, 30, 30))
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_start.collidepoint(event.pos):
                        if self.data_str_to_value() is True:
                            return 3
                        else:
                            pygame.time.wait(500)
                    if self.button_back.collidepoint(event.pos):
                        return 1

                for box in self.input_boxes:
                    box.handle_event(event)
                text = FONT.render('Введите параметры:',
                                   True, white)
                self.screen.blit(text,
                                 (self.input_boxes[0].rect.x, self.input_boxes[0].rect.y - 60))

                text1 = FONT.render('Размер популяции', True, white)
                self.screen.blit(text1,
                                 (self.input_boxes[0].rect.x, self.input_boxes[0].rect.y - 20))
                text2 = FONT.render('Шанс мутации', True, white)
                self.screen.blit(text2,
                                 (self.input_boxes[1].rect.x, self.input_boxes[1].rect.y - 20))
                text3 = FONT.render('Кол-во поколений', True, white)
                self.screen.blit(text3,
                                 (self.input_boxes[2].rect.x, self.input_boxes[2].rect.y - 20))

                pygame.draw.rect(self.screen, yellow, self.button_start)
                text = FONT.render('Начать', True, black)
                self.screen.blit(text,
                                 (self.button_start.x + 65, self.button_start.y + 7))

                pygame.draw.rect(self.screen, yellow, self.button_back)
                text = FONT.render('Назад', True, black)
                self.screen.blit(text,
                                 (self.button_back.x + 65, self.button_back.y + 7))

                # если параметр не умещается в длину поля для ввода данных
                for box in self.input_boxes:
                    box.update()

                # вывод на экран полей для ввода параметров
                for box in self.input_boxes:
                    box.draw(self.screen)

            for i in range(len(self.input_boxes)):
                self.data[i] = self.input_boxes[i].get_data()

            pygame.display.update()
            self.clock.tick(30)


class GameMenu(Menu):
    def __init__(self, screen, params):
        print('running options menu')
        Menu.__init__(self, screen)
        self.r = 250
        self.R = 330
        self.population_size = params[0]
        self.mutation_chance = params[1]
        self.generation_limit = params[2]
        self.cars = []
        for i in range(self.population_size):
            self.cars.append(Car(40, self.R - 10, screen, self.mutation_chance))
        self.dt = 0.01
        self.generation_counter = 1

    def run(self):
        while True:
            # разметка
            pygame.draw.circle(self.screen, (255, 0, 0), (self.R, self.R), self.R, width=2)
            pygame.draw.circle(self.screen, (255, 0, 0), (self.R, self.R), self.r, width=2)
            pygame.draw.line(self.screen, 'red', (0, self.R), (self.R, self.R))
            pygame.draw.line(self.screen, 'red', (self.R, 0), (self.R, self.R))

            self.draw_text(f'Поколение: {self.generation_counter}/{self.generation_limit}', 15, 100, 10)
            # обновление
            self.clock.tick(round(1 // self.dt))

            all_dead = True  # флаг того, что живых не осталось
            for car in self.cars:
                car.update(self.dt)
                if car.is_dead is False:
                    all_dead = False
            if all_dead is True:
                self.generation_counter += 1
                if self.generation_counter > self.generation_limit:
                    return 1

                self.cars.sort()

                best_car1, best_car2 = self.cars[len(self.cars) - 1], self.cars[len(self.cars) - 2]
                best_car1.color = 'red'
                best_car2.color = 'red'
                for c in (best_car2, best_car1):
                    c.update(self.dt)  # чтобы цвет поменялся
                pygame.display.update()
                for i in range(len(self.cars)):
                    self.cars[i] = Car(40, self.R - 10, self.screen, self.mutation_chance)
                    self.cars[i].genes = best_car1.genes.crossover(best_car2.genes)
                for car in self.cars:
                    car.genes.mutate()
            pygame.display.update()
            self.screen.fill('black')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 1


if __name__ == '__main__':
    print('This module is not for direct call!')
