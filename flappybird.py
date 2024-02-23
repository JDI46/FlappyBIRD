import pygame
import sys
pygame.init()


#class for background for flappy bird
class Background:
    #this will have the image size as private attributes and return the image to the screen/ this gets the image. Don't need getter and setter for image in pygame
    def __init__(self, game_background):
        self.image = None
        try:
            self.image = pygame.image.load('flappy_background.png')
        except Exception as e:
            print('Error loading image:', str(e))



    #this contains the background image
    def get_image(self):
        return self.image

