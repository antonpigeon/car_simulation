import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

# ------------------------------------------------------------

red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)
colors = [red, blue, yellow, green, magenta, cyan]

screen.fill(white)

base_font = pygame.font.Font(None, 18)
user_text = ''
param1 = ''

input_rect = pygame.Rect(150, 150, 130, 25)
button_rect = pygame.Rect(150, 185, 100, 25)
active = False

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

            if button_rect.collidepoint(event.pos):
                param1 = user_text
                print(f'Параметр 1: {param1}')
                user_text = ''

        if event.type == pygame.KEYDOWN:
            if active:
                # Действие при нажатии на кнопку Enter
                # if event.key == pygame.K_RETURN:
                #     param1 = user_text
                #     print(f'Параметр 1: {param1}')
                #     user_text = ''

                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

    text_title = base_font.render('Параметр 1', True, black)
    screen.blit(text_title, (input_rect.x + 2, input_rect.y - 15))

    text_surface = base_font.render(user_text, True, black)
    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 7))

    rect(screen, black, input_rect, 1)
    input_rect.w = max(100, text_surface.get_width())

    rect(screen, yellow, button_rect)
    text_ = base_font.render('Ввод', True, black)
    screen.blit(text_, (button_rect.x + 5, button_rect.y + 7))

    pygame.display.update()
    screen.fill(white)

pygame.quit()
