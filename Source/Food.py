from Specification import *


class Food:
    ################################################## CORE FUNCTIONS ##################################################
    def __init__(self, app, pos):
        self.app = app
        self.grid_pos = [pos[0], pos[1]]
        self.pixel_pos = self.get_current_pixel_pos()
        self.color = GREEN
        self.radius = int(CELL_SIZE // 5)
        self.image = pygame.image.load(FOOD)
        self.image = pygame.transform.scale(self.image, (20, 20))

    def appear(self):
        """
        Make the Food appear on the screen.
        """
        self.draw()

    ####################################################################################################################


    def get_current_pixel_pos(self):
        """
        Get the current pixel position via the current grid position.

        :return: the pixel position [x, y]
        """
        return [self.grid_pos[0] * CELL_SIZE + CELL_SIZE // 2 + MAP_POS_X,
                self.grid_pos[1] * CELL_SIZE + CELL_SIZE // 2 + MAP_POS_Y]


    def draw(self):
        """
        Draw the Food onto the screen.
        """
        food_rect = self.app.screen.blit(self.image, (self.pixel_pos[0]-10, self.pixel_pos[1]-10))
        pygame.display.update(food_rect)
