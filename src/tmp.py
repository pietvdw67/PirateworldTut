import pygame
import pygame._sdl2.video # Import the SDL2 video module

pygame.init()

# Define window dimensions
screen_width, screen_height = 600, 400

# Create the main display surface. This also creates an underlying SDL window.
# The pygame._sdl2.video.Window.from_display_module() method requires
# that a display surface has already been set up.
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Borderless Alpha Splash Screen")

# Get the pygame._sdl2.video.Window object from the existing display window
# This object allows access to SDL2-specific window properties.
my_window = pygame._sdl2.video.Window.from_display_module() [1]

# Set the window to be borderless
my_window.borderless = True [1]

# Set the window's opacity (0.0 is fully transparent, 1.0 is fully opaque)
my_window.opacity = 0.7 # 70% opaque, 30% transparent [1]

# Create a surface for your splash screen content
splash_surface = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA) # SRCALPHA for per-pixel alpha [2]
splash_surface.fill((50, 50, 150, 200)) # Blue background with some transparency
font = pygame.font.Font(None, 48)
text = font.render("Loading...", True, (255, 255, 255))
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
splash_surface.blit(text, text_rect)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # Allow closing with ESC
                running = False

    # Fill the main screen with a transparent color (this is the colorkey if using Windows API,
    # but with my_window.opacity, it controls the overall window translucency)
    screen.fill((0, 0, 0, 0)) # Fill with transparent black (will be affected by my_window.opacity)

    # Blit your splash screen content onto the main screen
    screen.blit(splash_surface, (0, 0))

    pygame.display.flip()
    clock.tick(60)

# Clean up
my_window.destroy() # Explicitly destroy the window [1]
pygame.quit()