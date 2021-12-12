import pygame
from genetics import *
pygame.init()


class CarGenesTooShortError(Exception):
    def __init__(self, genome_length, car_x, car_y):
        self.genome_length = genome_length
        self.x = car_x
        self.y = car_y

    def __str__(self):
        return f"Genome length of {self.genome_length} is not enough for car at {self.x}, {self.y}! " \
               f"Stopping simulation."


class Car:
    def __init__(self, x, y, surface, mutation_chance, color='yellow'):
        self.surface = surface
        self.x, self.y = x, y
        self.color = color
        self.a = 25
        self.b = 10
        self.vx = 0
        self.vy = -1
        self.lifetime = 0
        self.max_at = 0  # тангециальное
        self.max_an = 0  # нормальное
        self.at = self.max_at
        self.an = self.max_an
        self.genes = Genes(mutation_chance)
        self.is_dead = False

    def __str__(self):
        return f"Car at {(self.x, self.y)}, lived for {self.lifetime}, is now " + "dead" if self.is_dead else "alive"

    def draw(self):
        """
        рисует машину (прямоугольник)
        """
        cos = self.vx / (self.vx ** 2 + self.vy ** 2) ** 0.5
        sin = self.vy / (self.vx ** 2 + self.vy ** 2) ** 0.5
        Ax = self.x + (-self.a / 2) * cos - (self.b / 2) * sin
        Bx = self.x + (self.a / 2) * cos - (self.b / 2) * sin
        Cx = self.x + (self.a / 2) * cos - (-self.b / 2) * sin
        Dx = self.x + (-self.a / 2) * cos - (-self.b / 2) * sin
        Ay = self.y + (-self.a / 2) * sin + (self.b / 2) * cos
        By = self.y + (self.a / 2) * sin + (self.b / 2) * cos
        Cy = self.y + (self.a / 2) * sin + (-self.b / 2) * cos
        Dy = self.y + (-self.a / 2) * sin + (-self.b / 2) * cos
        pygame.draw.polygon(self.surface, self.color, [(Ax, Ay), (Bx, By), (Cx, Cy), (Dx, Dy)])

    def curvature(self):
        v = (self.vx ** 2 + self.vy ** 2) ** 0.5
        ax = (self.at * self.vx - self.an * self.vy) / (v + 0.0000001)
        ay = -(-self.at * self.vy - self.an * self.vx) / (v + 0.00000001)
        k = (abs(self.vx * ay - self.vy * ax)) / ((self.vx ** 2 + self.vy ** 2) ** 1.5)
        return k

    def update(self, dt):
        if self.is_dead is False and self.is_alive() is True:  # переменная и функция не путать!
            v = (self.vx**2 + self.vy**2) ** 0.5
            k = self.curvature()
            an_max = (v ** 2) * k
            try:
                if self.genes.an_genes[self.lifetime] < 0:
                    if self.lifetime > 0:
                        self.an = (min(abs(self.genes.an_genes[self.lifetime]), an_max)) * (-1)
                    else:
                        self.an = self.genes.an_genes[self.lifetime]
                else:
                    if self.lifetime > 0:
                        self.an = (max(self.genes.an_genes[self.lifetime], an_max))
                    else:
                        self.an = self.genes.an_genes[self.lifetime]
                if v < 2:
                    abs_mod = min(abs(self.an), 5)
                    if self.genes.an_genes[self.lifetime] < 0:
                        self.an = -abs_mod
                    else:
                        self.an = abs_mod
                self.at = self.genes.at_genes[self.lifetime]
            except IndexError:
                self.color = 'blue'
                self.draw()
                pygame.display.update()
                pygame.time.wait(500)
                raise CarGenesTooShortError(self.genes.genome_length, self.x, self.y)
            self.lifetime += 1
            self.x += self.vx
            self.y += self.vy
            if v != 0:
                self.vx += dt*(self.at*self.vx - self.an*self.vy)/(v + 0.0000001)
                self.vy += dt*(self.at*self.vy + self.an*self.vx)/(v + 0.00000001)
            else:
                self.vx += dt * (abs(self.at) * self.vx - self.an * self.vy) / (v + 0.0000001)
                self.vy += dt * (abs(self.at) * self.vy + self.an * self.vx) / (v + 0.00000001)
        else:
            self.is_dead = True
        self.draw()

    def is_alive(self, R=330, r=250):
        return R ** 2 > (self.x - R) ** 2 + (self.y - R) ** 2 > r ** 2

    def fitness(self, R=330):
        """
        оценивает успешность машины
        пока просто по расстоянию
        """
        return self.x**2 + (self.y - R)**2

    def __lt__(self, other_car):
        """
        метод переопределяет оператор "меньше" для класса Car
        """
        diff = self.fitness() - other_car.fitness()
        if abs(diff) > 5:
            return diff < 0
        else:
            return self.lifetime > other_car.lifetime


if __name__ == '__main__':
    print('This module is not for direct call!')
