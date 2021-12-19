from menu import InputBox, Menu, FONT, white, yellow, black
import pygame


class OptionsMenu(Menu):
    def __init__(self, screen, data):
        print('running options menu')
        Menu.__init__(self, screen)
        self.button_start = pygame.Rect(250, 400, 200, 25)

        input_box1 = InputBox(250, 230, 140, 25, str(data[0]))
        input_box2 = InputBox(250, 290, 140, 25, str(data[1]))
        input_box3 = InputBox(250, 350, 140, 25, str(data[2]))
        self.input_boxes = [input_box1, input_box2, input_box3]

        self.data = data
        assert type(self.data) is list
        assert len(self.data) <= 3

    def run(self):
        while True:  # да простят меня боги
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return 0
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_start.collidepoint(event.pos):
                        print(self.data)
                        return 3

                for box in self.input_boxes:
                    box.handle_event(event)
                self.screen.fill((30, 30, 30))
                text = FONT.render('Введите параметры для игры .........',
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
                                 (self.button_start.x + 80, self.button_start.y + 7))

                # если параметр не умещается в длину поля для ввода данных
                for box in self.input_boxes:
                    box.update()

                # вывод на экран полей для ввода параметров
                for box in self.input_boxes:
                    box.draw(self.screen)

            for i in range(len(self.input_boxes)):
                self.data[i] = (float(self.input_boxes[i].get_data()))

            pygame.display.update()
            self.clock.tick(30)
