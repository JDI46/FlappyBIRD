import pygame
pygame.init()


#class for background for flappy bird
class Background:
    #this will have the image size as private attributes and return the image to the screen
    def __init__(self, game_background):
        self.game_background = game_background

        return game_background

    #this containst the background image
    def get_image(self, background_image):
        self.background_image = background_image

        background_image = pygame.image.load('flappy_background.png')
        width, height = pygame.image.get_size()


    #this gets the size from the intialization; I don't need a private attribute here; use pygame to validate module for getting image size
    def set_image_size(self, new_size):
        self.new_size = new_size
        new_size = pygame.transform.scale(image, (400, 788))