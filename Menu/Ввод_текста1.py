import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((400, 400))

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


def main():
    clock = pygame.time.Clock()

    input_box1 = InputBox(100, 130, 140, 25)
    input_box2 = InputBox(100, 200, 140, 25)
    input_box3 = InputBox(100, 270, 140, 25)
    input_boxes = [input_box1, input_box2, input_box3]

    button_rect = pygame.Rect(100, 320, 140, 25)
    data = []

    done = False

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                # если нажали на кнопку начать игру
                if button_rect.collidepoint(event.pos):
                    for box in input_boxes:
                        data.append(box.get_data())

                    print(data)

            for box in input_boxes:
                box.handle_event(event)

        screen.fill((30, 30, 30))
        text = TITLE.render('Название игры', True, white)
        screen.blit(text, (input_box1.rect.x, input_box1.rect.y - 90))
        text_ = FONT.render('Введите параметры для игры .........', True, white)
        screen.blit(text_, (input_box1.rect.x, input_box1.rect.y - 60))

        text1 = FONT.render('Параметр 1', True, white)
        screen.blit(text1, (input_box1.rect.x, input_box1.rect.y - 20))
        text2 = FONT.render('Параметр 2', True, white)
        screen.blit(text2, (input_box1.rect.x, input_box2.rect.y - 20))
        text1 = FONT.render('Параметр 3', True, white)
        screen.blit(text1, (input_box3.rect.x, input_box3.rect.y - 20))

        rect(screen, yellow, button_rect)
        text_ = FONT.render('Начать игру', True, black)
        screen.blit(text_, (button_rect.x + 35, button_rect.y + 7))

        # если параметр не умещается в длину поля для ввода данных
        for box in input_boxes:
            box.update()

        # вывод на экран полей для ввода параметров
        for box in input_boxes:
            box.draw(screen)

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pygame.quit()
