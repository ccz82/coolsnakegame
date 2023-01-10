# Import and initialise pygame 
import pygame
pygame.init()

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
                snakeSizeY = 16
                ):
        self.gameSurface = gameSurface
        self.gameColor = gameColor
        self.snakeColor = snakeColor
        self.snakePosX = snakePosX
        self.snakePosY = snakePosY
        self.snakeSizeX = snakeSizeX
        self.snakeSizeY = snakeSizeY
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

            # Movement of head
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT] or key[pygame.K_a]:
                self.snakePosX -= 16
            elif key[pygame.K_RIGHT] or key[pygame.K_d]:
                self.snakePosX += 16
            elif key[pygame.K_UP] or key[pygame.K_w]:
                self.snakePosY -= 16
            elif key[pygame.K_DOWN] or key[pygame.K_s]:
                self.snakePosY += 16

            # Clear board and update head
            self.gameSurface.fill(self.gameColor)
            self.drawHead()

            pygame.time.wait(100)       

if __name__ == "__main__":
    surface = initWindow()
    gameInstance(surface)
