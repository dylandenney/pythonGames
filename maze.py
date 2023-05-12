import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tile size
TILE_SIZE = 20

# Maze dimensions
MAZE_WIDTH = WIDTH // TILE_SIZE
MAZE_HEIGHT = HEIGHT // TILE_SIZE

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# Maze generation (Recursive Division)
def generate_maze(maze, x, y, width, height):
    if width <= 2 or height <= 2:
        return

    horizontal = width < height

    if horizontal:
        wall_y = random.randrange(y + 1, y + height - 1, 2)
        hole_x = random.randrange(x, x + width, 2)

        for i in range(x, x + width):
            maze[wall_y][i] = 1 if i != hole_x else 0

        generate_maze(maze, x, y, width, wall_y - y)
        generate_maze(maze, x, wall_y + 1, width, y + height - wall_y - 1)
    else:
        wall_x = random.randrange(x + 1, x + width - 1, 2)
        hole_y = random.randrange(y, y + height, 2)

        for i in range(y, y + height):
            maze[i][wall_x] = 1 if i != hole_y else 0

        generate_maze(maze, x, y, wall_x - x, height)
        generate_maze(maze, wall_x + 1, y, x + width - wall_x - 1, height)

# Create the maze
maze = [[0 for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]
generate_maze(maze, 0, 0, MAZE_WIDTH, MAZE_HEIGHT)

# Player
player_x, player_y = 0, 0

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            new_x, new_y = player_x, player_y
            if event.key == pygame.K_UP:
                new_y -= 1
            elif event.key == pygame.K_DOWN:
                new_y += 1
            elif event.key == pygame.K_LEFT:
                new_x -= 1
            elif event.key == pygame.K_RIGHT:
                new_x += 1

            if maze[new_y][new_x] == 0:
                player_x, player_y = new_x, new_y

    # Drawing
    for y in range(MAZE_HEIGHT):
        for x in range(MAZE_WIDTH):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, BLACK, (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.draw.rect(screen, (0, 255, 0), (player_x * TILE_SIZE, player_y * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    pygame.display.flip()

    # Delay
    pygame.time.delay(100)

#
# Clean up
pygame.quit()
