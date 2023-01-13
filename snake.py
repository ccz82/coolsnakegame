# Import and initialise pygame 
import pygame
pygame.init()

# Import randint function
from random import randint

class Snake:

    def __init__(
                self,
                gameSurface,
                snakeColor = (255, 0, 0),
                snakePosX = 256,
                snakePosY = 256,
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
    while not exit:

        # Check if the user has exited the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        # Draw snake head
        snake.drawHead()

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

        # Draw snake head
        snake.drawHead()

        # FPS management
        fps.tick(10)
