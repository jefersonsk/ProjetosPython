import pygame
from pygame import KEYDOWN

class Bolinha:
    def __init__(self, cor, posx, posy, tamanho = 10, velocidade = 1.0):
        self.posx = posx
        self.posy = posy
        self.cor = cor
        self.tamanho = tamanho
        self.velocidade = velocidade

    def Desenha(self, TelaDeDesenho):
        pygame.draw.circle(TelaDeDesenho,
                           self.cor,
                           (self.posx, self.posy),
                           self.tamanho)
        
    def MoverHorizontal(self, FatorMov):
        self.posx += (self.velocidade*FatorMov)

    def MoverVertical(self, FatorMov):
        self.posy += (self.velocidade*FatorMov)

    def DetectaTeclado(self, key_pressed):
        if key_pressed[pygame.K_RIGHT] == True:
            self.MoverHorizontal(1)
        if key_pressed[pygame.K_LEFT] == True:
            self.MoverHorizontal(-1)
        if key_pressed[pygame.K_DOWN]:
            self.MoverVertical(1)
        if key_pressed[pygame.K_UP] == True:
            self.MoverVertical(-1)

listaDeBolinhas = []
listaDeBolinhas.append(Bolinha((255,0,0),150, 300,30, velocidade=0.2))
listaDeBolinhas.append(Bolinha("blue",250, 100,50,velocidade=0.05))
listaDeBolinhas.append(Bolinha("orange",250, 200,10,velocidade=0.04))
listaDeBolinhas.append(Bolinha("yellow",150, 150,30,velocidade=0.03))
listaDeBolinhas.append(Bolinha("white",50, 100,20,velocidade=0.025))
listaDeBolinhas.append(Bolinha("pink",50, 100,velocidade=0.015))

pygame.init()
tela = pygame.display.set_mode([600, 600])
run = True
while run:
    #print("running")
    #bolinha1.posx += 0.01 #posx = posx + 1

    teclado = pygame.key.get_pressed()
    #print(teclado)
    for bolinha in listaDeBolinhas:
        bolinha.DetectaTeclado(teclado)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            run = False
            print(evento)

        if evento.type == KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                run = False

    # comando para pintar o fundo da tela
    tela.fill((0, 0, 0))
    for bolinha in listaDeBolinhas:
        bolinha.Desenha(tela)
        #bolinha.MoverHorizontal(1)
        #bolinha.MoverVertical(1)

    # comando para atualizar a tela
    pygame.display.flip()

pygame.quit()