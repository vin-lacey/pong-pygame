from numpy import random
import pygame, sys

def ball_animation(player_score, ai_score):
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.left <= 0:
        ai_score += 1
        reset_ball()

    if ball.right >= SCREEN_WIDTH:
        player_score += 1
        reset_ball()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

    return player_score, ai_score

def ai(opponent):
    ai_speed = random.randint(1, 10)
    if opponent.top < ball.y:
        opponent.y += ai_speed
    if opponent.bottom > ball.y:
        opponent.y -= ai_speed

def reset_ball():
    global ball_speed_x, ball_speed_y
    ball.x = SCREEN_WIDTH // 2 - 6
    ball.y = SCREEN_HEIGHT // 2 - 15
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))
    pygame.time.wait(1000)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

def start_screen():
    screen.fill(BLACK)
    draw_text('PONG', font_large, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
    draw_text('Press SPACE to Start', font_small, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    pygame.display.flip()

def game_over_screen(winner):
    screen.fill(BLACK)
    draw_text(f'{winner} Wins!', font_large, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
    draw_text('Press SPACE to Restart', font_small, WHITE, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
    pygame.display.flip()

pygame.init()
clock = pygame.time.Clock()
player_score = 0
ai_score = 0
game_active = False
game_over = False

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
FPS = 60
WHITE = (245, 245, 245)
BLACK = (50, 50, 50)
font_large = pygame.font.Font("assets/PressStart2P-Regular.ttf", 72)
font_small = pygame.font.Font("assets/PressStart2P-Regular.ttf", 36)
font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 36)
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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_over:
                    player_score = 0
                    ai_score = 0
                    game_over = False
                game_active = True

    if not game_active:
        start_screen()
    elif game_over:
        game_over_screen('Player' if player_score == 15 else 'AI')
    else:
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and player.top > 0:
            player.y -= paddle_speed
        if key[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
            player.y += paddle_speed

        player_score, ai_score = ball_animation(player_score, ai_score)
        ai(opponent)

        if player_score >= 15 or ai_score >= 15:
            game_active = False
            game_over = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, WHITE, opponent)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

        # Adjusted positions for scores
        player_text = font.render(f"{player_score}", False, WHITE)
        screen.blit(player_text, (SCREEN_WIDTH // 2 - 100, 10))

        ai_text = font.render(f"{ai_score}", False, WHITE)
        screen.blit(ai_text, (SCREEN_WIDTH // 2 + 75, 10))

        pygame.display.flip()
        clock.tick(FPS)
