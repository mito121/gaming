import pygame

class Poop(pygame.sprite.Sprite):
     def __init__(self, rect):
        super().__init__()
        poop_frame_1 = pygame.image.load("assets/graphics/poop/sausage.png").convert_alpha()
        self.image = poop_frame_1
        self.image = pygame.transform.rotozoom(self.image, -60, .025)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = rect

     def destroy(self):
          if self.rect.y >= 600:  #ehh whats this?
               self.kill()

     def update(self):
          self.rect.y += 12
          self.destroy()