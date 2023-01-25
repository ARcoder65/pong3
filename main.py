import random

import pygame, sys

pygame.init()
clock = pygame.time.Clock()

def ball_animation():
    global ball_x_speed,ball_y_speed,player_score,opponent_score,score_time
    ball.x += ball_x_speed
    ball.y += ball_y_speed

    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_y_speed *= -1

    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()

    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()

    if ball.colliderect(player) or ball.colliderect(opponent):
        pygame.mixer.Sound.play(pong_sound)
        ball_x_speed *= -1


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_code():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_start():
    global ball_y_speed, ball_x_speed,score_time

    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)

    score_font = pygame.font.Font("texgyreadventor-bolditalic.otf", 40)

    if current_time - score_time < 700:
        number_three = score_font.render('3',False,(203, 194, 192))
        screen.blit(number_three, (screen_width/2 - 10,screen_height/2 - 250))

    if 700 <  current_time - score_time < 1400:
        number_two = score_font.render('2',False,(203, 194, 192))
        screen.blit(number_two, (screen_width/2 - 10,screen_height/2 - 250))

    if 1400 <  current_time - score_time < 2100:
        number_two = score_font.render('1',False,(203, 194, 192))
        screen.blit(number_two, (screen_width/2 - 10,screen_height/2 - 250))

    if current_time - score_time < 2100:
        ball_x_speed, ball_y_speed = 0, 0
    else:
        ball_y_speed = 7 * random.choice((1, -1))
        ball_x_speed = 7 * random.choice((1, -1))
        score_time = 0





screen_width = 1280
screen_height = 700
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# game rect

ball = pygame.Rect(screen_width/2 - 13,screen_height/2 - 15,30,30)
player = pygame.Rect(screen_width - 20,screen_height/2 - 70, 10 ,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10 ,140)

bg_clr = pygame.Color('Grey12')
light_grey = (200,200,200)

ball_x_speed = 7 * random.choice((1,-1))
ball_y_speed = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7
score_time = True

player_score = 0
opponent_score = 0
game_font = pygame.font.Font("texgyreadventor-bolditalic.otf", 32)

pong_sound = pygame.mixer.Sound('pong.ogg')
score_sound = pygame.mixer.Sound('score.ogg')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_code()

    screen.fill(bg_clr)
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen,light_grey, ball)
    pygame.draw.aaline(screen,light_grey, (screen_width/2,0), (screen_width/2,screen_height))

    if score_time:
        ball_start()
    player_text = game_font.render(f"{player_score}",False,light_grey)
    screen.blit(player_text,(660,375))
    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (600, 375))

    pygame.display.flip()
    clock.tick(60)