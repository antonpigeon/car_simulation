from menu import Menu, FONT, TITLE, white, yellow, black
import pygame


class MainMenu(Menu):
    def __init__(self, screen: pygame.Surface):
        Menu.__init__(self, screen)
        print('Running main menu')

        self.button_options = pygame.Rect(250, 320, 200, 25)
        self.button_quit = pygame.Rect(250, 380, 200, 25)

    def run(self):
        while True:  # да простят меня боги
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_options.collidepoint(event.pos):
                        return 4
                    if self.button_quit.collidepoint(event.pos):
                        return 0
            self.screen.fill((30, 30, 30))
            text = TITLE.render('Машины хаха', True, white)
            text_ = text.get_rect()
            text_.center = (self.mid_w, self.mid_h - 150)
            self.screen.blit(text, text_)

            pygame.draw.rect(self.screen, yellow, self.button_options)
            text = FONT.render('Начать', True, black)
            self.screen.blit(text, (self.button_options.x + 70, self.button_options.y + 7))

            pygame.draw.rect(self.screen, yellow, self.button_quit)
            text = FONT.render('Выйти', True, black)
            self.screen.blit(text, (self.button_quit.x + 70, self.button_quit.y + 7))

            pygame.display.update()
            self.clock.tick(30)
