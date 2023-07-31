import pygame
from random import randint

class Jellyfish(pygame.sprite.Sprite):
     def __init__(self):
        super().__init__()

        jellyfish_frame_1 = pygame.image.load("assets/graphics/jellyfish/jellyfish.png").convert_alpha()
        self.image = jellyfish_frame_1
        self.image = pygame.transform.scale(self.image, (75, 75))

        y_pos = randint(0, 400)
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100),y_pos))

     def destroy(self):
          if self.rect.x <= -250:
               self.kill()

     def update(self):
          self.rect.x -= 6
          self.destroy()