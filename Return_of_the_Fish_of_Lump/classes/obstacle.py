import pygame
from random import randint

class Obstacle(pygame.sprite.Sprite):
     def __init__(self, type):
        super().__init__()
        if type == "mine":
            mine_frame_1 = pygame.image.load("assets/graphics/mine/mine.png").convert_alpha()
          #   mine_frame_2 = pygame.image.load("assets/graphics/mine/mine2.png").convert_alpha()
          #   self.frames = [mine_frame_1, mine_frame_2]
            # y_pos = randint(100, 210) # 210
            self.image = mine_frame_1
            self.image = pygame.transform.scale(self.image, (75, 75))

        if type == "shark":
            shark_frame_1 = pygame.image.load("assets/graphics/shark/shark.png").convert_alpha()
          #   shark_frame_2 = pygame.image.load("assets/graphics/shark/shark2.png").convert_alpha()
          #   self.frames = [shark_frame_1, shark_frame_2]
            # y_pos = 300
            self.image = shark_frame_1
            self.image = pygame.transform.scale(self.image, (250, 85))

     #    self.animation_index = 0
     #    self.image = self.frames[self.animation_index]
        y_pos = randint(0, 400)
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100),y_pos))

     # def player_animation_state(self):
     #      self.animation_index += 0.1
     #      if self.animation_index >= len(self.frames): self.animation_index = 0
     #      self.image = self.frames[int(self.animation_index)]

     def destroy(self):
          if self.rect.x <= -250:
               self.kill()

     def update(self):
          # self.player_animation_state()
          self.rect.x -= 6
          self.destroy()