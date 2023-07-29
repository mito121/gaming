import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f"Score: {current_time}", False, "#000000")
    score_rect = score_surface.get_rect(center = (screen_width / 2, 25))
    screen.blit(score_surface,score_rect)
    return current_time

def obstacle_movement(list):
    if list:
        for rect in list:
            rect.x -= 5

            if rect.bottom == 300: # draw snail
                screen.blit(snail_surface, rect)
            elif rect.bottom == 210: # draw fly
                screen.blit(fly_surface, rect)
        
        list = [obstacle for obstacle in list if obstacle.x > -100] # remove obstacles from list that are off screen
        return list
    else: return []

def collision(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surface, player_index

    if player_rect.bottom < 300:
        # jump
        player_surface = player_jump
    else:
        # walk
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]



pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("RunescapeCraft: World of Fortnite Legends")
pygame.display.set_caption("RunescapeCraft: Return of the Fisk of Klump")
clock = pygame.time.Clock()
font = pygame.font.Font("font/Pixeltype.ttf", 50)
is_playing = False
start_time = 0
score = 0

## Sky settings
sky_surface = pygame.image.load('graphics/sky.png').convert_alpha()

## Ground settings
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
ground_x_position = 0
ground_speed = -50

## Obstacle settings
snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
# snail_surface = pygame.image.load("graphics/snail/snail1.png").convert_alpha()

fly_frame_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
# fly_surface = pygame.image.load("graphics/fly/fly1.png").convert_alpha()


obstacle_rect_list = []

## Player
player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
player_jump = pygame.image.load("graphics/player/player_jump.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0

player_surface = player_walk[player_index]
player_rect = player_surface.get_rect(midbottom = (80,300))

## Start Menu
player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
# player_stand = pygame.transform.rotozoom(player_stand, 0, 2) # rotozoom(surface, rotation angle, scale)
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400, 200))

game_title = font.render("RunescapeCraft: Return of the Fisk of Klump", False, "#ffffff")
game_title_rect = game_title.get_rect(center = (400, 80))
game_start_message = font.render("Press SPACE to start the game", False, "#ffffff")
game_start_message_rect = game_start_message.get_rect(center = (400, 350))

## Gravity
jump_height = -15
player_gravity = jump_height
floor = 300
force_of_gravity = 0.5

## Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)


while True:
    ## Listen to player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Uninitialize pygame
            pygame.quit()
            exit()
        
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
                if event.key == 32:
                    # RESTART GAME
                    is_playing = True
                    start_time = int(pygame.time.get_ticks() / 1000)
        
        if is_playing:
            if event.type == obstacle_timer:
                if randint(0, 2):
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom = (randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900, 1100), 210)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surface = fly_frames[fly_frame_index]

    ### IN GAME ###
    if is_playing:
        ## Environment
        ## Ground
        screen.blit(ground_surface, (0, 300))
        ground_x_position -= ground_speed

        ## Sky
        screen.blit(sky_surface, (0, 0))
        
        ## Score
        score = display_score()

        ## Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)
        
        ## Gravity
        player_gravity += force_of_gravity
        player_rect.bottom += player_gravity
        player_animation()
        if player_rect.bottom >= floor: player_rect.bottom = floor

        ## Player
        screen.blit(player_surface, player_rect)

        ## Collision
        is_playing = collision(player_rect, obstacle_rect_list)

    else:
    ### START MENU ###
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        
        obstacle_rect_list.clear() # empty list of obstacles
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_message = font.render(f"Your score: {score}", False, "#ffffff")
        score_message_rect = score_message.get_rect(center = (400, 80))
        restart_message = font.render("Press SPACE to restart the game", False, "#ffffff")
        restart_message_rect = restart_message.get_rect(center = (400, 335))

        if score == 0:
            screen.blit(game_title, game_title_rect)
            screen.blit(game_start_message, game_start_message_rect)
        else:
            screen.blit(restart_message, restart_message_rect)
            screen.blit(score_message, score_message_rect)

    ## Update display surface (screen)
    pygame.display.update()
    clock.tick(60)