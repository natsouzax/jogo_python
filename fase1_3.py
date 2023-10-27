import pygame
from pygame.locals import *
from sys import exit
import webbrowser
pygame.init()


branco = (255,255,255)
preto = (0,0,0)
red = (255,0,0)

largura = 720
altura = 480 

centrolar = (largura/2-30)
centroalt = (altura/2-30)

a = (largura/2-30)
b = (altura/2-30)  



#tela
frame = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
terreno = pygame.image.load('imagens/fase3fundo.png')
fundo = pygame.transform.scale(terreno,(largura,altura))
#sons
gunsound = pygame.mixer.Sound('sounds/gunsound.mp3')
#player
personagem = pygame.image.load('sprites/personagem.png')
arma = pygame.image.load('imagens/arma.png')
gun = pygame.transform.scale(arma,(560//3,70//3))
#bot
bot1 = pygame.image.load('sprites/poseidon.png')
bot = pygame.transform.scale(bot1,(660/2,780/2))
#funçoes

 
    
def fase1_3():
         pygame.mixer.music.load('sounds/battle.mp3')
         pygame.mixer.music.set_volume(0.5)
         pygame.mixer.music.play()
         cs = 0
         gmovy = 0
         gmovx = 0
         xmov = 0
         ymov = 0
         x = 10
         y = 400
         morte = 0
         
              
         xb = 260
         yb = 0
         xbx = 0
         xby = 0
         
         
         
         fase3 = True
         while fase3:
               frame.tick(15)
               tela.fill((branco))
               player = pygame.draw.rect(tela,0,(x, y ,36,36))#parte física
               #colisões_cenário
               
               arvore1 =  pygame.draw.rect(tela,preto,(180,90,90,180))
               arvore2 =  pygame.draw.rect(tela,preto,(0,0,60,140))
               arvore3 =  pygame.draw.rect(tela,red,(90*3,0,90,80))
               arvore4 =  pygame.draw.rect(tela,red,(90*3,60*4,90,160))
               arvore5 =  pygame.draw.rect(tela,preto,(90*5,60*3.5,90,160))

               barranco1=  pygame.draw.rect(tela,branco,(90*3,50*2,150,70))
               barranco2=  pygame.draw.rect(tela,branco,(90*4,50*3,250,30))
               barranco3=  pygame.draw.rect(tela,branco,(400,140,150,70))
               barranco4=  pygame.draw.rect(tela,branco,(530,120,60,90))
               barranco5 =  pygame.draw.rect(tela,red,(560,140,50,70))

               #barranco6=  pygame.draw.rect(tela,preto,(600,200,200,60))

               portal =  pygame.draw.rect(tela,branco,(470,0,90,30))
                    #cenário
               
               tela.blit(fundo,(0,0))

               #personagem
               tela.blit(bot,(xb,yb),(xbx, xby, 140//2, 170//2))#parte animada
               

               tela.blit(personagem,(x,y),(xmov*36, ymov , 36, 36))#parte animada
               
               for evento in pygame.event.get():
                  if evento.type == pygame.QUIT:
                     fase3= False
                  #if evento.type ==  pygame.KEYDOWN:
               

               
#movimento     
               
               xbx = xbx + 80
               if xbx >= 200:
                    xbx = 0

               xg = x + 20
               yg = y + 5

               key = pygame.key.get_pressed()

               if key[K_RCTRL] and  direita == True:
                  
                   
                   tela.blit(gun,(xg,yg),(gmovx*45,gmovy*32,45,32))
                   gmovx = gmovx + 2
                   cs = cs +1
                   if gmovx >=4:
                       gmovx = 0


                   if  cs ==3:
                       gunsound.play()
                       if cs >=2:
                           cs = 0

                   if 70>yg>10:

                         xb = xb - 5
                         morte = morte + 1   
                         print('foi de arrasta pra cima')

                         if morte >= 15:
                             
                             pygame.mixer_music.stop()
                             webbrowser.open("poseidon.mp4")
                             xb = -59
                
                   
               elif key[K_RIGHT]:
                    direita = True
                    esquerda = False
                    baixo = False
                    cima = False
                    x = x + 5
                    ymov = 37*2
                    xmov = xmov + 1

               elif key[K_LEFT]:
                    
                    

                    esquerda = True
                    direita =False
                    baixo = False
                    cima = False
                    x = x - 5
                    ymov = 38
                    xmov = xmov + 1

               elif key[K_UP]:
                    cima = True
                    baixo = False
                    esquerda = False
                    direita =False
                    y = y - 5
                    ymov = 110
                    xmov = xmov + 1

               elif key[K_DOWN]:
                    baixo = True
                    cima =False
                    esquerda = False
                    direita =False
                    y = y + 5
                    ymov = 0
                    xmov = xmov + 1
               
                    
                    if xby >=550:
                        lope = False
                        xbx = xbx + 0
                    
               
               if xmov >= 3:
                   xmov = 0
#Colisão

               chao =  pygame.draw.rect(tela,preto,(-10, 477,730,6))
               paredelefth =  pygame.draw.rect(tela,preto,(-5,-10 ,6,730))
               parederight =  pygame.draw.rect(tela,preto,(719, -10,6,730))
               teto=  pygame.draw.rect(tela,preto,(-10, -5 ,730,6))
               
               #colisão no cenário
               if player.colliderect(arvore1):
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5

               if player.colliderect(arvore2):
                  
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5

                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5

               if player.colliderect(arvore3):
                  if xb <= 0:
                    x = x +0
                    y = y + 0
                  elif esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5

               if player.colliderect(arvore4):
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5

               if player.colliderect(arvore5):
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5
               #barranco
               if player.colliderect(barranco1):
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5

               if player.colliderect(barranco2):
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5

               if player.colliderect(barranco3):
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5

               if player.colliderect(barranco4):
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5

               if player.colliderect(barranco5):
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5
               '''
               if player.colliderect(barranco6):
                 
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5
                '''
               #
               if player.colliderect(chao) :
                  y = y - 5

               if player.colliderect(teto):
                  y = y + 5

               if player.colliderect(paredelefth):
                  x = x + 5
               
               if player.colliderect(parederight):
                  x = x - 5
               
               if player.colliderect(portal):
                   if xb== -59:
                       
                       webbrowser.open("final1_3(1).mp4")
                   else:
                       pygame.mixer.music.stop()
                       webbrowser.open("final1_3(2).mp4")
                       
                   fase3 = False
                   
                   



               pygame.display.flip()

def iniciar3():
    sounds = pygame.mixer.Sound('sounds/clique.mp3')
    fonte4 = pygame.font.SysFont('Bold',80, True, False)
    iniciar3 = True
    while iniciar3:
        tela.fill((branco))
        #textos
        text_fase2 = fonte4.render("Aperte Qualquer Tecla",True,(preto))
        tela.blit(text_fase2,(50,175))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                iniciar3 = False
            if evento.type == pygame.KEYDOWN:
                iniciar3 = False
                sounds.play()
                fase1_3()
        pygame.display.update()  

#iniciar3()
#jogo


