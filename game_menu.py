from menu import Menu
from car import Car
import pygame


class GameMenu(Menu):
    def __init__(self, screen, params):
        print('running options menu')
        Menu.__init__(self, screen)
        self.r = 250
        self.R = 330
        self.population_size = params[0]
        self.mutation_chance = params[1]
        self.generation_limit = params[2]
        self.cars = []
        for i in range(int(self.population_size)):
            self.cars.append(Car(40, self.R - 10, screen, self.mutation_chance))
        self.dt = 0.01
        self.generation_counter = 1

    def run(self):
        while True:
            # разметка
            pygame.draw.circle(self.screen, (255, 0, 0), (self.R, self.R), self.R, width=2)
            pygame.draw.circle(self.screen, (255, 0, 0), (self.R, self.R), self.r, width=2)
            pygame.draw.line(self.screen, 'red', (0, self.R), (self.R, self.R))
            pygame.draw.line(self.screen, 'red', (self.R, 0), (self.R, self.R))

            self.draw_text(f'Generation: {self.generation_counter}', 15, 30, 10)
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
