import pygame
pygame.init()

r = 270
R = 330


class Car:
    def __init__(self, x, y, surface):
        self.surface = surface
        self.x, self.y = x, y
        self.a = 15
        self.b = 10
        self.vx = 0
        self.vy = -4
        self.lifetime = 0
        self.max_at = 1  # тангециальное
        self.max_an = 2  # нормальное
        self.at = self.max_at
        self.an = self.max_an
        self.genes = [4, 4, 4, 4, 4, 4, -1, -1, -1, -1, -1] * 100

    def draw(self):
        pygame.draw.rect(self.surface, 'yellow', (round(self.x - self.a/2), round(self.y - self.b/2),
                                                  self.a, self.b))

    def update(self, dt):
        if self.is_alive() is True:
            # self.an = self.genes[self.lifetime]
            self.an = self.max_an
            self.lifetime += 1
            self.x += self.vx
            self.y += self.vy
            v = (self.vx**2 + self.vy**2)**0.5
            self.vx += dt*(self.at*self.vx - self.an*self.vy)/v
            self.vy += -dt*(-self.at*self.vy - self.an*self.vx)/v
        self.draw()

    def is_alive(self):
        return R ** 2 > (self.x - R) ** 2 + (self.y - R) ** 2 > r ** 2


screen = pygame.display.set_mode((400, 400), pygame.FULLSCREEN)
car = Car(15, R - 10, screen)
finished = False
clock = pygame.time.Clock()
dt = 0.1
while not finished:
    # разметка
    pygame.draw.circle(screen, (255, 0, 0), (R, R), R, width=2)
    pygame.draw.circle(screen, (255, 0, 0), (R, R), r, width=2)
    pygame.draw.line(screen, 'red', (0, R), (R, R))
    pygame.draw.line(screen, 'red', (R, 0), (R, R))
    # обновление
    clock.tick(1//dt)
    car.update(dt)
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
