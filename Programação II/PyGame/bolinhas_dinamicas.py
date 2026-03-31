import pygame
from pygame import KEYDOWN
from random import randint, choice

class Bolinha:
    def __init__(self, cor, posx, posy, tamanho, velocidade_posx, velocidade_posy, comportamento):
        self.cor = cor
        self.posx = posx
        self.posy = posy
        self.tamanho = tamanho
        self.velocidade_posx = velocidade_posx
        self.velocidade_posy = velocidade_posy
        self.comportamento = comportamento

    def Desenha(self, tela_desenho):
        pygame.draw.circle(tela_desenho,
                           self.cor,
                           (self.posx, self.posy),
                           self.tamanho)
        
    def mover_horizontal(self, fator_movimento):
        self.posx += (self.velocidade_posx * fator_movimento)

    def mover_vertical(self, fator_movimento):
        self.posy += (self.velocidade_posy * fator_movimento)

def calcular_distancia() -> float:
    """ Calcula a distância entre o centro dos objetos.

    Returns:
        float: Retorna a distâcia total entre os objetos.
    """
    distancia_x = bolinhas_criadas[0].posx - bolinhas_criadas[1].posx
    distancia_y = bolinhas_criadas[0].posy - bolinhas_criadas[1].posy
    return ((distancia_x ** 2) + (distancia_y ** 2)) ** 0.5

def quicar_objetos(lista: list) -> None:
    """
    Calcula o momento que as bolinhas batem entre elas.

    Args:
        lista (list): Lista com os objetos.
    """
    # 1. Dá marcha ré na direção atual
    lista[0].velocidade_posx = 1
    lista[0].velocidade_posy = 1
    lista[1].velocidade_posx = -1
    lista[1].velocidade_posy = -1
    
    # 2. Move as bolinhas até se separarem
    while calcular_distancia() <= 40:
        lista[0].mover_horizontal(1)
        lista[0].mover_vertical(1)
        lista[1].mover_horizontal(1)
        lista[1].mover_vertical(1)
        
    # 3. Sorteia a nova direção
    lista[0].velocidade_posx = choice([-0.3, 0.3])
    lista[0].velocidade_posy = choice([-0.3, 0.3])
    lista[1].velocidade_posx = choice([-0.3, 0.3])
    lista[1].velocidade_posy = choice([-0.3, 0.3])

def sortear_posicao() -> int:
    return randint(20, 580)

bolinhas_criadas = []

bolinhas_criadas.append(Bolinha("red", posx=sortear_posicao(), posy=sortear_posicao(), tamanho=20, velocidade_posx=choice([-0.3, 0.3]), velocidade_posy=choice([-0.3, 0.3]), comportamento="quica"))
bolinhas_criadas.append(Bolinha("black", posx=sortear_posicao, posy=sortear_posicao(), tamanho=20, velocidade_posx=choice([-0.3, 0.3]), velocidade_posy=choice([-0.3, 0.3]), comportamento="atravessa"))
    
pygame.init()
tela = pygame.display.set_mode([600, 600])
flag = True

while flag:
    teclado = pygame.key.get_pressed()

    distancia_total = calcular_distancia()

    # Causa a colisão das bolinhas caso a distância total entre elas fique abaixo de 40.
    if distancia_total <= 40:
        quicar_objetos(bolinhas_criadas)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag = False

        if evento.type == KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                flag = False

    tela.fill(("white"))

    for bolinhas in bolinhas_criadas:
        bolinhas.Desenha(tela)
        bolinhas.mover_horizontal(1)
        bolinhas.mover_vertical(1)

        if bolinhas.comportamento == "quica":
            if bolinhas.posx >= 580:
                bolinhas.velocidade_posx = -0.3

            if bolinhas.posx <= 20:
                bolinhas.velocidade_posx = 0.3

            if bolinhas.posy >= 580:
                bolinhas.velocidade_posy = -0.3

            if bolinhas.posy <= 20:
                bolinhas.velocidade_posy = 0.3

        if bolinhas.comportamento == "atravessa":
            if bolinhas.posx >= 600:
                bolinhas.posx = 0
            elif bolinhas.posx <= 0:
                bolinhas.posx = 600

            if bolinhas.posy >= 600:
                bolinhas.posy = 0
            elif bolinhas.posy <= 0:
                bolinhas.posy = 600

    pygame.display.flip()

pygame.quit()