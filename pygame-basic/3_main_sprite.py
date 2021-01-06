import pygame

pygame.init() # 초기화 (필수)

# 스크린 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("gameName") # 게임명

# 배경 이미지 불러오기
background = pygame.image.load("C:/JaeGyeong/github-repository/pygame/pygame-basic/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/JaeGyeong/github-repository/pygame/pygame-basic/character.png")
characterSize = character.get_rect().size # 이미지 크기를 구해옴. # (가로, 세로)
characterWidth = characterSize[0]
characterHeight = characterSize[1]
characterXpos = (screen_width / 2) - (characterWidth / 2)
characterYpos = screen_height - characterHeight

# 이벤트 루프
running = True # 게임 진행중인지? -> True
while running:
    for event in pygame.event.get(): # 사용자 이벤트 체크
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생했는 지
            running = False

    # screen.fill((0, 0, 255)) # r: 0, g: 0, b: 255 # 파란색
    screen.blit(background, (0, 0)) # 0, 0 좌표에 background 삽입
    screen.blit(character, (characterXpos, characterYpos))
    pygame.display.update() # 화면 다시 그리기 (필수)       

pygame.quit()
