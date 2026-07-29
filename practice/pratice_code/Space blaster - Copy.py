import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Fullscreen setup
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
pygame.display.set_caption("Space Blaster")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Player (spaceship)
player_width = 60
player_height = 40
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 8

# Bullet
bullets = []
bullet_speed = 10

# Enemy
enemy_width = 50
enemy_height = 40
enemies = []
enemy_speed = 3
enemy_direction = 1  # 1 for right, -1 for left

# Score
score = 0
font = pygame.font.SysFont(None, 40)

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

# Game loop
running = True
while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                sys.exit()
            if event.key == pygame.K_SPACE:
                bullets.append([player_x + player_width // 2, player_y])

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Draw player
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

    # Update and draw bullets
    for bullet in bullets[:]:
        bullet[1] -= bullet_speed
        pygame.draw.circle(screen, RED, (bullet[0], bullet[1]), 5)
        if bullet[1] < 0:
            bullets.remove(bullet)

    # Spawn enemies
    if len(enemies) < 5:
        enemy_x = random.randint(0, screen_width - enemy_width)
        enemy_y = random.randint(50, 150)
        enemies.append([enemy_x, enemy_y])

    # Move enemies left/right
    for enemy in enemies:
        enemy[0] += enemy_speed * enemy_direction

    # Change direction if enemies hit the edge
    for enemy in enemies:
        if enemy[0] <= 0 or enemy[0] >= screen_width - enemy_width:
            enemy_direction *= -1
            break  # Flip direction once per frame

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (0, 255, 0), (enemy[0], enemy[1], enemy_width, enemy_height))

    # Check collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            bx, by = bullet
            ex, ey = enemy
            if ex < bx < ex + enemy_width and ey < by < ey + enemy_height:
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # Draw score
    draw_text(f"Score: {score}", 10, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
