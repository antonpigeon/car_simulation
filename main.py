import pygame
import random
from car import *
pygame.init()

r = 250
R = 330

screen = pygame.display.set_mode((700, 700))

population_size = 100
cars = []
for i in range(population_size):
    cars.append(Car(40, R - 10, screen))
finished = False
clock = pygame.time.Clock()
dt = 0.01
generation_counter = 1
while not finished:
    # разметка
    pygame.draw.circle(screen, (255, 0, 0), (R, R), R, width=2)
    pygame.draw.circle(screen, (255, 0, 0), (R, R), r, width=2)
    pygame.draw.line(screen, 'red', (0, R), (R, R))
    pygame.draw.line(screen, 'red', (R, 0), (R, R))
    # обновление
    clock.tick(1 // dt)

    all_dead = True  # флаг того, что живых не осталось
    for car in cars:
        car.update(dt)
        if car.is_dead is False:
            all_dead = False
    if all_dead is True:
        generation_counter += 1
        print(f'generation: {generation_counter}')

        cars.sort()

        best_car1, best_car2 = cars[len(cars) - 1], cars[len(cars) - 2]
        best_car1.color = 'red'
        best_car2.color = 'red'
        for c in (best_car2, best_car1):
            c.update(dt)  # чтобы цвет поменялся
        pygame.display.update()
        for i in range(len(cars)):
            cars[i] = Car(40, R - 10, screen)
            cars[i].genes = best_car1.genes.crossover(best_car2.genes)
        for car in cars:
            car.genes.mutate()
    pygame.display.update()
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                finished = True
