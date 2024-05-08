import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
FPS = 60

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, (self.x, self.y - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT))

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 5
        self.dy = 5

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def bounce_off_wall(self):
        if self.y < 0 or self.y > HEIGHT:
            self.dy *= -1

    def bounce_off_paddle(self, paddle):
        if self.x < paddle.x + PADDLE_WIDTH and paddle.y - PADDLE_HEIGHT / 2 < self.y < paddle.y + PADDLE_HEIGHT / 2:
            self.dx *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), BALL_RADIUS)

def main():
    paddle1 = Paddle(0, HEIGHT / 2)
    paddle2 = Paddle(WIDTH - PADDLE_WIDTH, HEIGHT / 2)
    ball = Ball(WIDTH / 2, HEIGHT / 2)

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Move the paddles
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move_up()
        if keys[pygame.K_s]:
            paddle1.move_down()
        if keys[pygame.K_UP]:
            paddle2.move_up()
        if keys[pygame.K_DOWN]:
            paddle2.move_down()

        # Move the ball
        ball.move()

        # Bounce the ball off the walls
        ball.bounce_off_wall()

        # Bounce the ball off the paddles
        ball.bounce_off_paddle(paddle1)
        ball.bounce_off_paddle(paddle2)

        # Draw everything
        screen.fill(BLACK)
        paddle1.draw(screen)
        paddle2.draw(screen)
        ball.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

if __name__ == '__main__':
    main()