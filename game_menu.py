from menu import Menu, white
from car import Car
import pygame


class GameMenu(Menu):
    def __init__(self, screen):
        Menu.__init__(self, screen)
        self.is_demo = True
        self.road = [[False] * 700] * 700
        self.road_width = 20
        self.road_color = (40, 40, 40)
        self.offroad_color = (0, 200, 0)
        self.r = 250
        self.R = 330
        self.params = [100, 0.001, 20]
        self.population_size = self.params[0]
        self.mutation_chance = self.params[1]
        self.generation_limit = self.params[2]
        self.cars = []
        self.pixel_list = []
        for i in range(700):
            self.pixel_list.append([False]*700)
        for i in range(int(self.population_size)):
            self.cars.append(Car(40, self.R - 20, screen, self.mutation_chance))
        self.dt = 0.01
        self.generation_counter = 1

    def fitness(self, car_x, car_y):
        print("aaaaaaa!!!!!!!")
        return car_x*0 + car_y*0  # просто дефолтная штука, не используется

    def fitness1(self, car):
        return self.fitness(car.x, car.y)  # просто дефолтная штука, не используется

    def reset(self):
        self.cars = []
        for i in range(int(self.population_size)):
            self.cars.append(Car(40, self.R - 10, self.screen, self.mutation_chance))
        self.generation_counter = 1
        self.population_size = self.params[0]
        self.mutation_chance = self.params[1]
        self.generation_limit = self.params[2]

    def draw_road(self):
        self.screen.fill(self.offroad_color)
        for [x, y] in self.road:
            pygame.draw.circle(self.screen, self.road_color, (x, y), self.road_width)

    def draw_road1(self):
        for i in range(700):
            for j in range(700):
                if self.pixel_list[i][j] is True:
                    pygame.draw.line(self.screen, 'red', (i, j), (i, j))

    def check_pixels(self):
        for [x0, y0] in self.road:
            for i in range(x0 - self.road_width, x0 + self.road_width + 1):
                for j in range(y0 - self.road_width, y0 + self.road_width + 1):
                    try:
                        if (i - x0) ** 2 + (j - y0) ** 2 <= self.road_width ** 2:
                            self.pixel_list[i][j] = True
                        # else:
                            # self.pixel_list[i][j] = False
                    except IndexError:
                        pass

    def is_alive(self, car_x, car_y):
        return self.pixel_list[int(car_x)][int(car_y)]

    def run(self):
        if self.is_demo:
            # то, что было
            finished = False
            while not finished:
                # разметка
                pygame.draw.circle(self.screen, (255, 0, 0), (self.R, self.R), self.R, width=2)
                pygame.draw.circle(self.screen, (255, 0, 0), (self.R, self.R), self.r, width=2)
                pygame.draw.line(self.screen, 'red', (0, self.R), (100, self.R))

                self.draw_text(f'Поколение: {self.generation_counter}/{self.generation_limit}', 15, 50, 20, white)
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
                        finished = True
                        break

                    self.cars.sort()

                    best_car1, best_car2 = self.cars[len(self.cars) - 1], self.cars[len(self.cars) - 2]
                    best_car1.color = 'red'
                    best_car2.color = 'red'
                    for c in (best_car2, best_car1):
                        c.update(self.dt)  # чтобы цвет поменялся
                    pygame.display.update()
                    for i in range(len(self.cars)):
                        self.cars[i] = Car(40, self.R - 20, self.screen, self.mutation_chance)
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
        else:
            self.check_pixels()
            while True:
                # разметка
                self.draw_road()
                self.draw_text(f'Поколение: {self.generation_counter}/{self.generation_limit}', 15, 50, 20, white)
                # обновление
                self.clock.tick(round(1 // self.dt))

                all_dead = True  # флаг того, что живых не осталось
                for car in self.cars:
                    car.is_dead = False if self.is_alive(car.x, car.y) is True else True
                    car.update(self.dt)
                    if car.is_dead is False:
                        all_dead = False
                if all_dead is True:
                    self.generation_counter += 1
                    if self.generation_counter > self.generation_limit:
                        finished = True
                        break
                    self.cars.sort(key=self.fitness1)

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

            results_box = pygame.Rect(200, 200, 300, 300)
            pygame.draw.rect(self.screen, (0, 0, 0), results_box)
            pygame.draw.rect(self.screen, (255, 255, 255), results_box, width=2)
            self.draw_text('Симуляция завершена!', 15, 350, 350, (255, 255, 255))
            button_back = pygame.Rect(300, 380, 100, 30)
            pygame.draw.rect(self.screen, (255, 255, 0), button_back)
            self.draw_text("главное меню", 15, 350, 395)
            while True:
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if button_back.collidepoint(event.pos):
                            return 1
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            return 0
