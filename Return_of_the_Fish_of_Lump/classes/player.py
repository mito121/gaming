import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('assets/graphics/mola/klumpfisk.png').convert_alpha()
        # player_walk_1 = pygame.transform.scale(player_walk_1, (115, 125))
        player_walk_1 = pygame.transform.rotozoom(player_walk_1, 0, .5) # rotozoom(surface, rotation angle, scale)
        # player_walk_1 = pygame.image.load('assets/graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('assets/graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_animation_index = 0
        self.player_jump = pygame.image.load('assets/graphics/player/player_jump.png').convert_alpha()

        self.image = self.player_walk[self.player_animation_index]
        self.rect = self.image.get_rect(midbottom = (120,400))
        self.mask = pygame.mask.from_surface(self.image)
        self.size = 1
        self.swim_speed = 2.75
        self.orientation = "right"

        # self.jump_sound = pygame.mixer.Sound('assets/audio/jump.mp3')
        # self.jump_sound.set_volume(0.05)
        

    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.rect.top > 35:
            self.rect.y -= self.swim_speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.rect.bottom < 720:
            self.rect.y += self.swim_speed
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect.right < 1280:
            self.rect.right += self.swim_speed
            if self.orientation == "left":
                self.orientation = "right"
                self.image = pygame.transform.flip(self.image, True, False)
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.left > 0:
            self.rect.left -= self.swim_speed
            if self.orientation == "right":
                self.orientation = "left"
                self.image = pygame.transform.flip(self.image, True, False)

    # def player_animation_state(self):
        # if self.rect.bottom < 300: 
            # self.image = self.player_jump
        # else:
            # self.player_animation_index += 0.1
            # if self.player_animation_index >= len(self.player_walk):self.player_animation_index = 0
            # self.image = self.player_walk[int(self.player_animation_index)]

    def update(self):
        self.player_input()
        # self.player_animation_state()