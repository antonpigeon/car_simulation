import pygame
from genetics import *
pygame.init()


class Car:
    def __init__(self, x, y, surface):
        self.surface = surface
        self.x, self.y = x, y
        self.a = 25
        self.b = 10
        self.vx = 0
        self.vy = -1
        self.lifetime = 0
        self.max_at = 0  # тангециальное
        self.max_an = 0  # нормальное
        self.at = self.max_at
        self.an = self.max_an
        self.genes = Genes()
        self.is_dead = False

    def draw(self):
        """
        рисует машину (прямоугольник)
        """
        # FIXME: пусть прямоугольник поворачивается по направлению движения
        pygame.draw.rect(self.surface, 'yellow', (round(self.x - self.a/2), round(self.y - self.b/2),
                                                  self.a, self.b))
    def curvature(self):
        v = (self.vx ** 2 + self.vy ** 2) ** 0.5
        ax = (self.at * self.vx - self.an * self.vy) / (v + 0.0000001)
        ay = -(-self.at * self.vy - self.an * self.vx) / (v + 0.00000001)
        k = (abs(self.vx * ay - self.vy * ax)) / ((self.vx**2 + self.vy**2) ** 1.5)
        return k

    def update(self, dt):
        if self.is_dead is False and self.is_alive() is True:  # переменная и функция не путать!
            v = (self.vx**2 + self.vy**2)**0.5
            k = self.curvature()
            an_max = (v ** 2) * k
            if self.genes.an_genes[self.lifetime] < 0 :
                self.an = abs(max(self.genes.an_genes[self.lifetime], an_max, 10)) * (-1)
            else:
                self.an = abs(max(self.genes.an_genes[self.lifetime], an_max, 10))
            if v < 2:
                abs_mod = min(abs(self.an), 5)
                if self.genes.an_genes[self.lifetime] < 0:
                    self.an = -abs_mod
                else:
                    self.an = abs_mod
            self.at = self.genes.at_genes[self.lifetime]
            self.lifetime += 1
            self.x += self.vx
            self.y += self.vy
            self.vx += dt*(self.at*self.vx - self.an*self.vy)/(v + 0.0000001)
            self.vy += dt*(self.at*self.vy + self.an*self.vx)/(v + 0.00000001)
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
        return self.fitness() < other_car.fitness()


if __name__ == '__main__':
    print('this module is not for direct call!')
