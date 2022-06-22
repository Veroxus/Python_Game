import pygame
import os

WIDTH, HEIGHT = 900,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BORDER = pygame.Rect(WIDTH/2 - 5, 0, 10, HEIGHT)

FPS = 144
VELOCITY = 2
BULLET_VELOCITY = 3

YELLOW_SPACESHIP_IMAGE = pygame.image.load('Assets/spaceship_yellow.png')
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (50,50)), 270)

RED_SPACESHIP_IMAGE = pygame.image.load('Assets/spaceship_red.png')
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (50, 50)), 90)

def draw_window(red, yellow, red_bullets, yellow_bullets):
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, (255, 0, 0), bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, (255, 255, 0), bullet)

    pygame.display.update()

def move_red_ship(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x - VELOCITY > 0: # Left
        red.x -= VELOCITY
    if keys_pressed[pygame.K_d] and red.x + VELOCITY + red.width < BORDER.x : # Right
        red.x += VELOCITY
    if keys_pressed[pygame.K_w] and red.y - VELOCITY > 0: # Up
        red.y -= VELOCITY
    if keys_pressed[pygame.K_s] and red.y + VELOCITY + red.height < 500: # Down
        red.y += VELOCITY

def move_yellow_ship(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VELOCITY > BORDER.x + 10: # Left
        yellow.x -= VELOCITY
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VELOCITY + yellow.width < 900 : # Right
        yellow.x += VELOCITY
    if keys_pressed[pygame.K_UP] and yellow.y - VELOCITY > 0: # Up
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and yellow.y + VELOCITY + yellow.height < 500: # Down
        yellow.y += VELOCITY

def fire_bullets(bullets_red, bullets_yellow, red, yellow):
    for bullet in bullets_red:
        bullet.x += BULLET_VELOCITY

    for bullet in bullets_yellow:
        bullet.x -= BULLET_VELOCITY

def main():
    red = pygame.Rect(100, 300, 50, 50)
    yellow = pygame.Rect(700, 300, 50, 50)

    bullets_red = []
    bullets_yellow = []

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(red.x, red.y+red.height//2, 10, 5)
                    bullets_red.append(bullet) 
                if event.key == pygame.K_RCTRL:
                    bullet = pygame.Rect(yellow.x, yellow.y, 10, 5)
                    bullets_yellow.append(bullet)
    
        keys_pressed = pygame.key.get_pressed()
        move_red_ship(keys_pressed, red)
        move_yellow_ship(keys_pressed, yellow)

        fire_bullets(bullets_red, bullets_yellow, red, yellow)

        draw_window(red, yellow, bullets_red, bullets_yellow)

    pygame.quit()
    

if __name__ == "__main__":
    main()