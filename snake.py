# Import and initialise pygame 
import pygame
pygame.init()

# Import random.randrange() function
from random import randrange

class Snake:

    def __init__(
                self,
                gameSurface,
                size,
                color,
                ):
        self.gameSurface = gameSurface
        self.color = color
        self.size = size
        self.snakeDirection = ''
        self.snakeList = [(randrange(0, 512, self.size), randrange(0, 512, self.size))]

    def growSnake(self):
        if self.snakeDirection == 'L':
            self.snakeList.append((self.snakeList[-1][0] - self.size, self.snakeList[-1][1]))
        if self.snakeDirection == 'R':
            self.snakeList.append((self.snakeList[-1][0] + self.size, self.snakeList[-1][1] - self.size))
        if self.snakeDirection == 'U':
            self.snakeList.append((self.snakeList[-1][0], self.snakeList[-1][1] + self.size))
        if self.snakeDirection == 'D':
            self.snakeList.append((self.snakeList[-1][0], self.snakeList[-1][1] - self.size))

    def drawSnake(self):
        for x, y in self.snakeList:
            pygame.draw.rect(self.gameSurface, self.color, pygame.Rect(
                x,
                y,
                self.size,
                self.size
                ))
        pygame.display.update()
        return pygame.Rect(self.snakeList[0][0], self.snakeList[0][1], self.size, self.size)

    def updateDirection(self):
        if self.snakeDirection == 'L':
            self.snakeList[0] = (self.snakeList[0][0] - self.size, self.snakeList[0][1])
        if self.snakeDirection == 'R':
            self.snakeList[0] = (self.snakeList[0][0] + self.size, self.snakeList[0][1])
        if self.snakeDirection == 'U':
            self.snakeList[0] = (self.snakeList[0][0], self.snakeList[0][1] - self.size)
        if self.snakeDirection == 'D':
            self.snakeList[0] = (self.snakeList[0][0], self.snakeList[0][1] + self.size)

# Generate an apple position
def generateApplePos(occupiedRects):

    # Randomly generate a position in an unoccupied space for the apple to spawn
    applePos = (randrange(0, 512, gridSize), randrange(0, 512, gridSize))
    while applePos in occupiedRects:
        applePos = (randrange(0, 512, gridSize), randrange(0, 512, gridSize))

    return pygame.Rect(
        applePos[0],
        applePos[1],
        gridSize,
        gridSize
        )

# Draw/update apple position
def drawApple(gameSurface, color, rect):
    pygame.draw.rect(gameSurface, color, rect)
    pygame.display.update()

# Main program
if __name__ == "__main__":

    # Game properties
    caption = "cool snake game"
    width = 512
    height = 512
    gridSize = 32
    backgroundColor = pygame.Color(255, 255, 255)
    appleColor = pygame.Color(255, 0, 0)
    snakeColor = pygame.Color(0, 255, 0)

    # Set window title
    pygame.display.set_caption(caption)

    # Set window size and get pygame.Surface
    surface = pygame.display.set_mode((width, height))

    # Set FPS counter
    fps = pygame.time.Clock()

    # Create a Snake object, passing in pygame.Surface
    snake = Snake(
            gameSurface = surface,
            size = gridSize,
            color = snakeColor
            )

    # Draw initial snake (head)
    head = snake.drawSnake()

    # Generate initial apple
    apple = generateApplePos(snake.snakeList)
    drawApple(surface, appleColor, apple)
    appleEaten = False

    # Game loop
    exit = False
    while not exit:

        # pygame event queue
        for event in pygame.event.get():

            # Check if user has exited the game
            if event.type == pygame.QUIT:
                exit = True

            # Check if user has changed direction of snake
            if event.type == pygame.KEYDOWN:
                if ((event.key == pygame.K_LEFT
                or event.key == pygame.K_a)
                and snake.snakeDirection != 'L'):
                    snake.snakeDirection = 'L'
                if ((event.key == pygame.K_RIGHT
                or event.key == pygame.K_d)
                and snake.snakeDirection != 'R'):
                    snake.snakeDirection = 'R'
                if ((event.key == pygame.K_UP
                or event.key == pygame.K_w)
                and snake.snakeDirection != 'U'):
                    snake.snakeDirection = 'U'
                if ((event.key == pygame.K_DOWN
                or event.key == pygame.K_s)
                and snake.snakeDirection != 'D'):
                    snake.snakeDirection = 'D'

        # Update direction
        snake.updateDirection()

        # Check if the snake head has touched the edge
        if (snake.snakeList[0][0] < 0
        or snake.snakeList[0][0] > 512 - gridSize
        or snake.snakeList[0][1] < 0
        or snake.snakeList[0][1] > 512 - gridSize):
            exit = True

        # Check if apple eaten
        appleEaten = pygame.Rect.colliderect(apple, head)
        if appleEaten:

            # Generate a new position for the apple to spawn
            apple= generateApplePos(snake.snakeList)

            # Grow the snake
            snake.growSnake()

        # Clear board
        snake.gameSurface.fill(backgroundColor)

        # Update apple
        drawApple(surface, appleColor, apple)

        # Update snake
        head = snake.drawSnake()

        # FPS management
        fps.tick(7)
