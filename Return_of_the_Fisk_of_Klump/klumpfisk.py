import pygame
from sys import exit
from random import randint, choice

from classes.player import Player
from classes.obstacle import Obstacle
from classes.jellyfish import Jellyfish

def display_score():
    # current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f"Score: {score}", False, "#000000")
    score_rect = score_surface.get_rect(center = (screen_width / 2, 25))
    screen.blit(score_surface,score_rect)
    return score

def collision_sprite():
     if pygame.sprite.spritecollide(player.sprite, obstacle_group, False, pygame.sprite.collide_mask): # sprite, group, bool (destroy sprite on collision - True = delete sprite on collision)
        obstacle_group.empty()
        jellyfish_group.empty()
        player.remove(player.sprite)
        pygame.time.set_timer(obstacle_timer, 1750)
        return False
     else: return True

def eat():
    global score, obstacle_timer
    if pygame.sprite.spritecollide(player.sprite, jellyfish_group, True, pygame.sprite.collide_mask):
        score += 1
    set_obstacle_time_interval()

def set_obstacle_time_interval():
    global score 
    match score:
        case 10:
            pygame.time.set_timer(obstacle_timer, 1500)
        case 15:
            pygame.time.set_timer(obstacle_timer, 1250)
        case 20:
            pygame.time.set_timer(obstacle_timer, 1000)
        case 25:
            pygame.time.set_timer(obstacle_timer, 750)
        case 10:
            pygame.time.set_timer(obstacle_timer, 500)

pygame.init()
# screen_width = 800
# screen_height = 400
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RunescapeCraft: Return of the Fisk of Klump")
clock = pygame.time.Clock()
font = pygame.font.Font("assets/font/Pixeltype.ttf", 60)
is_playing = False
score = 0

## Sprite groups
player = pygame.sprite.GroupSingle()
obstacle_group = pygame.sprite.Group()
jellyfish_group = pygame.sprite.Group()

## Environment
sea_surface = pygame.image.load('assets/graphics/sea.jpg').convert_alpha()
sea_surface = pygame.transform.scale(sea_surface, (1280, 720))
# ground_surface = pygame.image.load('assets/graphics/ground.png').convert_alpha()

## Start Menu
player_stand = pygame.image.load("assets/graphics/mola/klumpfisk.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 1) # rotozoom(surface, rotation angle, scale) - adds filtering
# player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (640, 360))

game_title = font.render("RunescapeCraft: Return of the Fisk of Klump", False, "#ffffff")
game_title_rect = game_title.get_rect(center = (640, 180))
game_intructions = font.render("Control with W,A,S,D or arrow keys", False, "#ffffff")
game_intructions_rect = game_intructions.get_rect(center = (640, 575))
game_start_message = font.render("Press SPACE to start the game", False, "#ffffff")
game_start_message_rect = game_start_message.get_rect(center = (640, 650))

## Timers
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1750)

jellyfish_timer = pygame.USEREVENT + 2
pygame.time.set_timer(jellyfish_timer, 1500)

# snail_animation_timer = pygame.USEREVENT + 2
# pygame.time.set_timer(snail_animation_timer, 500)

# fly_animation_timer = pygame.USEREVENT + 3
# pygame.time.set_timer(fly_animation_timer, 200)


while True:
    ## Listen to player input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Uninitialize pygame
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            # keys = [32, 119, 1073741906] # Space, W, Arrow up
            if not is_playing:
                if event.key == 32:
                    # RESTART GAME
                    score = 0
                    player.add(Player())
                    is_playing = True
        
        if is_playing:
            if event.type == obstacle_timer:
                # obstacle_group.add(Obstacle(choice(['fly', 'snail', 'snail'])))
                obstacle_group.add(Obstacle(choice(['shark', 'mine'])))
                
            if event.type == jellyfish_timer:
                if randint(0, 2) >= 1: jellyfish_group.add(Jellyfish())

    ### IN GAME ###
    if is_playing:
        # Environment
        # screen.blit(ground_surface, (0, 300))
        screen.blit(sea_surface, (0, 0))
        score = display_score()

        ## Jellyfish
        jellyfish_group.draw(screen)
        jellyfish_group.update()

        ## Obstacles
        obstacle_group.draw(screen)
        obstacle_group.update()

        ## Player
        player.draw(screen)
        player.update()
        eat()
        
		## Check for collisions
        is_playing = collision_sprite()

    else:
    	### START MENU ###
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)

        score_message = font.render(f"Your score: {score}", False, "#ffffff")
        score_message_rect = score_message.get_rect(center = (640, 180))
        restart_message = font.render("Press SPACE to restart the game", False, "#ffffff")
        restart_message_rect = restart_message.get_rect(center = (640, 600))

        if  pygame.time.get_ticks() < 2000: ## Bad way to check if this is first time game is started
            screen.blit(game_title, game_title_rect)
            screen.blit(game_intructions, game_intructions_rect)
            screen.blit(game_start_message, game_start_message_rect)
        else:
            screen.blit(restart_message, restart_message_rect)
            screen.blit(score_message, score_message_rect)

    ## Update display surface (screen)
    pygame.display.update()
    clock.tick(60)