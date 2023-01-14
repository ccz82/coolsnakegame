# Import and initialise pygame 
import pygame
pygame.init()

# Import randint function
from random import randrange

class Snake:

    def __init__(
                self,
                gameSurface,
                snakeColor = (0, 255, 0),
                snakePosX = randrange(0, 512, 16),
                snakePosY = randrange(0, 512, 16),
                snakeSizeX = 16,
                snakeSizeY = 16,
                snakeDirection = ''
                ):
        self.gameSurface = gameSurface
        self.snakeColor = snakeColor
        self.snakePosX = snakePosX
        self.snakePosY = snakePosY
        self.snakeSizeX = snakeSizeX
        self.snakeSizeY = snakeSizeY
        self.snakeDirection = snakeDirection

    def drawHead(self):
        rect = pygame.Rect(
            self.snakePosX,
            self.snakePosY,
            self.snakeSizeX,
            self.snakeSizeY
            )
        pygame.draw.rect(self.gameSurface, self.snakeColor, rect)
        pygame.display.update()

    def updateDirection(self):
        if self.snakeDirection == 'L':
            self.snakePosX -= 16
        if self.snakeDirection == 'R':
            self.snakePosX += 16
        if self.snakeDirection == 'U':
            self.snakePosY -= 16
        if self.snakeDirection == 'D':
            self.snakePosY += 16

# Generate an apple randomly
def generateApple(gameSurface):
    apple = pygame.Rect(
        randrange(0, 512),
        randrange(0, 512),
        16,
        16
        )
    pygame.draw.rect(gameSurface, (255, 0, 0), apple)
    pygame.display.update()

# Generate border around window
def generateBorder(gameSurface):
    leftRect = pygame.Rect(
        0,
        0,
        16,
        512
        )
    rightRect = pygame.Rect(
        496,
        0,
        16,
        512
        )
    topRect = pygame.Rect(
        0,
        0,
        512,
        16
        )
    botRect = pygame.Rect(
        0,
        496,
        512,
        16
        )
    rectangles = [leftRect, rightRect, topRect, botRect]
    for i in range(4):
        pygame.draw.rect(gameSurface, (0, 0, 0), rectangles[i])
    pygame.display.update() 

# Main program
if __name__ == "__main__":

    # Variable assignment
    caption = "cool snake game"
    width = 512
    height = 512
    white = pygame.Color(255, 255, 255)

    # Set window title
    pygame.display.set_caption(caption)

    # Set window size and get pygame.Surface
    surface = pygame.display.set_mode((width, height))

    # Set FPS counter
    fps = pygame.time.Clock()

    # Create a Snake object, passing in pygame.Surface
    snake = Snake(gameSurface = surface)

    # Game loop
    exit = False

    # Draw snake head
    snake.drawHead()

    while not exit:

        # Check if the user has exited the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        # Get direction
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            snake.snakeDirection = 'L'
        elif key[pygame.K_RIGHT] or key[pygame.K_d]:
            snake.snakeDirection = 'R'
        elif key[pygame.K_UP] or key[pygame.K_w]:
            snake.snakeDirection = 'U'
        elif key[pygame.K_DOWN] or key[pygame.K_s]:
            snake.snakeDirection = 'D'

        # Update direction
        snake.updateDirection()

        # Clear board
        snake.gameSurface.fill(white)

        # Create border
        generateBorder(surface)

        # Draw snake head
        snake.drawHead()

        # FPS management
        fps.tick(10)