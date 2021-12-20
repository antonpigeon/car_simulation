import pygame

from draw_menu import DrawMenu
from main_menu import MainMenu
from options_menu import OptionsMenu
from game_menu import GameMenu
pygame.init()


class Game:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.BLACK, self.WHITE = (30, 30, 30), (255, 255, 255)
        self.options_params = [100, 0.001, 20]  # Параметры options: размер популяции, шанс мутации, кол-во поколений
        self.is_demo = True
        self.main_menu = MainMenu(self.window)
        self.draw_menu = DrawMenu(self.window)
        self.options_menu = OptionsMenu(self.window)
        self.game_menu = GameMenu(self.window)
        self.curr_menu = self.main_menu

    def run_menus(self):
        while True:
            self.window.fill((30, 30, 30))
            to_run = self.curr_menu.run()  # Меню делает свои дела и возвращает, к какому меню перейти
            assert type(to_run) is int
            if to_run == 0:
                pygame.quit()
                break
            elif to_run == 1:
                self.curr_menu = self.main_menu
            elif to_run == 2:
                self.curr_menu = self.options_menu
            elif to_run == 3:
                self.game_menu.road = self.draw_menu.fitness_list
                self.game_menu.road_width = self.draw_menu.road_width
                self.game_menu.is_demo = self.main_menu.is_demo
                self.game_menu.params = self.options_menu.data
                self.game_menu.fitness = self.draw_menu.fitness
                self.game_menu.reset()
                self.curr_menu = self.game_menu
            elif to_run == 4:
                self.draw_menu.reset()
                self.curr_menu = self.draw_menu


if __name__ == '__main__':
    screen = pygame.display.set_mode((700, 700))
    g = Game(screen)
    g.run_menus()
