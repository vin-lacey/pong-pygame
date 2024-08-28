from numpy import random
import pygame, sys

def ball_animation():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
        ball.x = SCREEN_WIDTH // 2 - 6
        ball.y = SCREEN_HEIGHT // 2 - 15
        pygame.time.wait(2000)
        ball_speed_x *= -1


    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def ai(opponent):
    # AI logic
    ai_speed = random.randint(1, 10)
    if opponent.top < ball.y:
        opponent.y += ai_speed
    if opponent.bottom > ball.y:
        opponent.y -= ai_speed


pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
FPS = 60
WHITE = (245, 245, 245)
BLACK = (50, 50, 50)

ball_speed_x = 7
ball_speed_y = 7
paddle_speed = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

ball = pygame.Rect(SCREEN_WIDTH // 2 - 6, SCREEN_HEIGHT // 2 - 15, 15, 15)
opponent = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - 70, 15, 140)
player = pygame.Rect(10, SCREEN_HEIGHT // 2 - 70, 15, 140)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and player.top > 0:
        player.y -= paddle_speed
    if key[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
        player.y += paddle_speed

    ball_animation()
    ai(opponent)

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, opponent)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)
