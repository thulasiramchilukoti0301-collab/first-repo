import pygame
import random

# Initialize pygame
pygame.init()

# Screen
WIDTH = 300
HEIGHT = 600
BLOCK = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")

# Colors
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)

# Clock
clock = pygame.time.Clock()

# Grid
grid = [[0 for _ in range(10)] for _ in range(20)]

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],

    [[1, 1],
     [1, 1]],

    [[0, 1, 0],
     [1, 1, 1]]
]

class Piece:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.x = 3
        self.y = 0

piece = Piece()

# Draw grid
def draw_grid():
    for y in range(20):
        for x in range(10):
            rect = pygame.Rect(x*BLOCK, y*BLOCK, BLOCK, BLOCK)

            if grid[y][x]:
                pygame.draw.rect(screen, CYAN, rect)

            pygame.draw.rect(screen, (40,40,40), rect, 1)

# Draw current piece
def draw_piece(piece):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                rect = pygame.Rect(
                    (piece.x + x)*BLOCK,
                    (piece.y + y)*BLOCK,
                    BLOCK,
                    BLOCK
                )

                pygame.draw.rect(screen, CYAN, rect)

# Collision
def collision(piece):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = piece.x + x
                new_y = piece.y + y

                if new_x < 0 or new_x >= 10:
                    return True

                if new_y >= 20:
                    return True

                if new_y >= 0 and grid[new_y][new_x]:
                    return True

    return False

# Merge piece into grid
def merge(piece):
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                grid[piece.y + y][piece.x + x] = 1

# Rotate piece
def rotate(piece):
    rotated = list(zip(*piece.shape[::-1]))
    old_shape = piece.shape
    piece.shape = rotated

    if collision(piece):
        piece.shape = old_shape

# Clear completed lines
def clear_lines():
    global grid

    new_grid = []

    lines_cleared = 0

    for row in grid:

        # If row is full
        if 0 not in row:
            lines_cleared += 1

        else:
            new_grid.append(row)

    # Add empty rows at top
    while len(new_grid) < 20:
        new_grid.insert(0, [0 for _ in range(10)])

    grid = new_grid

    return lines_cleared

# Game loop
fall_time = 0
running = True

while running:

    screen.fill(BLACK)

    fall_time += clock.get_rawtime()
    clock.tick()

    # Piece falls every 500ms
    if fall_time > 500:
        piece.y += 1

        if collision(piece):
            piece.y -= 1
            merge(piece)
            # Clear completed rows
            clear_lines()
            piece = Piece()

        fall_time = 0

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                piece.x -= 1
                if collision(piece):
                    piece.x += 1

            if event.key == pygame.K_RIGHT:
                piece.x += 1
                if collision(piece):
                    piece.x -= 1

            if event.key == pygame.K_DOWN:
                piece.y += 1
                if collision(piece):
                    piece.y -= 1

            if event.key == pygame.K_UP:
                rotate(piece)

    draw_grid()
    draw_piece(piece)

    pygame.display.update()

pygame.quit()