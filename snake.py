# Import and initialise pygame 
import pygame
pygame.init()

# Import randint function
from random import randrange

class Snake:

    def __init__(
                self,
                gameSurface,
                snakeSize,
                snakeColor = (0, 255, 0),
                headPosX = randrange(0, 512, 32),
                headPosY = randrange(0, 512, 32)
                ):
        self.gameSurface = gameSurface
        self.snakeColor = snakeColor
        self.headPosX = snakePosX
        self.headPosY = snakePosY
        self.snakeSize = snakeSize
        self.snakeDirection = ''
        self.snakeList = []

    def updateSnake(self):
        if len(self.snakeList) == 0:
            self.snakeList.append((self.headPosX, self.headPosY))
        else:
            pass
        
    def drawSnake(self):
        head = pygame.Rect(
            self.headPosX,
            self.headPosY,
            self.snakeSize,
            self.snakeSize
            )
        pygame.draw.rect(self.gameSurface, self.snakeColor, head)
       
        pygame.display.update()
        return head
                
    def updateDirection(self):
        if self.snakeDirection == 'L':
            self.headPosX -= self.snakeSize
        if self.snakeDirection == 'R':
            self.headPosX += self.snakeSize
        if self.snakeDirection == 'U':
            self.headPosY -= self.snakeSize
        if self.snakeDirection == 'D':
            self.headPosY += self.snakeSize

# Generate an apple position
def generateApplePos():
    applePos = pygame.Rect(
        randrange(0, 512, gridSize),
        randrange(0, 512, gridSize),
        gridSize,
        gridSize
        )
    return applePos

# Update apple position
def updateApple(gameSurface, applePos):
    pygame.draw.rect(gameSurface, (255, 0, 0), applePos)
    pygame.display.update()

# Main program
if __name__ == "__main__":

    # Game properties
    caption = "cool snake game"
    width = 512
    height = 512
    gridSize = 32
    white = pygame.Color(255, 255, 255)

    # Set window title
    pygame.display.set_caption(caption)

    # Set window size and get pygame.Surface
    surface = pygame.display.set_mode((width, height))

    # Set FPS counter
    fps = pygame.time.Clock()

    # Create a Snake object, passing in pygame.Surface
    snake = Snake(gameSurface = surface, snakeSize = gridSize)
    
    # Draw initial snake head
    snakeHead = snake.drawSnake()

    # Generate initial apple
    applePos = generateApplePos()
    updateApple(surface, applePos)
    appleEaten = False

    # Check if apple and snake head spawned at the same place initially
    if appleEaten:
        applePos = generateApplePos()
        updateApple(surface,applePos)

    # Game loop
    exit = False
    while not exit:

        # Check if the user has exited the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        # Check if the snake head has touched the edge
        if snake.snakePosX < 0 or snake.snakePosX > 512 - gridSize or snake.snakePosY < 0 or snake.snakePosY > 512 - gridSize:
            exit = True

        # Get direction
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] or key[pygame.K_a]:
            snake.snakeDirection = 'L'
        if key[pygame.K_RIGHT] or key[pygame.K_d]:
            snake.snakeDirection = 'R'
        if key[pygame.K_UP] or key[pygame.K_w]:
            snake.snakeDirection = 'U'
        if key[pygame.K_DOWN] or key[pygame.K_s]:
            snake.snakeDirection = 'D'

        # Update direction
        snake.updateDirection()

        # Check if apple eaten
        appleEaten = pygame.Rect.colliderect(applePos, snakeHead)
        if appleEaten:

            # Generate a new position for the apple
            applePos = generateApplePos()

            # Grow the snake
            snake.updateSnake()
        
        # Clear board
        snake.gameSurface.fill(white)

        # Update apple
        updateApple(surface, applePos)

        # Update snake head
        snakeHead = snake.drawSnake()

        # FPS management
        fps.tick(10)