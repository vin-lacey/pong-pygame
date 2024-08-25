import pygame

# Initialize the game
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font("PressStart2P-Regular.ttf", 36)

player1 = pygame.Rect(50, 250, 20, 100)
player2 = pygame.Rect(730, 250, 20, 100)
ball = pygame.Rect(390, 290, 20, 20)

pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("pong.png"))

# Set up the colors
WHITE = (250, 250, 250)
BLACK = (55, 55, 55)

# Set up the game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)
    # Scores for the players
    player1_score = font.render("0", True, WHITE)
    player2_score = font.render("0", True, WHITE)
    screen.blit(player1_score, (300, 50))
    screen.blit(player2_score, (500, 50))

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        player1.y -= 10
    if key[pygame.K_s]:
        player1.y += 10
    # player1 wall collision
    if player1.y <= 0:
        player1.y = 0
    if player1.y >= 500:
        player1.y = 500

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.update()
pygame.quit()
