# Import and initialise pygame 
import pygame
pygame.init()

# Import randint function
from random import randint

# Draw a new window and return Surface object
def initWindow(caption = "cool snake game", width = 512, height = 512):
    # Set window title
    pygame.display.set_caption(caption)
    # Set window size and return Surface object
    return pygame.display.set_mode((width, height))

class gameInstance:

    def __init__(
                self,
                gameSurface,
                gameColor = (255, 255, 255),
                snakeColor = (255, 0, 0),
                snakePosX = 256,
                snakePosY = 256,
                snakeSizeX = 16,
                snakeSizeY = 16,
                snakeDirection = ''
                ):
        self.gameSurface = gameSurface
        self.gameColor = gameColor
        self.snakeColor = snakeColor
        self.snakePosX = snakePosX
        self.snakePosY = snakePosY
        self.snakeSizeX = snakeSizeX
        self.snakeSizeY = snakeSizeY
        self.snakeDirection = snakeDirection
        self.gameLoop()

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

    def gameLoop(self):

        # Game loop
        exit = False
        while not exit:

            # Check if the user has exited the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True

            # Draw snake head
            self.drawHead()

            # Get direction
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.snakeDirection = 'L'
            elif key[pygame.K_RIGHT] or key[pygame.K_d]:
                self.snakeDirection = 'R'
            elif key[pygame.K_UP] or key[pygame.K_w]:
                self.snakeDirection = 'U'
            elif key[pygame.K_DOWN] or key[pygame.K_s]:
                self.snakeDirection = 'D'

            # Update direction
            self.updateDirection()

            # Clear board
            self.gameSurface.fill(self.gameColor)

            # Draw snake head
            self.drawHead()

            # Time delay in ms, lower delay = higher snake speed
            pygame.time.wait(120)

if __name__ == "__main__":
    surface = initWindow()
    gameInstance(surface)

# Update local git repository
"""
git pull
"""

# Commit changes to local git repository and push to GitHub
"""
git add --all
git commit -m "message"
git push
"""

