import pygame


pygame.init()

width_screen = 800
height_screen = 600
screen = pygame.display.set_mode((width_screen, height_screen), 0)
fonte = pygame.font.SysFont("arial", 24, True, False)

# Lista de corres
amarelo = (255, 255, 0)
preto = (0, 0, 0)
azul = (0, 0, 255)

# Parametros gerais
x_per_01 = 100
y_per_01 = 240
r_per_01 = 30
velocidade = 1
vel_x_per_01 = velocidade
vel_y_per_01 = velocidade


class Cenario:
    def __init__(self, tamanho, pac):
        self.pacman = pac
        self.tamanho = tamanho
        self.pontos = 0
        self.matriz = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 0, 0, 0, 0, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2],
            [2, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 1, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2],
            [2, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        ]

    def desenha_pontos(self, tela):
        pontos_x = 30 * self.tamanho
        texto = "Pontos: {}".format(self.pontos)

        img_pontos = fonte.render(texto, True, amarelo)
        tela.blit(img_pontos, (pontos_x, 50))

    def desenha_linha(self, index_row, row, tela):
        for index_celula, celula in enumerate(row):
            x = index_celula * self.tamanho
            y = index_row * self.tamanho
            half_celula = self.tamanho // 2
            cor = preto

            if celula == 2:
                cor = azul

            pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
            if celula == 1:
                pygame.draw.circle(tela, amarelo, (x + half_celula, y + half_celula), self.tamanho//10, 0)
            elif celula == 5:
                pygame.draw.circle(tela, amarelo, (x + half_celula, y + half_celula), self.tamanho//4, 0)

    def pinta(self, tela):
        for index_row, row in enumerate(self.matriz):
            self.desenha_linha(index_row, row, tela)
        self.desenha_pontos(tela)

    def calcula_regras(self):
        pac_col = self.pacman.column_intetion
        pac_row = self.pacman.row_intention

        if (0 <= pac_col < 28) and (0 <= pac_row < 29):
            if self.matriz[pac_row][pac_col] != 2:
                pacman.aceita_movimento()
                if self.matriz[pac_row][pac_col] == 1:
                    self.pontos += 10
                    self.matriz[pac_row][pac_col] = 0
                elif self.matriz[pac_row][pac_col] == 5:
                    self.pontos += 100
                    self.matriz[pac_row][pac_col] = 0


class Pacman:
    def __init__(self, tamanho):
        self.center_x = int(width_screen / 2)
        self.center_y = int(height_screen / 2)
        self.tamanho = tamanho
        self.raio = self.tamanho // 2
        self.column = 1
        self.row = 1
        self.velocidade = 0
        self.vel_x = self.velocidade
        self.vel_y = self.velocidade
        self.column_intetion = self.column
        self.row_intention = self.row

    def calcula_regras(self):
        self.column_intetion = self.column + self.vel_x
        self.row_intention = self.row + self.vel_y
        self.center_x = int(self.column * self.tamanho + self.raio)
        self.center_y = int(self.row * self.tamanho + self.raio)

    def pintar(self, tela):
        # Desenho o corpo do PAC-MAN
        pygame.draw.circle(tela, amarelo, (self.center_x, self.center_y), self.raio)

        # Desenha a boca do PAC-MAN
        canto_boca = (self.center_x, self.center_y)
        labio_inferior = (self.center_x + self.raio, self.center_y)
        labio_superior = (self.center_x + self.raio, self.center_y - self.raio)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, preto, pontos, 0)

        # Desenha o olho do PAC-MAN
        olho_x = int(self.center_x + self.raio / 3)
        olho_y = int(self.center_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)

    def processa_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    self.vel_x = velocidade
                elif evento.key == pygame.K_LEFT:
                    self.vel_x = -velocidade
                elif evento.key == pygame.K_DOWN:
                    self.vel_y = velocidade
                elif evento.key == pygame.K_UP:
                    self.vel_y = -velocidade
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT:
                    self.vel_x = 0
                elif evento.key == pygame.K_LEFT:
                    self.vel_x = 0
                elif evento.key == pygame.K_DOWN:
                    self.vel_y = 0
                elif evento.key == pygame.K_UP:
                    self.vel_y = 0

    def processa_eventos_mouse(self, eventos):
        delay = 100
        for evento in eventos:
            if evento.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = evento.pos
                self.column = (mouse_x - self.center_x) / delay
                self.row = (mouse_y - self.center_y) / delay

    def aceita_movimento(self):
        self.column = self.column_intetion
        self.row = self.row_intention


if __name__ == "__main__":
    size = 600 // 30
    pacman = Pacman(size)
    cenario = Cenario(size, pacman)

    while True:
        # Calculos
        pacman.calcula_regras()
        cenario.calcula_regras()

        # Desenhar a tela
        screen.fill(preto)
        cenario.pinta(screen)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # Coleta de eventos
        eventos = pygame.event.get()
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()
        pacman.processa_eventos(eventos)
