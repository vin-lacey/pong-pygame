import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
FPS = 60

running = True
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font("assets/PressStart2P-Regular.ttf", 36)


pygame.init()

def main():
    while running:
        clock.tick(FPS)

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update


    pygame.quit()

if __name__ == "__main__":
    main()
