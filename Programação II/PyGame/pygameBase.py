import pygame
from pygame import KEYDOWN

class Bolinha:
    def __init__(self, cor, posx, posy, tamanho):
        self.cor = cor
        self.posx = posx
        self.posy = posy
        self.tamanho =tamanho

    def Desenha(self, tela_de_desenho):
        pygame.draw.circle(tela_de_desenho, 
                           self.cor, 
                           (self.posx, self.posy), 
                           self.tamanho)
            
        def MoverHorizontal(self, ValorMov):
            self.posx += ValorMov

lista_bolinhas = []

lista_bolinhas.append(Bolinha((255,0,0), 150, 300, 30))
lista_bolinhas.append(Bolinha("blue", 250, 100, 50))

pygame.init()
tela = pygame.display.set_mode([600, 600])
run = True
while run:
    print("running")

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            run = False
            print(evento)
            
        if evento.type == KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                run = False

    #comando para pintar o fundo da tela
    tela.fill((0, 0, 0))

    for bolinha in lista_bolinhas:
        bolinha.Desenha(tela)

    #comando para atualizar a tela
    pygame.display.flip()

pygame.quit()