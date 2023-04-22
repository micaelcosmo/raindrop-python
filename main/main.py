import pygame
import os
import random

# Definir as dimensões da janela
WIDTH, HEIGHT = 600, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raindrop Catcher")

# Carregar imagens
UMBRELLA_IMAGE = pygame.image.load(os.path.join('../images', 'bucket.png'))
RAIN_IMAGE = pygame.image.load(os.path.join('../images', 'droplet.png'))

# Carregar sons
pygame.mixer.init()
RAIN_SOUND = pygame.mixer.Sound(os.path.join('../images', 'rain.mp3'))
RAIN_SOUND.set_volume(0.1)


class Raindrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = RAIN_IMAGE

    def update(self):
        self.y += 5

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class Umbrella:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = UMBRELLA_IMAGE

    def move_left(self):
        if self.x > 0:
            self.x -= 5

    def move_right(self):
        if self.x < WIDTH - self.image.get_width():
            self.x += 5

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


def clear():
    WIN.fill((255, 255, 255))


def draw_objects(raindrops, umbrella, score):
    umbrella.draw(WIN)
    for raindrop in raindrops:
        raindrop.draw(WIN)
    score_text = pygame.font.SysFont('comicsans', 30).render(f"Score: {score}", 1, (0, 0, 0))
    WIN.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
    pygame.display.update()


def main():
    raindrops = []
    umbrella = Umbrella(WIDTH // 2, HEIGHT - 100)
    score = 0
    clock = pygame.time.Clock()

    # Reproduzir música de fundo
    RAIN_SOUND.play(-1)

    # Loop principal do jogo
    while True:
        clock.tick(30)

        # Lidar com eventos do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    umbrella.move_left()
                elif event.key == pygame.K_RIGHT:
                    umbrella.move_right()

        # Adicionar novas gotas de chuva aleatoriamente
        if random.randint(0, 100) < 10:
            raindrops.append(Raindrop(random.randint(0, WIDTH - RAIN_IMAGE.get_width()), 0))

        # Atualizar a posição das gotas de chuva e remover as que saíram da tela
        for raindrop in raindrops:
            raindrop.update()
            if raindrop.y > HEIGHT:
                raindrops.remove(raindrop)

        # Verificar se o guarda-chuva pegou alguma gota de chuva e atualizar a pont
        for raindrop in raindrops:
            if raindrop.y + raindrop.image.get_height() > umbrella.y:
                if raindrop.x > umbrella.x and raindrop.x < umbrella.x + umbrella.image.get_width():
                    score += 1
                    raindrops.remove(raindrop)

        # Limpar a tela e desenhar os objetos
        clear()
        draw_objects(raindrops, umbrella, score)
