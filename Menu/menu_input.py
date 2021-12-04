import pygame


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2

        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 30, self.cursor_rect.x + 10,
                            self.cursor_rect.y + 5)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 10
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 30
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Название игры', 27, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text("Начать игру", 20, self.startx, self.starty)
            self.game.draw_text("Задать параметры", 20, self.optionsx,
                                self.optionsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            self.run_display = False


class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Param1'
        self.param1x, self.param1y = self.mid_w, self.mid_h - 60
        self.param2x, self.param2y = self.mid_w, self.mid_h
        self.param3x, self.param3y = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.param1x + self.offset, self.param1y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((30, 30, 30))
            self.game.draw_text('Параметры игры', 27, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text("Параметр 1", 20, self.param1x, self.param1y)
            self.game.draw_rect((255, 255, 0), (self.param1x - 50, self.param1y + 15, 100, 20))

            self.game.draw_text("Параметр 2", 20, self.param2x, self.param2y)
            self.game.draw_rect((255, 255, 0),
                                (self.param2x - 50, self.param2y + 15, 100, 20))
            self.game.draw_text("Параметр 3", 20, self.param3x, self.param3y)
            self.game.draw_rect((255, 255, 0),
                                (self.param3x - 50, self.param3y + 15, 100, 20))

            self.draw_cursor()
            self.blit_screen()


    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.DOWN_KEY:
            if self.state == 'Param1':
                self.state = 'Param2'
                self.cursor_rect.midtop = (
                    self.param2x + self.offset, self.param2y)
            elif self.state == 'Param2':
                self.state = 'Param3'
                self.cursor_rect.midtop = (
                self.param3x + self.offset, self.param3y)
        elif self.game.UP_KEY:
            if self.state == 'Param3':
                self.state = 'Param2'
                self.cursor_rect.midtop = (
                    self.param2x + self.offset, self.param2y)
            elif self.state == 'Param2':
                self.state = 'Param1'
                self.cursor_rect.midtop = (
                self.param1x + self.offset, self.param1y)
