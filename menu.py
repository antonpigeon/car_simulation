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
TITLE = pygame.font.Font(None, 37)
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

    def draw_text(self, text, size, x, y, color = (0, 0, 0)):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
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


if __name__ == '__main__':
    print('This module is not for direct call!')