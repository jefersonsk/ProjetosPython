import pygame
from pygame import KEYDOWN
from random import randint

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
        
    def mover_horizontal(self, fator_movimento):
        self.posx += (self.velocidade * fator_movimento)

    def mover_vertical(self, fator_movimento):
        self.posy += (self.velocidade * fator_movimento)

bolinhas_criadas = []
cor = "red"

for x in range(2):
    posx = randint(20, 580)
    posy = randint(20, 580)

    bolinhas_criadas.append(Bolinha(cor, posx, posy, tamanho=20, velocidade=0.3))
    cor = "black"
    
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

    tela.fill((100, 0, 0))

    for bolinhas in bolinhas_criadas:
        bolinhas.Desenha(tela)
        bolinhas.mover_horizontal(1)
        if bolinhas.posx >= 580:
            bolinhas.velocidade = 0

    pygame.display.flip()

pygame.quit()