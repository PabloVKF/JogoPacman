import pygame


pygame.init()

amarelo = (255, 255, 0)
preto = (0, 0, 0)

x_per_01 = 100
y_per_01 = 240
r_per_01 = 30
velocidade = 0.5
vel_x_per_01 = velocidade
vel_y_per_01 = velocidade

width_tela = 640
height_tela = 480
tela = pygame.display.set_mode((width_tela, height_tela), 0)

while True:
    # Calculos
    x_per_01 = x_per_01 + vel_x_per_01
    y_per_01 = y_per_01 + vel_y_per_01
    if ((x_per_01 + r_per_01) >= width_tela) or ((x_per_01 - r_per_01) <= 0):
        vel_x_per_01 *= (-1)
    if ((y_per_01 + r_per_01) >= height_tela) or ((y_per_01 - r_per_01) <= 0):
        vel_y_per_01 *= (-1)

    # Interface
    tela.fill(preto)
    pygame.draw.circle(tela, amarelo, (int(x_per_01), y_per_01), r_per_01, 0)
    pygame.display.update()

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit()
