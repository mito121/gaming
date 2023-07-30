import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load('assets/graphics/mola/klumpfisk.png').convert_alpha()
        player_walk_1 = pygame.transform.scale(player_walk_1, (75, 80))
        # player_walk_1 = pygame.image.load('assets/graphics/player/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('assets/graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_animation_index = 0
        self.player_jump = pygame.image.load('assets/graphics/player/player_jump.png').convert_alpha()

        self.image = self.player_walk[self.player_animation_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound('assets/audio/jump.mp3')
        self.jump_sound.set_volume(0.05)
        

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()


    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def player_animation_state(self):
        if self.rect.bottom < 300: 
            # self.image = self.player_jump
            print("frol")
        else:
            # self.player_animation_index += 0.1
            if self.player_animation_index >= len(self.player_walk):self.player_animation_index = 0
            # self.image = self.player_walk[int(self.player_animation_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.player_animation_state()