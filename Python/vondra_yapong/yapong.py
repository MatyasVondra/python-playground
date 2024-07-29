import pygame
import random

BACKGROUND_COLOR = (70, 70, 70)
SPRITE_COLOR = (255, 214, 71)

WIDTH = 800
HEIGHT = 600
FPS = 60

DIFFICULTY_DICT = {
    2: 'easy',
    4: 'normal',
    6: 'hard'
}
DIFFICULTY = 4
COMPUTER_DELAY_DICT = {
    2: 40,
    4: 18,
    6: 1
}
COMPUTER_SPEED_DICT = {
    2: 9,
    4: 12,
    6: 15
}
SELECTED_MODE = "two players"


def get_random_direction():
    return random.choice([-1, 1])


# Funkce pro vykreslovani obrazovek
def draw_start_menu(difficulty, mode):
    global DIFFICULTY, SELECTED_MODE
    DIFFICULTY = difficulty
    SELECTED_MODE = mode

    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.SysFont("None", 30)
    title = font.render('YAPONG - Yet Another Pong', True, (255, 255, 255))
    underline = font.render('----------------------------------------------------', True, (255, 255, 255))
    difficulty_title = font.render('Select difficulty', True, (255, 255, 255))
    difficulty_options = font.render('1 - easy | 2 - normal | 3 - hard', True, (255, 255, 255))
    mode_title = font.render('Select mode', True, (255, 255, 255))
    mode_options = font.render('9 - two players | 0 - one player', True, (255, 255, 255))
    help_button = font.render('Press H to see help', True, (255, 255, 255))
    start_button = font.render(
        f'Press space to start with {SELECTED_MODE} and {DIFFICULTY_DICT[DIFFICULTY]} difficulty', True,
        (255, 255, 255))
    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, 150))
    screen.blit(underline, (WIDTH / 2 - underline.get_width() / 2, 168))
    screen.blit(difficulty_title, (WIDTH / 2 - difficulty_title.get_width() / 2, 200))
    screen.blit(difficulty_options, (WIDTH / 2 - difficulty_options.get_width() / 2, 225))
    screen.blit(mode_title, (WIDTH / 2 - mode_title.get_width() / 2, 275))
    screen.blit(mode_options, (WIDTH / 2 - mode_options.get_width() / 2, 300))
    screen.blit(help_button, (WIDTH / 2 - help_button.get_width() / 2, 350))
    screen.blit(start_button, (WIDTH / 2 - start_button.get_width() / 2, 400))
    pygame.display.update()


def draw_game_over_screen(winner):
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.SysFont("None", 30)
    title = font.render(f'Game Over - {winner} wins!', True, (255, 255, 255))
    start_button = font.render('Press M to return to main menu', True, (255, 255, 255))
    screen.blit(title, (WIDTH / 2 - title.get_width() / 2, 225))
    screen.blit(start_button, (WIDTH / 2 - start_button.get_width() / 2, 275))
    pygame.display.update()


def draw_help_screen():
    screen.fill(BACKGROUND_COLOR)
    font = pygame.font.SysFont("None", 30)
    first_row = font.render('Player One controls: W and S', True, (255, 255, 255))
    second_row = font.render('Player Two controls: Up and Down arrows', True, (255, 255, 255))
    third_row = font.render('First to 15 points wins', True, (255, 255, 255))
    fourth_row = font.render('Press M to return to main menu', True, (255, 255, 255))
    fifth_row = font.render('Press Escape to exit', True, (255, 255, 255))
    sixth_row = font.render('To select game mode, code has to be changed :(', True, (255, 255, 255))
    seventh_row = font.render('Made by Matyas Vondra, 2024', True, (255, 255, 255))
    screen.blit(first_row, (WIDTH / 2 - first_row.get_width() / 2, 150))
    screen.blit(second_row, (WIDTH / 2 - second_row.get_width() / 2, 175))
    screen.blit(third_row, (WIDTH / 2 - third_row.get_width() / 2, 200))
    screen.blit(fourth_row, (WIDTH / 2 - fourth_row.get_width() / 2, 225))
    screen.blit(fifth_row, (WIDTH / 2 - fifth_row.get_width() / 2, 250))
    screen.blit(sixth_row, (WIDTH / 2 - sixth_row.get_width() / 2, 275))
    screen.blit(seventh_row, (WIDTH / 2 - seventh_row.get_width() / 2, 350))
    pygame.display.update()


# Start pygame + start modulů!
pygame.init()
pygame.mixer.init()

# Nastaveni okna aj.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("YAPONG - Yet Another Pong")
# SOURCE: https://pixabay.com/sound-effects
hit_sound_effect = pygame.mixer.Sound("vondra_yapong/hit.mp3")
game_over_effect = pygame.mixer.Sound("vondra_yapong/game_over.mp3")
score_effect = pygame.mixer.Sound("vondra_yapong/score.mp3")


# Definice spritu
# Sprite hrace - ovladatelny
class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, is_player_one):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(SPRITE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_y = 0
        self.delta = 15
        self.is_player_one = is_player_one

    def update(self):
        self.speed_y = 0

        key_pressed = pygame.key.get_pressed()
        if self.is_player_one:
            if key_pressed[pygame.K_w]:
                self.speed_y -= self.delta
            if key_pressed[pygame.K_s]:
                self.speed_y += self.delta
        else:
            if key_pressed[pygame.K_UP]:
                self.speed_y -= self.delta
            if key_pressed[pygame.K_DOWN]:
                self.speed_y += self.delta

        if self.rect.bottom < 0:
            self.rect.top = HEIGHT
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

        self.rect.y += self.speed_y


# Sprite protivnika pocitace
class Computer(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, ball):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(SPRITE_COLOR)
        self.ball = ball
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_y = 0
        self.delta = COMPUTER_SPEED_DICT[DIFFICULTY]
        self.last = pygame.time.get_ticks()
        self.cooldown = COMPUTER_DELAY_DICT[DIFFICULTY]

    def update(self):
        self.speed_y = 0
        ball_y_pos = self.ball.rect.y

        # Computer will wait for 0.04 to 0.001 seconds before reacting
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            if ball_y_pos > self.rect.bottom:
                self.speed_y += self.delta
            if ball_y_pos < self.rect.top:
                self.speed_y -= self.delta

        if self.rect.bottom < 0:
            self.rect.top = HEIGHT
        if self.rect.top > HEIGHT:
            self.rect.bottom = 0

        self.rect.y += self.speed_y

    # Navraceni na stred
    def reset(self):
        self.rect.center = (self.x, self.y)

    # Update vlastnosti dle zvolene obtiznosti
    def set_difficulty(self, difficulty):
        self.delta = COMPUTER_SPEED_DICT[difficulty]
        self.cooldown = COMPUTER_DELAY_DICT[difficulty]


# Sprite mice
class Ball(pygame.sprite.Sprite):
    def __init__(self, dimension, speed, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dimension = dimension
        self.speed = speed
        self.x_direction = get_random_direction()
        self.y_direction = get_random_direction()
        self.image = pygame.Surface((dimension, dimension))
        self.image.fill(SPRITE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        # Pohyb na osach v dane rychlosti a aktualnim smerem
        self.rect.x += self.speed * self.x_direction
        self.rect.y += self.speed * self.y_direction

        # Odraz od horniho/dolniho okraje = prohozeni znaminka u y smeru
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.y_direction *= -1

        # Dotknuti se leveho/praveho okraje = zapocitani skore
        if self.rect.x <= 0:
            return 2
        elif self.rect.x >= WIDTH:
            return 1

    # Navrat na stred
    def reset(self):
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT // 2
        self.x_direction = get_random_direction()
        self.y_direction = get_random_direction()

    # Kolize s hraci = prohozeni znaminka u x smeru
    def hit(self):
        self.x_direction *= -1

    # Nastaveni rychlosti dle obtiznosti
    def set_difficulty(self, difficulty):
        self.speed = difficulty


# hodiny - FPS CLOCK / heart rate
clock = pygame.time.Clock()

# Kolekce spritů
my_sprites = pygame.sprite.Group()
players = pygame.sprite.Group()
ball = Ball(22, DIFFICULTY, WIDTH / 2, HEIGHT / 2)
player1 = Player(15, 90, 40, 300, True)

# SELECT HERE TWO PLAYERS OR ONE PLAYER
player2 = Player(15, 90, WIDTH - 55, 300, False)
# player2 = Computer(15, 90, WIDTH - 55, 300, ball)

my_sprites.add(player1)
my_sprites.add(player2)
my_sprites.add(ball)
players.add(player1)
players.add(player2)

# start:
running = True
game_state = "start_menu"
score_one = 0
score_two = 0

# cyklus udrzujici okno v chodu
while running:
    # FPS kontrola / jeslti bezi dle rychlosti!
    clock.tick(FPS)

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False

    # Hlavni menu
    if game_state == "start_menu":
        score_one = 0
        score_two = 0
        draw_start_menu(DIFFICULTY, SELECTED_MODE)
        key_state = pygame.key.get_pressed()

        # Volba obtiznosti
        if key_state[pygame.K_1]:
            draw_start_menu(2, SELECTED_MODE)
            ball.set_difficulty(DIFFICULTY)
            if isinstance(player2, Computer):
                player2.set_difficulty(2)
        elif key_state[pygame.K_2]:
            draw_start_menu(4, SELECTED_MODE)
            ball.set_difficulty(DIFFICULTY)
            if isinstance(player2, Computer):
                player2.set_difficulty(4)
        elif key_state[pygame.K_3]:
            draw_start_menu(6, SELECTED_MODE)
            ball.set_difficulty(DIFFICULTY)
            if isinstance(player2, Computer):
                player2.set_difficulty(6)
        # Volba herniho modu - nefunkcni
        elif key_state[pygame.K_9]:
            draw_start_menu(DIFFICULTY, "two players")
        elif key_state[pygame.K_0]:
            draw_start_menu(DIFFICULTY, "one player")
        # Zmeny herniho stavu
        elif key_state[pygame.K_h]:
            game_state = "help"
        elif key_state[pygame.K_SPACE]:
            game_state = "game"

    if game_state == "help":
        draw_help_screen()
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_m]:
            game_state = "start_menu"

    if game_state == "game_over":
        # Vyber viteze
        if score_one > score_two:
            draw_game_over_screen('Player One')
        else:
            draw_game_over_screen('Player Two')

        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_m]:
            game_state = "start_menu"

    if game_state == "game":
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_m]:
            game_state = "start_menu"

        # Kolize balonu s hraci = zmena smeru
        if pygame.sprite.spritecollide(ball, players, False):
            pygame.mixer.Sound.play(hit_sound_effect)
            ball.hit()

        # Update vraci hodnotu hrace, pokud skoroval
        point = ball.update()
        if point == 1:
            score_one += 1
        elif point == 2:
            score_two += 1
        if point:
            pygame.mixer.Sound.play(score_effect)
            # Reset balonu a computeru
            if isinstance(player2, Computer):
                player2.reset()
            ball.reset()

        # Kontrola win condition
        if score_one >= 15 or score_two >= 15:
            pygame.mixer.Sound.play(game_over_effect)
            game_state = "game_over"

        # Update
        my_sprites.update()
        my_font = pygame.font.SysFont("None", 30)
        player_one_text = my_font.render(f"Player One: {score_one}", True, SPRITE_COLOR)
        player_two_text = my_font.render(f"Player Two: {score_two}", True, SPRITE_COLOR)

        # Render
        screen.fill(BACKGROUND_COLOR)
        my_sprites.draw(screen)
        pygame.draw.line(screen, SPRITE_COLOR, (WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
        screen.blit(player_one_text, (WIDTH / 2 - player_one_text.get_width() - 25, 15))
        screen.blit(player_two_text, (WIDTH / 2 + player_two_text.get_width() - 107, 15))
        pygame.display.flip()

pygame.mixer.stop()
pygame.quit()
