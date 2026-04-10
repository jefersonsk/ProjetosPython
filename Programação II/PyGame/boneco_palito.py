import pygame
from pygame import KEYDOWN


class Boneco:
    def __init__(self, posx, posy, velocidade, tamanho, cor, espessura):
        self.posx = posx
        self.posy = posy
        self.velocidade = velocidade
        self.tamanho = tamanho
        self.cor = cor
        self.espessura = espessura
        self.movendo = False
        self.passos = 0

    def mover_objeto(self, teclas):
        self.movendo = False

        if teclas[pygame.K_w] and self.posy > 25:
            self.movendo = True
            self.posy -= self.velocidade
        if teclas[pygame.K_s] and self.posy < 675:
            self.movendo = True
            self.posy += self.velocidade
        if teclas[pygame.K_a] and self.posx > 30:
            self.movendo = True
            self.posx -= self.velocidade
        if teclas[pygame.K_d] and self.posx < 770:
            self.movendo = True
            self.posx += self.velocidade
        if self.movendo:
            self.passos += 1

    def desenhar_objeto(self, tela):
        # Cabeça
        pygame.draw.circle(tela, self.cor, (self.posx, self.posy), self.tamanho, self.espessura)
        # Corpo
        pygame.draw.line(tela, self.cor, (self.posx, self.posy + self.tamanho), (self.posx , self.posy + self.tamanho + 60), self.espessura)
        # Braços
        pygame.draw.line(tela, self.cor, (self.posx, self.posy + self.tamanho + 10), (self.posx + 20, self.posy + self.tamanho + 50), self.espessura)
        pygame.draw.line(tela, self.cor, (self.posx, self.posy + self.tamanho + 10), (self.posx - 20, self.posy + self.tamanho + 50), self.espessura)
        # Pernas
        if not self.movendo:
            pygame.draw.line(tela, self.cor, (self.posx, self.posy + self.tamanho + 60), (self.posx + 10, self.posy + self.tamanho + 100), self.espessura)
            pygame.draw.line(tela, self.cor, (self.posx, self.posy + self.tamanho + 60), (self.posx - 10, self.posy + self.tamanho + 100), self.espessura)
        elif (self.passos // 30) % 2 == 0:
            pygame.draw.line(tela, self.cor, (self.posx, self.posy + self.tamanho + 60), (self.posx + 20, self.posy + self.tamanho + 100), self.espessura)
            pygame.draw.line(tela, self.cor, (self.posx, self.posy + self.tamanho + 60), (self.posx - 20, self.posy + self.tamanho + 100), self.espessura)
        else:
            pygame.draw.line(tela, self.cor, (self.posx, self.posy + self.tamanho + 60), (self.posx - 10, self.posy + self.tamanho + 100), self.espessura)
            pygame.draw.line(tela, self.cor, (self.posx, self.posy + self.tamanho + 60), (self.posx + 10, self.posy + self.tamanho + 100), self.espessura)


pygame.init()

tela = pygame.display.set_mode([800, 800])
flag = True
boneco = Boneco(200, 200, 0.3, 20, "red", 3)

while flag:
    teclado = pygame.key.get_pressed()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag = False

        if evento.type == KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                flag = False

    tela.fill(("white"))

    boneco.desenhar_objeto(tela)
    boneco.mover_objeto(teclado)

    pygame.display.flip()

pygame.quit()