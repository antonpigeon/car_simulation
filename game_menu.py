from menu import Menu, white
from car import Car
import pygame


class GameMenu(Menu):
    def __init__(self, screen):
        print('running game menu')
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
        for i in range(int(self.population_size)):
            self.cars.append(Car(40, self.R - 10, screen, self.mutation_chance))
        self.dt = 0.01
        self.generation_counter = 1

    def reset(self):
        self.cars = []
        for i in range(int(self.population_size)):
            self.cars.append(Car(40, self.R - 10, self.screen, self.mutation_chance))
        self.generation_counter = 1

    def draw_road(self):
        self.screen.fill(self.offroad_color)
        for (x, y) in self.road:
            pygame.draw.circle(self.screen, self.road_color, (x, y), self.road_width)

    def run(self):
        if self.is_demo:
            # то, что было
            while True:
                # разметка
                pygame.draw.circle(self.screen, (255, 0, 0), (self.R, self.R), self.R, width=2)
                pygame.draw.circle(self.screen, (255, 0, 0), (self.R, self.R), self.r, width=2)
                pygame.draw.line(self.screen, 'red', (0, self.R), (self.R, self.R))
                pygame.draw.line(self.screen, 'red', (self.R, 0), (self.R, self.R))

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
                        return 1

                    self.cars.sort()

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
        else:
            while True:
                # разметка
                self.draw_road()
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
                        return 1

                    self.cars.sort()

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
