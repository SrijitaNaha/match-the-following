import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36
FONT_NAME = "Times New Roman"

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Load images
images = {
    "subway_surfer": pygame.image.load("subwaysurfer.png"),
    "ludo": pygame.image.load("ludo.png"),
    "temple_run": pygame.image.load("templerun.png"),
    "candy_crush": pygame.image.load("candycrush.jpg")
}

# Set up font
font = pygame.font.SysFont(FONT_NAME, FONT_SIZE)

# Set up text
texts = {
    "ludo": font.render("Ludo", True, BLACK),
    "candy_crush": font.render("Candy Crush", True, BLACK),
    "subway_surfer": font.render("Subway Surfer", True, BLACK),
    "temple_run": font.render("Temple Run", True, BLACK)
}

# Set up image and text positions
positions = {
    "subway_surfer": (150, 100),
    "ludo": (150, 200),
    "temple_run": (150, 300),
    "candy_crush": (150, 400)
}
text_positions = {
    "ludo": (350, 100),
    "candy_crush": (350, 200),
    "subway_surfer": (350, 300),
    "temple_run": (350, 400)
}

# Draw everything
def draw_everything():
    screen.fill(WHITE)
    for image_name, image in images.items():
        screen.blit(image, positions[image_name])
    for text_name, text in texts.items():
        screen.blit(text, text_positions[text_name])
    pygame.display.update()

# Main loop
def main():
    clock = pygame.time.Clock()
    running = True
    last_pos = None
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                last_pos = pygame.mouse.get_pos()
                pygame.draw.circle(screen, BLACK, last_pos, 20, 0)
                pygame.display.update()
            elif event.type == pygame.MOUSEBUTTONUP:
                if last_pos:
                    pos2 = pygame.mouse.get_pos()
                    pygame.draw.line(screen, BLACK, last_pos, pos2, 5)
                    pygame.draw.circle(screen, BLACK, pos2, 20, 0)
                    pygame.display.update()
                    last_pos = None
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    draw_everything()
    main()