import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = [5, 5]
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Create the paddle and ball
paddle = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 20, 120, 10)
ball = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)

# Initialize score variables
player_score = 0
opponent_score = 0

font = pygame.font.Font(None, 36)

def display_score():
    player_text = font.render(f"Player: {player_score}", True, WHITE)
    opponent_text = font.render(f"Opponent: {opponent_score}", True, WHITE)
    screen.blit(player_text, (10, 10))
    screen.blit(opponent_text, (WIDTH - 200, 10))

# Initialize clock
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(5, 0)

    ball.move_ip(BALL_SPEED)

    if ball.left < 0 or ball.right > WIDTH:
        BALL_SPEED[0] = -BALL_SPEED[0]
    if ball.top < 0:
        BALL_SPEED[1] = -BALL_SPEED[1]

    if ball.colliderect(paddle) and BALL_SPEED[1] > 0:
        BALL_SPEED[1] = -BALL_SPEED[1]

    if ball.bottom > HEIGHT:
        opponent_score += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        BALL_SPEED[1] = 5

    display_score()

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    if player_score >= 5:
        print("Player Wins!")
        pygame.quit()
        sys.exit()
    elif opponent_score >= 5:
        print("Opponent Wins!")
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)
