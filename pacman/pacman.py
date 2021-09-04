import random

import pygame
from abc import ABCMeta, abstractmethod

pygame.init()

width_screen = 800
height_screen = 600
screen = pygame.display.set_mode((width_screen, height_screen), 0)
font = pygame.font.SysFont("arial", 24, True, False)

# Lista de corres
amarelo = (255, 255, 0)
preto = (0, 0, 0)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
branco = (255, 255, 255)
ciano = (0, 255, 255)
laranja = (255, 140, 0)
rosa = (255, 15, 192)

# Parametros gerais
x_per_01 = 100
y_per_01 = 240
r_per_01 = 30
velocidade = 1
vel_x_per_01 = velocidade
vel_y_per_01 = velocidade
acima = 1
abaixo = 2
direita = 3
esquerda = 4


class ElementoJogo(metaclass=ABCMeta):
    @abstractmethod
    def calcular_regras(self):
        pass

    @abstractmethod
    def pintar(self, tela):
        pass

    @abstractmethod
    def processar_eventos(self, eventos):
        pass


class Movivel(metaclass=ABCMeta):
    @abstractmethod
    def aceitar_movimento(self):
        pass

    @abstractmethod
    def recusar_movimento(self, direcoes):
        pass

    @abstractmethod
    def esquina(self, direcoes):
        pass


class Cenario(ElementoJogo):
    def __init__(self, tamanho, pacman):
        self.pacman = pacman
        self.moviveis = []
        self.tamanho = tamanho
        self.vidas = 5
        self.pontos = 0
        # Estados possíveis: 0- Jogando | 1- Pausado | 2- GameOver | 3- Winner
        self.estado = 0
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

    def adicionar_movivel(self, obj):
        self.moviveis.append(obj)

    def pintar_score(self, tela):
        pontos_x = 30 * self.tamanho
        texto_pontos = "Pontos: {}".format(self.pontos)
        pontos_img = font.render(texto_pontos, True, amarelo)
        tela.blit(pontos_img, (pontos_x, 50))

        vidas_x = 30 * self.tamanho
        texto_vidas = "Vidas: {}".format(self.vidas)
        vidas_img = font.render(texto_vidas, True, amarelo)
        tela.blit(vidas_img, (vidas_x, 100))

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
                pygame.draw.circle(tela, amarelo, (x + half_celula, y + half_celula), self.tamanho // 10, 0)
            elif celula == 5:
                pygame.draw.circle(tela, amarelo, (x + half_celula, y + half_celula), self.tamanho // 4, 0)

    def pintar(self, tela):
        if self.estado == 0:
            self.pintar_jogando(tela)
        elif self.estado == 1:
            self.pintar_jogando(tela)
            self.pintar_pausado(tela)
        elif self.estado == 2:
            self.pintar_jogando(tela)
            self.pintar_gameover(tela)
        elif self.estado == 3:
            self.pintar_jogando(tela)
            self.pintar_winner(tela)

    @staticmethod
    def pintar_centro(tela, texto):
        texto_img = font.render(texto, True, amarelo)
        texto_x = (tela.get_width() - texto_img.get_width()) // 2
        texto_y = (tela.get_height() - texto_img.get_height()) // 2

        tela.blit(texto_img, (texto_x, texto_y))

    def pintar_winner(self, tela):
        self.pintar_centro(tela, 'W I N N E R ! ! !')

    def pintar_gameover(self, tela):
        self.pintar_centro(tela, 'G A M E   O V E R')

    def pintar_pausado(self, tela):
        self.pintar_centro(tela, 'P A U S A D O')

    def pintar_jogando(self, tela):
        for index_row, row in enumerate(self.matriz):
            self.desenha_linha(index_row, row, tela)
        self.pintar_score(tela)

    def get_direcoes(self, row, column):
        direcoes = []
        if self.matriz[int(row - 1)][int(column)] != 2:
            direcoes.append(acima)
        if self.matriz[int(row + 1)][int(column)] != 2:
            direcoes.append(abaixo)
        if self.matriz[int(row)][int(column + 1)] != 2:
            direcoes.append(direita)
        if self.matriz[int(row)][int(column - 1)] != 2:
            direcoes.append(esquerda)
        return direcoes

    def calcular_regras(self):
        if self.estado == 0:
            self.calcular_regras_jogando()
        elif self.estado == 1:
            self.calcular_regras_pausado()
        elif self.estado == 2:
            self.calcular_regras_gameover()
        elif self.estado == 3:
            self.calcular_regras_winner()

    def calcular_regras_winner(self):
        pass

    def calcular_regras_gameover(self):
        pass

    def calcular_regras_pausado(self):
        pass

    def calcular_regras_jogando(self):
        for movivel in self.moviveis:
            row = int(movivel.row)
            column = int(movivel.column)
            row_intention = int(movivel.row_intention)
            column_intention = int(movivel.column_intention)
            direcoes = self.get_direcoes(row, column)

            if len(direcoes) >= 3:
                movivel.esquina(direcoes)
            if isinstance(movivel, Fantasma) and (movivel.row == self.pacman.row) and \
                    (movivel.column == self.pacman.column):
                self.vidas -= 1
                if self.vidas <= 0:
                    self.estado = 2
                else:
                    self.pacman.row = 1
                    self.pacman.column = 1
            else:
                if (0 <= column_intention <= 28) and (0 <= row_intention <= 29) and (
                        self.matriz[row_intention][column_intention] != 2):
                    movivel.aceitar_movimento()
                    if isinstance(movivel, Pacman):
                        if self.matriz[row][column] == 1:
                            self.pontos += 10
                        elif self.matriz[row][column] == 5:
                            self.pontos += 100
                        self.matriz[row][column] = 0
                        if self.pontos >= 3420:
                            self.estado = 3
                else:
                    movivel.recusar_movimento(direcoes)

    def processar_eventos(self, eventos):
        for evento in eventos:
            if evento.type == pygame.QUIT:
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    if self.estado == 0:
                        self.estado = 1
                    elif self.estado == 1:
                        self.estado = 0


class Pacman(ElementoJogo, Movivel):
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
        self.column_intention = self.column
        self.row_intention = self.row
        self.abertura = 0
        self.vel_abertura = 4

    def calcular_regras(self):
        self.column_intention = self.column + self.vel_x
        self.row_intention = self.row + self.vel_y
        self.center_x = int(self.column * self.tamanho + self.raio)
        self.center_y = int(self.row * self.tamanho + self.raio)

    def pintar(self, tela):
        # Desenho o corpo do PAC-MAN
        pygame.draw.circle(tela, amarelo, (self.center_x, self.center_y), self.raio)

        # Desenha a boca do PAC-MAN
        self.abertura += self.vel_abertura
        if (self.abertura >= self.raio) or (self.abertura <= 0):
            self.vel_abertura *= (-1)

        canto_boca = (self.center_x, self.center_y)
        labio_inferior = (self.center_x + self.raio, self.center_y + self.abertura)
        labio_superior = (self.center_x + self.raio, self.center_y - self.abertura)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, preto, pontos, 0)

        # Desenha o olho do PAC-MAN
        olho_x = int(self.center_x + self.raio / 3)
        olho_y = int(self.center_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, preto, (olho_x, olho_y), olho_raio, 0)

    def processar_eventos(self, eventos):
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

    def aceitar_movimento(self):
        self.column = self.column_intention
        self.row = self.row_intention

    def recusar_movimento(self, direcoes):
        self.row_intention = self.row
        self.column_intention = self.column

    def esquina(self, direcoes):
        pass


class Fantasma(ElementoJogo):
    def __init__(self, cor, tamanho):
        self.row = 15.0
        self.column = 13.0
        self.row_intention = self.row
        self.column_intention = self.column
        self.velocidade = 1
        self.direcao = abaixo
        self.cor = cor
        self.tamanho = tamanho

    def calcular_regras(self):
        if self.direcao == acima:
            self.row_intention -= 1
        elif self.direcao == abaixo:
            self.row_intention += 1
        elif self.direcao == direita:
            self.column_intention += 1
        elif self.direcao == esquerda:
            self.column_intention -= 1

    def mudar_derecao(self, direcoes):
        self.direcao = random.choice(direcoes)

    def esquina(self, direcoes):
        self.mudar_derecao(direcoes)

    def aceitar_movimento(self):
        self.row = self.row_intention
        self.column = self.column_intention

    def recusar_movimento(self, direcoes):
        self.row_intention = self.row
        self.column_intention = self.column
        self.mudar_derecao(direcoes)

    def pintar(self, tela):
        fatia = self.tamanho // 8
        px = int(self.column * self.tamanho)
        py = int(self.row * self.tamanho)
        contorno = [(px, py + self.tamanho),
                    (px + fatia, py + (2 * fatia)),
                    (px + (2 * fatia), py + (fatia // 2)),
                    (px + (3 * fatia), py),
                    (px + (5 * fatia), py),
                    (px + (6 * fatia), py + (fatia // 2)),
                    (px + (7 * fatia), py + (2 * fatia)),
                    (px + self.tamanho, py + self.tamanho)]
        pygame.draw.polygon(tela, self.cor, contorno, 0)

        olho_raio_externo = fatia
        olho_raio_interno = fatia // 2
        px_olho_esquerdo = int(px + (2.5 * fatia))
        px_olho_direito = int(px + (5.5 * fatia))
        py_olho = int(py + (2.5 * fatia))

        pygame.draw.circle(tela, branco, (px_olho_esquerdo, py_olho), olho_raio_externo, 0)
        pygame.draw.circle(tela, preto, (px_olho_esquerdo, py_olho), olho_raio_interno, 0)
        pygame.draw.circle(tela, branco, (px_olho_direito, py_olho), olho_raio_externo, 0)
        pygame.draw.circle(tela, preto, (px_olho_direito, py_olho), olho_raio_interno, 0)

    def processar_eventos(self, eventos):
        pass


if __name__ == "__main__":
    size = 600 // 30
    pac_man = Pacman(size)
    blinky = Fantasma(vermelho, size)
    inky = Fantasma(ciano, size)
    clyde = Fantasma(laranja, size)
    pinky = Fantasma(rosa, size)
    cenario = Cenario(size, pac_man)
    cenario.adicionar_movivel(pac_man)
    cenario.adicionar_movivel(blinky)
    cenario.adicionar_movivel(inky)
    cenario.adicionar_movivel(clyde)
    cenario.adicionar_movivel(pinky)

    while True:
        # Calculos
        pac_man.calcular_regras()
        blinky.calcular_regras()
        inky.calcular_regras()
        clyde.calcular_regras()
        pinky.calcular_regras()
        cenario.calcular_regras()

        # Desenhar a tela
        screen.fill(preto)
        cenario.pintar(screen)
        pac_man.pintar(screen)
        blinky.pintar(screen)
        inky.pintar(screen)
        clyde.pintar(screen)
        pinky.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)

        # Coleta de eventos
        eventos_ocorridos = pygame.event.get()
        cenario.processar_eventos(eventos_ocorridos)
        pac_man.processar_eventos(eventos_ocorridos)
