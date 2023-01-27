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
                snakeVelX = 0,
                snakeVelY = 0,
                ):
        self.gameSurface = gameSurface
        self.color = color
        self.size = size
        self.snakeList = [(randrange(0, 512, self.size), randrange(0, 512, self.size))]
        self.head = self.snakeList[0]
        self.snakeVelX = snakeVelX
        self.snakeVelY = snakeVelY

    def drawSnake(self):

        # Update snake head
        self.head = self.snakeList[0]

        # Draw all parts of the snake
        for x, y in self.snakeList:
            pygame.draw.rect(self.gameSurface, self.color, pygame.Rect(
                x,
                y,
                self.size,
                self.size
                ))

        # Update display
        pygame.display.update()

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

# Render score onto display
def blitScore(snakeList, gameSurface, color, font):
    score = font.render("Your score: " + str(len(snakeList)), True, color)
    gameSurface.blit(score, [0, 0])
    pygame.display.update()

# Main program
if __name__ == "__main__":

    # Game properties
    caption = "cool snake game"
    width = 512
    height = 512
    gridSize = 32
    backgroundColor = pygame.Color(255, 255, 255)
    scoreColor = pygame.Color(200, 100, 200)
    appleColor = pygame.Color(255, 0, 0)
    snakeColor = pygame.Color(0, 255, 0)

    # Initialise sound effects
    eatingSound = pygame.mixer.Sound("eating.wav")

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

    # Draw initial snake
    snake.drawSnake()

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
                and snake.snakeVelX != snake.size):
                    snake.snakeVelX = -snake.size
                    snake.snakeVelY = 0
                if ((event.key == pygame.K_RIGHT
                or event.key == pygame.K_d)
                and snake.snakeVelX != -snake.size):
                    snake.snakeVelX = snake.size
                    snake.snakeVelY = 0
                if ((event.key == pygame.K_UP
                or event.key == pygame.K_w)
                and snake.snakeVelY != snake.size):
                    snake.snakeVelX = 0
                    snake.snakeVelY = -snake.size
                if ((event.key == pygame.K_DOWN
                or event.key == pygame.K_s)
                and snake.snakeVelY != -snake.size):
                    snake.snakeVelX = 0
                    snake.snakeVelY = snake.size

        # Update direction of snake head
        snake.head = (snake.head[0] + snake.snakeVelX, snake.head[1] + snake.snakeVelY)
        snake.snakeList.insert(0, snake.head)

        # Remove snake tail
        snake.snakeList.pop()

        # Check if the snake head has touched the edge
        if (snake.snakeList[0][0] < 0
        or snake.snakeList[0][0] > 512 - gridSize
        or snake.snakeList[0][1] < 0
        or snake.snakeList[0][1] > 512 - gridSize):
            exit = True

        # Check if the snake head has touched its body
        for body in snake.snakeList[1:]:
            if snake.head == body:
                exit = True

        # Check if apple eaten
        appleEaten = pygame.Rect.colliderect(apple, pygame.Rect(snake.snakeList[0][0], snake.snakeList[0][1], snake.size, snake.size))
        if appleEaten:

            # Play eating sound
            pygame.mixer.Sound.play(eatingSound)

            # Generate a new position for the apple to spawn
            apple = generateApplePos(snake.snakeList)

            # Grow the snake
            snake.snakeList.append(snake.head)

        # Clear board
        snake.gameSurface.fill(backgroundColor)

        # Update apple
        drawApple(surface, appleColor, apple)

        # Update snake
        snake.drawSnake()

        # Show score
        blitScore(snake.snakeList, surface, scoreColor, pygame.font.SysFont("comicsansms", 35))

        # FPS management
        fps.tick(7)