import pygame
import random

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the game window
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

# Set up the game clock
CLOCK = pygame.time.Clock()

# Define the paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        self.rect.y -= pixels
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += pixels
        if self.rect.y > WINDOW_HEIGHT - self.rect.height:
            self.rect.y = WINDOW_HEIGHT - self.rect.height

# Define the ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.velocity = [random.choice([-8, 8]), random.randint(-8, 8)]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        if self.rect.y < 0 or self.rect.y > WINDOW_HEIGHT - self.rect.height:
            self.velocity[1] = -self.velocity[1]

    def collide_paddle(self):
        self.velocity[0] = -self.velocity[0]

# Create the sprites
all_sprites = pygame.sprite.Group()
paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 20
paddle1.rect.y = 250
paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = WINDOW_WIDTH - 30
paddle2.rect.y = 250
ball = Ball(WHITE, 10, 10)
ball.rect.x = WINDOW_WIDTH // 2
ball.rect.y = WINDOW_HEIGHT // 2

all_sprites.add(paddle1, paddle2, ball)

# Define the main game loop
def game_loop():
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        # Move the paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_up(5)
        if keys[pygame.K_s]:
            paddle1.move_down(5)
        if keys[pygame.K_UP]:
            paddle2.move_up(5)
        if keys[pygame.K_DOWN]:
            paddle2.move_down(5)

        # Update the ball position
        ball.update()

        # Handle ball collisions
        if pygame.sprite.collide_rect(ball, paddle1) or pygame.sprite.collide_rect(ball, paddle2):
            ball.collide_paddle()

        # Draw everything on the screen
        WINDOW.fill(BLACK)
        pygame.draw.rect(WINDOW, WHITE, [0, 0, WINDOW_WIDTH])
