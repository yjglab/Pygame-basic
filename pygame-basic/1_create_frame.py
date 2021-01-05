import pygame

pygame.init() # 초기화 (필수)

# 스크린 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("gameName") # 게임명

# 이벤트 루프
running = True # 게임 진행중인지? -> True
while running:
    for event in pygame.event.get(): # 사용자 이벤트 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생했는 지
            running = False
            

pygame.quit()
