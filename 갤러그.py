import pygame
import sys

# 게임 설정
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SPEED = 5
BULLET_SPEED = 5
ENEMY_SPEED = 2

# 색상 설정
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 플레이어 클래스
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT-30))

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -PLAYER_SPEED)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, PLAYER_SPEED)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)

        # 플레이어가 화면 밖으로 나가지 않도록 함
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# 적 클래스
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((50, 10))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT-30))

    def update(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# 게임 초기화
pygame.init()

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 플레이어 생성
player = Player()

# 적 그룹 생성
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 플레이어 업데이트
    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # 적 생성
    if pygame.time.get_ticks() % 30 == 0:
        new_enemy = Enemy()
        enemies.add(new_enemy)
        all_sprites.add(new_enemy)

    # 적 업데이트
    enemies.update()

    # 화면 그리기
    screen.fill((0, 0, 0))
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # 충돌 체크
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()