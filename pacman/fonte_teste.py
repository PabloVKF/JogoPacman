import pygame


pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

pontos = 100
texto = "Hello word and pygame!\nPontos: {}".format(pontos)

fonte = pygame.font.SysFont("arial", 48, True, False)
img_texto = fonte.render(texto, True, (255, 255, 0))

while True:
    screen.blit(img_texto, (100, 100))
    pygame.display.update()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit()
