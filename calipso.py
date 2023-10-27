import pygame
from pygame.locals import *
from sys import exit
import webbrowser

pygame.init()
#musica
waterfall = pygame.mixer.music.load('sounds/waterfall.mp3')
waterfall = pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)


frame = pygame.time.Clock()

largura = 720
altura= 480
y = 50
x = 50

tela = pygame.display.set_mode((largura, altura))

#cores
branco = (255,255,255)
preto = (0,0,0)
vermelho = (255,0,0)
#fontes
fonte3 = pygame.font.SysFont('Monospace',20, True, False)

#funções
def video2():
     webbrowser.open("fase1.mp4")

def leitura():
    iniciar = True
    while iniciar: 
       
        textformat5= fonte3.render("Parabéns, Você chegou a ilha da pedra.",True,(preto))
        textformat6= fonte3.render('Seu objetivo é lutar com os "Amantes de Pedra"',True,(0,0,0))
        textformat7= fonte3.render("e conseguir o apoio do Rei para voltar",True,(0,0,0))
        textformat8= fonte3.render("para o ERRIJOTA, sua terra natal.",True,(0,0,0))
        textformat9= fonte3.render("(...)Boa Sorte!",True,(0,0,0))
        iniciar = fonte3.render('Pressione (espaço) para INICIAR', True,(branco))
    
        frame.tick(60)
        tela.fill((branco))
        #textos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                iniciar = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    iniciar = False
                    
        todas_sprites.draw(tela)  
        todas_sprites.update()
        #fundobranco 
       
        tela.blit(textformat5,(120,100))    
        tela.blit(textformat6,(120,120))   
        tela.blit(textformat7,(120,140))
        tela.blit(textformat8,(120,160))
        tela.blit(textformat9,(120,200))
        tela.blit(iniciar,(180,440))       
        #pygame.draw.rect(tela,(255,255,255),(x,y, 630, 350))
        pygame.display.flip()
  
#classes
class Fundo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/a/a1.jpeg'))
        self.sprites.append(pygame.image.load('sprites/a/a2.jpeg'))
        self.sprites.append(pygame.image.load('sprites/a/a3.jpeg'))
        self.sprites.append(pygame.image.load('sprites/a/a4.jpeg'))
        self.sprites.append(pygame.image.load('sprites/a/a5.jpeg'))
        self.sprites.append(pygame.image.load('sprites/a/a6.jpeg'))
        self.sprites.append(pygame.image.load('sprites/a/a7.jpeg'))
        self.sprites.append(pygame.image.load('sprites/a/a8.jpeg'))
        self.sprites.append(pygame.image.load('sprites/a/a9.jpeg'))
        self.sprites.append(pygame.image.load('sprites/a/a10.jpeg'))
        
        self.atual = 0

        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (largura,altura))


        self.rect = self.image.get_rect()
        self.rect.topleft = -70, 0
    def update(self):
        self.atual = self.atual + 0.1
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (largura+140,altura))
        
#sprites
todas_sprites = pygame.sprite.Group()
fundo = Fundo()
todas_sprites.add(fundo)
#Jogo
#leitura()
