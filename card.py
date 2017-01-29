import pygame


class Card(object):
    def __init__(self, num):
        self.num = num
        self.pic = pygame.image.load("pics/"+str(num)+".png")

    def __str__(self):
        return 'Card:'+str(self.num)

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise
        if self.num == other.num:
            return True
        return False

    def draw(self, screen, pos):
        screen.blit(self.pic, pos)
