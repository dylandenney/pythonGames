import pygame
import random

pygame.mixer.init()
#pygame.mixer.music.load('background_music.mp3')  # Replace with the path to your music file
#pygame.mixer.music.play(-1)  # -1 means loop the music indefinitely

#pygame.mixer.music.load("music.mid")
pygame.mixer.music.load("generated_music.mid")
pygame.mixer.music.play(-1)

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Objects")

# Load the character sprite
character = pygame.image.load("character.png")
character_rect = character.get_rect()
character_rect.x = WIDTH // 2
character_rect.y = HEIGHT - character_rect.height

# Object properties
object_speed = 5
object_width, object_height = 30, 30

strawberry = pygame.image.load("strawberry.png")
strawberry = pygame.transform.scale(strawberry, (object_width, object_height))


# Object list
objects = []

character_speed = 5
shift_speed_multiplier =2

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   # Character movement
    keys = pygame.key.get_pressed()

    # Determine character speed
    current_speed = character_speed
    if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
        current_speed *= shift_speed_multiplier

    if keys[pygame.K_LEFT] and character_rect.x > 0:
        character_rect.x -= current_speed
    if keys[pygame.K_RIGHT] and character_rect.x < WIDTH - character_rect.width:
        character_rect.x += current_speed

    # Object generation
    if random.randint(1, 100) <= 5:
        objects.append(pygame.Rect(random.randint(0, WIDTH - object_width), -object_height, object_width, object_height))

    # Object movement and collision detection
    new_objects = []
    for obj in objects:
        obj.y += object_speed
        if obj.colliderect(character_rect):
            print("Caught!")
        elif obj.y < HEIGHT:
            new_objects.append(obj)
    objects = new_objects

    # Drawing
    screen.fill(WHITE)
    screen.blit(character, character_rect)
    for obj in objects:
   #     pygame.draw.rect(screen, BLACK, obj)
        screen.blit(strawberry, (obj.x, obj.y))
    pygame.display.flip()

    # Delay
    pygame.time.delay(20)

# Clean up
pygame.quit()

