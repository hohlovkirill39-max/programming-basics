import pygame

class Ball:
    def __init__(self, x, y, r, color="red", vx=3, vy=3):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 1
        if (self.x + self.r > WIDTH) or (self.x < self.r):
            self.vx = -self.vx
        if (self.y + self.r > HEIGHT) or (self.y < self.r):
            self.vy = -0.9*self.vy

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            self.color, 
            (self.x, self.y), 
            self.r
        )

pygame.init()

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)

WIDTH, HEIGHT = screen.get_size()

clock = pygame.time.Clock()

from random import randint, choice

colors = ["red", "blue", "yellow", 'pink', 'magenta', 'green']

def new_ball():
    return Ball(
            randint(100, WIDTH - 100),
            randint(100, HEIGHT - 100),
            randint(10, 30),
            choice(colors),
            randint(-5, 5),
            randint(-5, 5)) 

balls = [ new_ball() for _ in range(50) ]
FPS = 60
finished = False
while not finished:
    clock.tick(FPS)
    screen.fill(choice(colors))
    
    for b in balls:
        b.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                balls.append(new_ball())
            if event.key == pygame.K_p:
                balls.pop()
            if event.key == pygame.K_c:
                balls.clear()
            if event.key == pygame.K_KP_PLUS:
                FPS += 10
            if event.key == pygame.K_KP_MINUS:
                if FPS > 10:
                    FPS -= 10
            


    for b in balls:
        b.move()

pygame.quit()
