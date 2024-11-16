import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        rand_x = 0
        rand_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = event.pos
                    if rand_x < click[0] < rand_x + 32 and rand_y < click[1] < rand_y + 32:
                        rand_x = random.randrange(0, 640, 32)
                        rand_y = random.randrange(0, 512, 32)
            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(rand_x, rand_y)))
            for i in range(0, 640, 32):
                pygame.draw.line(screen, "black", (i, 0), (i, 512)) # draws vertical lines
            for j in range(32, 512, 32):
                pygame.draw.line(screen, "black", (0, j), (640, j)) # draws horizontal lines
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
