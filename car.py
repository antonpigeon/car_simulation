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
        self.vy = -2
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
        # пусть прямоугольник поворачивается по направлению движения
        pygame.draw.rect(self.surface, 'yellow', (round(self.x - self.a/2), round(self.y - self.b/2),
                                                  self.a, self.b))

    def update(self, dt):
        if self.is_dead is False and self.is_alive() is True:  # переменная и функция
            self.an = self.genes.an_genes[self.lifetime]       # не путать!
            self.at = self.genes.at_genes[self.lifetime]
            self.lifetime += 1
            self.x += self.vx
            self.y += self.vy
            v = (self.vx**2 + self.vy**2)**0.5
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
