import pygame
import random

pygame.init()
screen_x,screen_y=800,600
screen = pygame.display.set_mode((screen_x,screen_y))

class Snake:

    def __init__(self):
       self.size =1
       self.x = 100
       self.y = 100
       self.elements =[[100,100],[80,100],[60,100]]
       self.head = [self.x,self.y]
       self.radius =10
       self.dx =10
       self.dy=0

    def animation(self,food_x,food_y,food_radius):
        self.elements.insert(0,list(self.head))
        if not((self.x-food_x)**2 + (self.y - food_y)**2<=(self.radius+food_radius)**2    ):
            self.elements.pop()
        else:
            return 1
    
    def move(self):
        self.x +=self.dx
        self.y +=self.dy
        self.head = [self.x,self.y]
        if self.x<self.radius*2:
            self.x=self.radius*2
        if self.y<self.radius*2:
            self.y=self.radius*2
        if self.x>screen_x-self.radius*2:
            self.x=screen_x-self.radius*2
        if self.y>screen_y-self.radius*2:
            self.y=screen_y-self.radius*2        



    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen,(255,0,0),element,self.radius)
    
class Food():
    def __init__(self):
        self.x = random.randrange(0,80)*10
        self.y = random.randrange(0,60)*10
        self.size = 10
    def new(self,eat):
        if eat:
            self.x = random.randrange(0,80)*10
            self.y = random.randrange(0,60)*10
            
    def draw(self):
        #pygame.draw.rect(screen,(0,255,0),(self.x,self.y,self.size,self.size))
        pygame.draw.circle(screen, (0,255,0), (self.x,self.y), 10)

snake = Snake()

running=True

food = Food()

clock=pygame.time.Clock()
d=10
FPS =15
eat = False
while running:
    mill =clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
               running = False
            if event.key == pygame.K_RIGHT and snake.dx!=-d :
                snake.dx=d
                snake.dy=0
            if event.key == pygame.K_LEFT and snake.dx!=d :
                snake.dx=-d
                snake.dy=0
            if event.key == pygame.K_UP and snake.dy!=d :
                snake.dx=0
                snake.dy=-d
            if event.key == pygame.K_DOWN and snake.dy!=-d :
                snake.dx=0
                snake.dy=d
            if event.key == pygame.K_1:
                FPS+=5
            if event.key == pygame.K_SPACE:
                snake.dx=0
                snake.dx=0    
    snake.move()
    screen.fill((0,0,0))
    eat = snake.animation(food.x,food.y,food.size)
    food.new(eat)
    food.draw()
    snake.draw()
    eat = False
    pygame.display.update()
