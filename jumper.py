import pygame
from sys import exit

pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("RunescapeCraft: World of Fortnite Legends")
pygame.display.set_caption("RunescapeCraft: Return of the Fisk of Klump")
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)

is_playing = True

## Sky settings
sky_surface = pygame.image.load('graphics/sky.png').convert_alpha()

## Ground settings
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
ground_x_position = 0
ground_speed = -50

## Score settings
score = 0
score_surface = font.render(f"Score: {score}", False, "Deeppink")
score_rect = score_surface.get_rect(center = (screen_width / 2, 25))

## Snail settings
snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_speed = 4
snail_left_max = -100
snail_x_max = screen_width + 50
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

## Player
player_surface = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

## Gravity
jump_height = -15
player_gravity = jump_height
floor = 300
force_of_gravity = 0.5

while True:
    ## Listen to player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Uninitialize pygame
            pygame.quit()
            exit()
        
        # if event.type == pygame.MOUSEMOTION: print(event.pos)
        # if event.type == pygame.MOUSEBUTTONDOWN: print("mouse down")
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if player_rect.collidepoint(event.pos):
        #           print("player rect clicked")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and player_rect.bottom >= floor:
                player_gravity = jump_height
        if event.type == pygame.KEYDOWN:
            keys = [32, 119, 1073741906] # Space, W, Arrow up

            if is_playing:
                if player_rect.bottom >= floor:
                    if event.key in keys:
                        player_gravity = jump_height
            else:
                is_playing = True
                snail_rect.x = 800

    ### IN GAME ###
    if is_playing:
        ## Environment
        ## Ground
        screen.blit(ground_surface, (0, 300))
        ground_x_position -= ground_speed

        ## Sky
        screen.blit(sky_surface, (0, 0))

        ## Score text
        pygame.draw.rect(screen, "blue", score_rect)
        pygame.draw.rect(screen, "blue", score_rect, 10)
        # pygame.draw.line(screen,"red",(0,0),pygame.mouse.get_pos(),10)
        screen.blit(score_surface, score_rect)

        ## Snail
        screen.blit(snail_surface, snail_rect)
        # Movement
        snail_rect.x -= snail_speed
        if snail_rect.x <= snail_left_max: snail_rect.x = snail_x_max
        
        ## Gravity
        player_gravity += force_of_gravity
        player_rect.y += player_gravity
        if player_rect.bottom >= floor: player_rect.bottom = floor

        ## Player
        screen.blit(player_surface, player_rect)

        ## Collision
        if player_rect.colliderect(snail_rect):
            if snail_rect.colliderect(player_rect):
                is_playing = False

        ## Mouse
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     print(pygame.mouse.get_pressed())
    else:
        ### MENU ###
        screen.fill("yellow")

    ## Update display surface (screen)
    pygame.display.update()
    clock.tick(60)