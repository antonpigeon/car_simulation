from menu import Menu, FONT, TITLE, white, yellow, black
import pygame


class MainMenu(Menu):
    def __init__(self, screen: pygame.Surface):
        Menu.__init__(self, screen)

        self.is_demo = False
        self.button_start = pygame.Rect(self.mid_w - 100, self.mid_h - 60, 200, 25)
        self.button_demo = pygame.Rect(self.mid_w - 100, self.mid_h, 200, 25)
        self.button_quit = pygame.Rect(self.mid_w - 100, self.mid_h + 60, 200, 25)

    def run(self):
        while True:  # да простят меня боги
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_start.collidepoint(event.pos):
                        self.is_demo = False
                        return 4
                    if self.button_quit.collidepoint(event.pos):
                        return 0
                    if self.button_demo.collidepoint(event.pos):
                        self.is_demo = True
                        return 2
            self.screen.fill((30, 30, 30))
            text = TITLE.render('', True, white)
            text_ = text.get_rect()
            text_.center = (self.mid_w, self.mid_h - 150)
            self.screen.blit(text, text_)

            pygame.draw.rect(self.screen, yellow, self.button_start)
            text = FONT.render('Начать', True, black)
            self.screen.blit(text, (self.button_start.x + 70, self.button_start.y + 7))

            pygame.draw.rect(self.screen, yellow, self.button_quit)
            text = FONT.render('Выйти', True, black)
            self.screen.blit(text, (self.button_quit.x + 70, self.button_quit.y + 7))

            pygame.draw.rect(self.screen, yellow, self.button_demo)
            text = FONT.render('Демонстрация', True, black)
            self.screen.blit(text, (self.button_demo.x + 70, self.button_demo.y + 7))

            pygame.display.update()
            self.clock.tick(30)
