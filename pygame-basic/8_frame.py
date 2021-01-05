import pygame

pygame.init() # 초기화 (필수)

# 스크린 크기 설정 (필수)
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정 (필수)
pygame.display.set_caption("gameName") # 게임명

# FPS (필수)
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트)


running = True 
while running:
    dt = clock.tick(30)
    
    # 2. 이벤트 처리 (키보드, 마우스)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

    # 3. 캐릭터 위치 정의

    # 4. 충돌 처리
    
    # 5. 화면에 그리기

   
    pygame.display.update() # 화면 다시 그리기 (필수)       

pygame.time.delay(2000) # 2s 대기 
pygame.quit()
