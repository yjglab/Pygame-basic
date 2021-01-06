import pygame
import random

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("game2")

clock = pygame.time.Clock()

background = pygame.image.load("C:/JaeGyeong/github-repository/pygame/pygame-basic/background.png")

character = pygame.image.load("C:/JaeGyeong/github-repository/pygame/pygame-basic/character.png")
characterSize = character.get_rect().size
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXpos = (screen_width / 2) - (characterWidth / 2)
characterYpos = screen_height - characterHeight

to_x = 0
to_y = 0

character_speed = 0.6

enemy = pygame.image.load("C:/JaeGyeong/github-repository/pygame/pygame-basic/enemy.png")
enemySize = enemy.get_rect().size
enemyWidth = enemySize[0]
enemyHeight = enemySize[1]
enemyXpos = random.randint(0, screen_width - enemyWidth)
enemyYpos = 0



running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    enemyYpos += 6
    if enemyYpos > screen_height:
        enemyXpos = random.randint(0, screen_width - enemyWidth)
        enemyYpos = 0
        
    characterXpos += to_x * dt
    characterYpos += to_y * dt

    if  characterXpos < 0:
        characterXpos = 0
    elif characterXpos > screen_width - characterWidth: 
        characterXpos = screen_width - characterWidth
    elif characterYpos < 0:
        characterYpos = 0
    elif characterYpos > screen_height - characterHeight:
        characterYpos = screen_height - characterHeight
    
    character_rect = character.get_rect()
    character_rect.left = characterXpos
    character_rect.top = characterYpos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemyXpos
    enemy_rect.top = enemyYpos
    
    if character_rect.colliderect(enemy_rect):
        running = False

    screen.blit(background, (0, 0))
    screen.blit(character, (characterXpos, characterYpos))
    screen.blit(enemy, (enemyXpos, enemyYpos))

    

    pygame.display.update()

pygame.time.delay(500)
pygame.quit()