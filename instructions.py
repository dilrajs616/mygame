import pygame
import pygame.font

class Instructions:

    def __init__(self, ai_game, msg) :

        # Get screen info.
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 1050, 50
        self.button_color = (255, 0, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and position it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x, self.rect.y = (300, 700)

        # The button msg needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        # Turn the msg into a rendered image and center text on the button.
        self.msg_image = self.font.render(msg, True, self.text_color, 
                    self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)