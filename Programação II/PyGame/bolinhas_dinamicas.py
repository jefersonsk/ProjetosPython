import pygame
from pygame import KEYDOWN

class Bolinha:
    def __init__(self, cor, posx, posy, tamanho, velocidade):
        self.cor = cor
        self.posx = posx
        self.posy = posy
        self.tamanho = tamanho
        self.velocidade = velocidade

    def Desenha(self, tela_desenho):
        pygame.draw.circle(tela_desenho,
                           self.cor,
                           (self.posx, self.posy),
                           self.tamanho)

bolinha_teste = Bolinha("red", 200, 200, 20, 1.5)

pygame.init()
tela = pygame.display.set_mode([600, 600])
flag = True

while flag:
    teclado = pygame.key.get_pressed()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag = False

        if evento.type == KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                flag = False

    tela.fill((0, 0, 0))

    bolinha_teste.Desenha(tela)

    pygame.display.flip

pygame.quit()