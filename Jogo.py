from main import *
import pygame
from pygame.locals import *
from sys import exit
import webbrowser
from fase1_2 import *
from fase3 import *


pygame.init()
#tela_dimensoes
largura = 720
altura= 480
y = 50
x = 50
'''
xs = -80
ys = -40
xl = -80
yl = -40
'''
#cores
branco = (255,255,255)
preto = (0,0,0)

#fontes
fonte4 = pygame.font.SysFont('Bold',80, True, False)
fonte3 = pygame.font.SysFont('Monospace',15, True, False)
fonte2 = pygame.font.SysFont('Bold',30, True, False)
fonte1 = pygame.font.SysFont('Monospace',80, True, False)
fonte = pygame.font.SysFont('Monospace',60, True, True)

#musica
'''''
on_of = True
musica_fundo = pygame.mixer.music.load('sounds/trilhadojogo.mp3')
if on_of == True:
   musica_fundo = pygame.mixer.music.play(-1)
'''
musica_fundo = pygame.mixer.music.set_volume(0.5)
sounds = pygame.mixer.Sound('sounds/clique.mp3')




#tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('As Aventuras de Cleiton( O Bom de Guerra)')
frame =pygame.time.Clock()
#imagens







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
        
class Fundo1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites/b/b1.png'))
        self.sprites.append(pygame.image.load('sprites/b/b2.png'))
        self.sprites.append(pygame.image.load('sprites/b/b3.png'))
        self.sprites.append(pygame.image.load('sprites/b/b4.png'))
        self.sprites.append(pygame.image.load('sprites/b/b5.png'))
        self.sprites.append(pygame.image.load('sprites/b/b6.png'))
        self.sprites.append(pygame.image.load('sprites/b/b7.png'))
        self.sprites.append(pygame.image.load('sprites/b/b8.png'))
        self.sprites.append(pygame.image.load('sprites/b/b9.png'))
        self.sprites.append(pygame.image.load('sprites/b/b10.png'))
        self.sprites.append(pygame.image.load('sprites/b/b11.png'))
        self.sprites.append(pygame.image.load('sprites/b/b12.png'))
        self.sprites.append(pygame.image.load('sprites/b/b13.png'))
        self.sprites.append(pygame.image.load('sprites/b/b14.png'))
        self.sprites.append(pygame.image.load('sprites/b/b15.png'))
        self.sprites.append(pygame.image.load('sprites/b/b16.png'))
        self.sprites.append(pygame.image.load('sprites/b/b17.png'))
        self.sprites.append(pygame.image.load('sprites/b/b18.png'))
        self.sprites.append(pygame.image.load('sprites/b/b19.png'))
        self.sprites.append(pygame.image.load('sprites/b/b20.png'))
        self.sprites.append(pygame.image.load('sprites/b/b21.png'))
        self.sprites.append(pygame.image.load('sprites/b/b22.png'))
        self.sprites.append(pygame.image.load('sprites/b/b23.png'))
        self.sprites.append(pygame.image.load('sprites/b/b24.png'))
        self.sprites.append(pygame.image.load('sprites/b/b25.png'))
        self.sprites.append(pygame.image.load('sprites/b/b26.png'))
        self.sprites.append(pygame.image.load('sprites/b/b27.png'))
        self.sprites.append(pygame.image.load('sprites/b/b28.png'))
        self.sprites.append(pygame.image.load('sprites/b/b29.png'))
        self.sprites.append(pygame.image.load('sprites/b/b30.png'))
        self.sprites.append(pygame.image.load('sprites/b/b31.png'))

        
        self.atual = 0

        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (largura,altura))


        self.rect = self.image.get_rect()
        self.rect.topleft = -70, 0
    def update(self):
        self.atual = self.atual + 0.30
        if self.atual >= len(self.sprites):
            self.atual = 0
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image, (largura+140,altura))
#sprites
todas_sprites = pygame.sprite.Group()
fundo = Fundo1()

todas_sprites.add(fundo)
#funções
def video_player():
        
        '''
        som = pygame.mixer.music.load('sounds/fase1.mp3')
      
        Tela = tkinter.Tk()
        Tela.title('Guerra de Troia')
        Tela.geometry('720x480+300+100')
        Tela.resizable(0,0)
        Tela.config(background='gray')

        video = tkVideoPlayer.TkinterVideo(Tela,scaled=True)
        video.load('videos/fase1.mp4')
        video.grid(row=1,column=0, columnspan= 3, sticky='we', ipady=170)
        print(dir(video))
        input()
        ligado = True
        def play():
            video.play()
            if ligado == True:
                som = pygame.mixer.music.play()
        def pular():
            print('sim')
            if ligado == True:
                pygame.mixer.music.stop()
                video.pause()
        play = tkinter.Button(Tela, text='play',relief='flat', width=99, borderwidth=1 , command=play).grid(row=10, column=0, padx=10, pady=10)
        pular = tkinter.Button(Tela, text='pular(1)',relief='flat', width=99, borderwidth=1 , command=pular).grid(row=0, column=0, padx=10, pady=10)
       
        Tela.mainloop()
        '''
        webbrowser.open("fase1.mp4")
''''
def tela_pause():
    pause = True
    while pause:
        tela.fill(branco)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pause = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    pause = False
                    sounds.play()
                    fasedois()
        tela.blit(telapause,(0,0))
        pygame.display.update()
'''
def iniciar_fase2():
    iniciar2 = True
    while iniciar2:
        tela.fill((branco))
        #textos
        text_fase2 = fonte4.render("Aperte Qualquer Tecla",True,(preto))
        tela.blit(text_fase2,(50,175))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                iniciar2 = False
            if evento.type == pygame.KEYDOWN:
                iniciar2 = False
                sounds.play()
                fasedois()
        pygame.display.update()
def perdeu():
    perdeu = True
    #webbrowser.open("morte.mp4")
    while perdeu:
        tela.fill((branco))
        #textos
        texto_perdeu = fonte4.render("Você Perdeu",True,(preto))
        texto_perdeu1 = fonte3.render("Aperte qualquer tecla",True,(preto))
        tela.blit(texto_perdeu1,(250,300))
        tela.blit(texto_perdeu,(180,150))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                perdeu = False
            if evento.type == pygame.KEYDOWN:
                perdeu = False
                sounds.play()
                menu()

          
        pygame.display.update()
def inicia_jogo():

    #música
    ''''
    on_of = False
    if on_of == False:
        pygame.mixer.music.stop() 
    '''
    
    Loop2= True
    while Loop2:
        
         #tela
         tela.fill((0,162,232))
         3131
         #textos
         textformat4= fonte2.render("(4)Voltar",True,(preto))
         textformat5= fonte3.render("(PLAYER)QUEM EU SOU?",True,(0,0,0))
         textformat6= fonte3.render("(.)Você é Cleiton, Seu objetivo é voltar para sua terra natal (RJ).",True,(0,0,0))
         textformat7= fonte3.render("(.)Mas para isso você deve passar por vários desafios.",True,(0,0,0))
         textformat8= fonte3.render("(.)Sua história começa em Trolha. Lá você terá que vencer a guerra.",True,(0,0,0))
         textformat9= fonte3.render("(.)Boa Sorte!",True,(0,0,0))
         iniciar = fonte3.render('Pressione (espaço) para INICIAR', True,(preto))
         #coordenadas
        
         #botões
         for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    sounds.play()
                    
                    fase1()
                    sounds.play()
                    Loop2 = False
                    
                if evento.key == pygame.K_4:
                    #música
                   
                    sounds.play()
                    #loop
                    Loop2 = False
                    menu()
        #desenhos
         todas_sprites.draw(tela)
        #fundobranco 
         pygame.draw.rect(tela,(255,255,255),(x,y, 630, 350))
         tela.blit(textformat4,(620,440))
         tela.blit(textformat5,(70,100))    
         tela.blit(textformat6,(70,120))   
         tela.blit(textformat7,(70,140))
         tela.blit(textformat8,(70,160))
         tela.blit(textformat9,(70,180))
         tela.blit(iniciar,(225,290))
         #atualização
         todas_sprites.update()
         pygame.display.flip() 
def leitura():
    pygame.mixer.music.load('sounds/waterfall.mp3')
    pygame.mixer.music.set_volume(0.5)
    waterfal = pygame.sprite.Group()
    fundo = Fundo()
    waterfal.add(fundo)
    iniciar = True
    pygame.mixer.music.play(-1)
    while iniciar: 
       
        textformat5= fonte3.render("Já se passaram 6 anos e você mudou.",True,(preto))
        textformat6= fonte3.render('Graças a sua conquista e aventura você adiquiriu',True,(0,0,0))
        textformat7= fonte3.render("uma nova arma. Seu objetivo e conversar com o rei, lutar com ",True,(0,0,0))
        textformat8= fonte3.render("Poseidon e voltar para o ERRIJOTA, sua terra natal.",True,(0,0,0))
        textformat9= fonte3.render("(...)Boa Sorte!",True,(0,0,0))
        iniciar = fonte3.render('Pressione (espaço) para INICIAR', True,(branco))
    
        frame.tick(60)
        tela.fill((branco))
        #textos
        for evento in pygame.event.get():
            #pygame.mixer.music.stop()
            if evento.type == pygame.QUIT:
                iniciar = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    sounds.play()
                    fase3_1()
                    iniciar = False
                    
        waterfal.draw(tela)  
        waterfal.update()
        
        #fundobranco 
       
        tela.blit(textformat5,(120,100))    
        tela.blit(textformat6,(120,120))   
        tela.blit(textformat7,(120,140))
        tela.blit(textformat8,(120,160))
        tela.blit(textformat9,(120,200))
        tela.blit(iniciar,(180,440))       
        #pygame.draw.rect(tela,(255,255,255),(x,y, 630, 350))
        pygame.display.flip()
def video2():
     webbrowser.open("fase1.mp4")

def inicia_creditos():
    creditos = pygame.image.load('imagens/creditos.png')
    Loop3 = True
    while Loop3:
        #tela
        tela.fill((0,0,0))
        tela.blit(creditos,( 0 ,0))
        #botões
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                Loop3 = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_4:
                    sounds.play()
                    Loop3 = False
        #textos e desenhos
        textformat4= fonte2.render("(4)Voltar",True,(preto))           
        tela.blit(textformat4,(620,420))
        #atualização
        pygame.display.update()
def fase1():
    fundo1 = pygame.image.load('imagens/plano.png')
    fundo = pygame.transform.scale(fundo1,(largura,altura))
    pygame.mixer.music.load('sounds/battle.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()
    
    fase1 = True
    while fase1:
        #tela
        tela.fill((0,0,0))
        tela.blit(fundo,(0,0))
        frame.tick(60)
        #botões

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fase1 = False
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    
                    fase1 = False
                    sounds.play()
                    pygame.mixer.music.stop()
                    
                    webbrowser.open("fugindo.mp4")
                    fase1_2()
                    
                    
                    
                elif evento.key == pygame.K_2:
                    pygame.mixer.music.stop()
                    sounds.play()
                    video_player()
                    iniciar_fase2()
                    fase1 = False     
                   
        #desenho
        pygame.draw.rect(tela,(branco),( x,y,630,350))

        #textos
        texto_fase1_1 = fonte3.render("(Aliado) Senhor!Como vamos vencer esta guerra?",True,(0,0,0))
        texto_fase1_2 = fonte3.render("(Aliado) Metade do nosse exército morreu!",True,(0,0,0))
        texto_fase1_3 = fonte3.render("(1) Fugir",True,(0,0,0))
        texto_fase1_4 = fonte3.render("(2) Constuir um cavalo de madeira cheio de soldados e entregar de ",True,(0,0,0))
        texto_fase1_5 = fonte3.render("    presente para o inimigo e depois saquear a vila!",True,(0,0,0))
        
                
        tela.blit(texto_fase1_1,(70,100))    
        tela.blit(texto_fase1_2,(70,120))   
        tela.blit(texto_fase1_3,(70,140))
        tela.blit(texto_fase1_4,(70,160))
        tela.blit(texto_fase1_5,(70,175))
        
    
        #atualização
        pygame.display.update()
def menu():
    on_of = True
    musica_fundo = pygame.mixer.music.load('sounds/trilhadojogo.mp3')
    if on_of == True:
         musica_fundo = pygame.mixer.music.play(-1)
    #loop
    Loop1= True
    while Loop1:
        #música
        on_of = True
        #tela e fps
        tela.fill((0,0,0))
        frame.tick(60)
        #fonte
        textformat1 = fonte.render("(1)Começar",True,(255,255,255))
        textformat2 = fonte.render("(2)Créditos",True,(255,255,255))
        textformat3= fonte.render("(3)Sair",True,(255,255,255))

        textformat = fonte1.render("MENU",True,(255,255,255))
        #botões
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                Loop1 = False
            #sair
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_3:
                    sounds.play()
                    Loop1 = False
                #jogar
                elif evento.key == pygame.K_1:
                    
                    sounds.play()
                    inicia_jogo()
                    Loop1 = False
                    
                #créditos
                elif evento.key == pygame.K_2:
                    sounds.play()
                    inicia_creditos()
        #imagens
        #tela.blit(skynight,(0,0))
        #tela.blit(chao,(0,420))
        '''
        tela.blit(sol,(xs,ys))
        tela.blit(lua, (xl, yl))
        animações
        '''
        #sprites
        todas_sprites.draw(tela)
        #textos
        tela.blit(textformat1,((largura-350)/2, (altura-340)))
        tela.blit(textformat2,((largura-350)/2, (altura-260)))
        tela.blit(textformat3,((largura-350)/2, (altura-180)))
        
        tela.blit(textformat,((largura-180)/2, (altura-440)))
          
    
        #atualização
        todas_sprites.update()
        pygame.display.flip()
def fasedois():
    musica = pygame.mixer.music.load('sounds/battle.mp3')
    musica = pygame.mixer.music.play(-1)
    musica = pygame.mixer.music.set_volume(0.3)
    fase2()
    '''''
    fase2 = True
    while fase2:
        tela.fill((branco))
        #textos
        text_fase2 = fonte4.render("Código",True,(preto))
        tela.blit(text_fase2,(50,175))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fase2= False
            if evento.type == pygame.KEYDOWN:
                fase2 = False
                sounds.play()
                leitura()
        pygame.display.update()
'''''
#loop
menu()
