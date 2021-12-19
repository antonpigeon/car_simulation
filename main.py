from menus import *
pygame.init()
from DrawMenu import DrawMenu

class Game:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.BLACK, self.WHITE = (30, 30, 30), (255, 255, 255)
        self.curr_menu = MainMenu(self.window)
        self.options_params = [100, 0.001, 20]  # Параметры options: размер популяции, шанс мутации, кол-во поколений

    def run_menus(self):
        while True:
            self.window.fill((30, 30, 30))
            to_run = self.curr_menu.run()  # Меню делает свои дела и возвращает, к какому меню перейти
            # print(to_run)
            assert type(to_run) is int
            if to_run == 0:
                pygame.quit()
                break
            elif to_run == 1:
                self.curr_menu = MainMenu(self.window)
            elif to_run == 2:
                self.curr_menu = OptionsMenu(self.window, self.options_params)
            elif to_run == 3:
                self.curr_menu = GameMenu(self.window, self.options_params)
            elif to_run == 4:
                self.curr_menu = DrawMenu(self.window)


if __name__ == '__main__':
    screen = pygame.display.set_mode((700, 700))
    g = Game(screen)
    g.run_menus()
