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
                ):
        self.gameSurface = gameSurface
        self.snakeColor = snakeColor
        self.snakeSize = snakeSize
        self.snakeDirection = ''
        self.snakeList = [(randrange(0, 512, self.snakeSize), randrange(0, 512, self.snakeSize))]

    def growSnake(self):
        if self.snakeDirection == 'L':
            self.snakeList.append((self.snakeList[-1][0] - self.snakeSize, self.snakeList[-1][1]))
        if self.snakeDirection == 'R':
            self.snakeList.append((self.snakeList[-1][0] + self.snakeSize, self.snakeList[-1][1] - self.snakeSize))
        if self.snakeDirection == 'U':
            self.snakeList.append((self.snakeList[-1][0], self.snakeList[-1][1] + self.snakeSize))
        if self.snakeDirection == 'D':
            self.snakeList.append((self.snakeList[-1][0], self.snakeList[-1][1] - self.snakeSize))

    def drawSnake(self):
        for x, y in self.snakeList:
            pygame.draw.rect(self.gameSurface, self.snakeColor, pygame.Rect(
                x,
                y,
                self.snakeSize,
                self.snakeSize
                ))
        pygame.display.update()
        return pygame.Rect(self.snakeList[0][0], self.snakeList[0][1], self.snakeSize, self.snakeSize)

    def updateDirection(self):
        if self.snakeDirection == 'L':
            self.snakeList[0] = (self.snakeList[0][0] - self.snakeSize, self.snakeList[0][1])
            # self.headPosX += self.snakeSize
        if self.snakeDirection == 'R':
            self.snakeList[0] = (self.snakeList[0][0] + self.snakeSize, self.snakeList[0][1])
            # self.headPosX += self.snakeSize
        if self.snakeDirection == 'U':
            self.snakeList[0] = (self.snakeList[0][0], self.snakeList[0][1] - self.snakeSize)
            # self.headPosY -= self.snakeSize
        if self.snakeDirection == 'D':
            self.snakeList[0] = (self.snakeList[0][0], self.snakeList[0][1] + self.snakeSize)
            # self.headPosY += self.snakeSize

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
    backgroundColor = pygame.Color(255, 255, 255)

    # Set window title
    pygame.display.set_caption(caption)

    # Set window size and get pygame.Surface
    surface = pygame.display.set_mode((width, height))

    # Set FPS counter
    fps = pygame.time.Clock()

    # Create a Snake object, passing in pygame.Surface
    snake = Snake(gameSurface = surface, snakeSize = gridSize)
    
    # Draw initial snake (head)
    head = snake.drawSnake()

    # Generate initial apple
    applePos = generateApplePos()
    updateApple(surface, applePos)
    appleEaten = False

    # Check if apple and snake head spawned at the same place initially
    if appleEaten:
        applePos = generateApplePos()
        updateApple(surface, applePos)

    # Game loop
    exit = False
    while not exit:

        # Check if the user has exited the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        # Check if the snake head has touched the edge
        if (snake.snakeList[0][0] < 0
        or snake.snakeList[0][0] > 512 - gridSize
        or snake.snakeList[0][1] < 0
        or snake.snakeList[0][1] > 512 - gridSize):
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
        appleEaten = pygame.Rect.colliderect(applePos, head)
        if appleEaten:

            # Generate a new position for the apple
            applePos = generateApplePos()

            # Grow the snake
            snake.growSnake()

        # Clear board
        snake.gameSurface.fill(backgroundColor)

        # Update apple
        updateApple(surface, applePos)

        # Update snake
        head = snake.drawSnake()

        # FPS management
        fps.tick(6)
