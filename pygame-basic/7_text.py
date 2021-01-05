import pygame

pygame.init() # 초기화 (필수)

# 스크린 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("gameName") # 게임명

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/JaeGyeong/github-repository/pygame/pygame-basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/JaeGyeong/github-repository/pygame/pygame-basic/character.png")
characterSize = character.get_rect().size # 이미지 크기를 구해옴. #get rectangle
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXpos = (screen_width / 2) - (characterWidth / 2)
characterYpos = screen_height - characterHeight

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 enemy
enemy = pygame.image.load("C:/JaeGyeong/github-repository/pygame/pygame-basic/enemy.png")
enemySize = enemy.get_rect().size # 이미지 크기를 구해옴. #get rectangle
enemyWidth = enemySize[0]
enemyHeight = enemySize[1]
enemyXpos = (screen_width / 2) - (enemyWidth / 2)
enemyYpos = (screen_height / 2) - (enemyHeight / 2)

# 폰트 정보 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트패밀리, 크기)

# 총 시간
total_time = 10 # 10s

# 시작 시간
start_ticks = pygame.time.get_ticks() # 시작 tick 정보 받아옴

# 이벤트 루프
running = True # 게임 진행중인지? -> True
while running:
    dt = clock.tick(60) # 화면 초당 프레임 수 설정
    
    for event in pygame.event.get(): # 사용자 이벤트 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생했는 지
            running = False
        
        if event.type == pygame.KEYDOWN: # 키 눌림 이벤트
            if event.key == pygame.K_LEFT : 
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 키 뗌
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    characterXpos += to_x * dt
    characterYpos += to_y * dt

    # 가로 경계 값 처리
    if characterXpos < 0:
        characterXpos = 0
    elif characterXpos > screen_width - characterWidth:
        characterXpos = screen_width - characterWidth
    # 세로 경계 값 처리
    if characterYpos < 0:
        characterYpos = 0
    elif characterYpos > screen_height - characterHeight:
        characterYpos = screen_height - characterHeight

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect() # character의 좌표, width, height 정보 포함 중
    character_rect.left = characterXpos
    character_rect.top = characterYpos

    enemy_rect = enemy.get_rect() # 이미지를 불러온 것.
    enemy_rect.left = enemyXpos # 좌표값 반영
    enemy_rect.top = enemyYpos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect): # rect 기준으로 충돌 여부 확인
        print("enemy와 충돌함")
        running = False
    

    # screen.fill((0, 0, 255)) # r: 0, g: 0, b: 255 # 파란색
    screen.blit(background, (0, 0)) # 0, 0 좌표에 background 삽입
    screen.blit(character, (characterXpos, characterYpos)) # 캐릭터 그리기
    screen.blit(enemy, (enemyXpos, enemyYpos)) # 적 그리기

    # 타이머 넣기, 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms를 s단위로 환산

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        print("Time out")
        running = False

    pygame.display.update() # 화면 다시 그리기 (필수)       

pygame.time.delay(2000) # 2s 대기 
pygame.quit()
