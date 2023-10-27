from tkinter import Menu, Menubutton
import pygame
from pygame.locals import *
from sys import exit
import webbrowser
from fase1_3 import *


pygame.init()

#cores
branco = (255,255,255)
preto = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
verde = (0,255,0)
amarelo = (0,255,255)

#px
largura = 720
altura = 480 

centrolar = (largura/2-30)
centroalt = (altura/2-30)

a = (largura/2-30)
b = (altura/2-30)  

fonte2 = pygame.font.SysFont('Bold',30, True, False)




#tela
frame = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))
terreno = pygame.image.load('imagens/fase1_2/masmorra.png')
fundo = pygame.transform.scale(terreno,(largura,altura))
#sons
gunsound = pygame.mixer.Sound('sounds/gunsound.mp3')
#player
personagem = pygame.image.load('sprites/personagem.png')
playerr = pygame.transform.scale(personagem,(110//2, 150//2))
arma = pygame.transform.scale(personagem,(36//2,36//2))
gun = pygame.transform.scale(arma,(560//3,70//3))
#bot
#bot1 = pygame.image.load('sprites/poseidon.png')
#bot = pygame.transform.scale(bot1,(720//3,480//3))
#funçoes

    
    
def fase1_2():
         cs = 0
         gmovy = 0
         gmovx = 0
         xmov = 0
         ymov = 0
         x = 60
         y = 300

         monster = True

         pygame.mixer.music.stop()
         pygame.mixer.music.load('sounds/masmorra.ogg')
         pygame.mixer.music.set_volume(2)     

         xb = 260
         yb = 10
         xbx = 0
         xby = 0
       
         key = pygame.key.get_pressed()
        
         pygame.mixer.music.play(-1)
         fase1_2 = True
         while fase1_2:
               frame.tick(15)
               tela.fill((branco))
              
                   
               #colisões_cenário
               bau = pygame.draw.rect(tela,amarelo,(280,150,50,10))

               monstro = pygame.draw.rect(tela,verde,(600,210,20,30))

               parede1 =  pygame.draw.rect(tela,blue,(50,0,10,480))
               parede2 =  pygame.draw.rect(tela,preto,(410,265,10,100))
               parede3 =  pygame.draw.rect(tela,blue,(410,400,10,100))
               parede4_temp =  pygame.draw.rect(tela,preto,(210,260,10,100))
               parede5_pass =  pygame.draw.rect(tela,preto,(210,0,1,480))
               parede7 =  pygame.draw.rect(tela,blue,(515,0,1,130))
               parede8 =  pygame.draw.rect(tela,blue,(550,0,1,130))
               parede9 =  pygame.draw.rect(tela,blue,(450,150,1,50))
               parede6 =  pygame.draw.rect(tela,blue,(510,150,2,100))
               parede10 =  pygame.draw.rect(tela,red,(540,150,20,100))
               parede11 =  pygame.draw.rect(tela,blue,(240,210,2,20))
               parede12 =  pygame.draw.rect(tela,blue,(180,260,2,60))
               paredinha1 =  pygame.draw.rect(tela,branco,(180,350,2,20))
               bloco1 =  pygame.draw.rect(tela,red,(240,230,120,80))
               chao1 =  pygame.draw.rect(tela,blue,(200,440,220,10))
               chao2 =  pygame.draw.rect(tela,preto,(420,400,200,10))
               chao3 =  pygame.draw.rect(tela,red,(250,150,200,5))
               bloco2 =  pygame.draw.rect(tela,red,(190,140,80,30))
               chao4 =  pygame.draw.rect(tela,blue,(240,200,210,10))
               chao5 =  pygame.draw.rect(tela,blue,(60,220,150,10))
               chao6 =  pygame.draw.rect(tela,blue,(60,340,150,10))
               chao7 =  pygame.draw.rect(tela,blue,(420,360,150,10))
               chao8 =  pygame.draw.rect(tela,blue,(420,120,100,10))
               chao9 =  pygame.draw.rect(tela,blue,(550,120,50,10))

               parede14 =  pygame.draw.rect(tela,blue,(410,265,10,100))
               parede15 =  pygame.draw.rect(tela,blue,(600,310,10,100))
               parede16 =  pygame.draw.rect(tela,blue,(560,270,10,100))
               parede17 =  pygame.draw.rect(tela,blue,(630,60,10,250))
               bloco3 =  pygame.draw.rect(tela,red,(540,240,60,40))
               bloco4 =  pygame.draw.rect(tela,red,(600,310,60,40))
               parede20 =  pygame.draw.rect(tela,blue,(590,90,10,100))
               bloco5 =  pygame.draw.rect(tela,red,(350,200,80,70))

               #arvore4 =  pygame.draw.rect(tela,preto,(90*3,60*4,90,180))
               #arvore5 =  pygame.draw.rect(tela,preto,(90*5,60*3.5,90,180))

               #barranco1=  pygame.draw.rect(tela,branco,(90*3,50*2,150,70))
               #barranco2=  pygame.draw.rect(tela,branco,(90*4,50*3,250,30))
               #barranco3=  pygame.draw.rect(tela,branco,(400,140,150,70))
               #barranco4=  pygame.draw.rect(tela,branco,(530,120,60,90))
               #barranco5 =  pygame.draw.rect(tela,branco,(560,120,60,60))

               #barranco6=  pygame.draw.rect(tela,preto,(600,200,200,60))

               portal =  pygame.draw.rect(tela,branco,(470,0,90,30))
                    #cenário
               
               player = pygame.draw.rect(tela,0,(x, y ,16,16))#parte física
               tela.blit(fundo,(0,0))
               #personagem
               #tela.blit(bot,(xb,yb),(xbx, xby, 150//3, 200//3))#parte animada
               xbx = xbx + 66
               if xbx >= 200:
                   xbx = 0
               xby = xby + 0

               
               tela.blit(playerr,(x,y),(((xmov*36)//2), ymov , 36//2, 36//2))#parte animada
               
               for evento in pygame.event.get():
                  if evento.type == pygame.QUIT:
                     fase1_2 = False
                  #if evento.type ==  pygame.KEYDOWN:
               

               
#movimento     
               
               xg = x+20
               yg = y + 5

               key = pygame.key.get_pressed()
               '''
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

                   if 50>yg>20:
                         xb = xb - 10
                         yb = yb -1
                         print('foi de arrasta pra cima')
                         if xb == x:
                             pygame.mixer_music.stop()
                             webbrowser.open("poseidon.mp4")
                             xb = -49
              '''     
               if key[K_RIGHT]:
                    direita = True
                    esquerda = False
                    baixo = False
                    cima = False
                    x = x + 5
                    ymov = (38//2)*2
                    xmov = xmov + 1

               elif key[K_LEFT]:
                    esquerda = True
                    direita =False
                    baixo = False
                    cima = False
                    x = x - 5
                    ymov = 38//2
                    xmov = xmov + 1

               elif key[K_UP]:
                    cima = True
                    baixo = False
                    esquerda = False
                    direita =False
                    y = y - 5
                    ymov = 115//2
                    xmov = xmov + 1

               elif key[K_DOWN]:
                    baixo = True
                    cima =False
                    esquerda = False
                    direita =False
                    y = y + 5
                    ymov = 0
                    xmov = xmov + 1

               else:
                    
                    '''''
                    if ymov == 37*2:
                         ymov = 37*2
                    elif ymov == 38:
                         ymov = 38
                    '''''
                    xmov = xmov + 0
               if xmov >= 3:
                   xmov = 0
#Colisão

               chao =  pygame.draw.rect(tela,preto,(-10, 477,730,6))
               paredelefth =  pygame.draw.rect(tela,preto,(-5,-10 ,6,730))
               parederight =  pygame.draw.rect(tela,preto,(719, -10,6,730))
               teto=  pygame.draw.rect(tela,preto,(-10, -5 ,730,6))
               
               #colisão no cenário
               
               if player.colliderect(parede1):
                  x = x + 5
            
               if player.colliderect(parede2):
                  
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5

                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5
                
               
               if player.colliderect(parede3):
                x = x - 5

               if player.colliderect(parede12):
                  x = x - 5
                

               if player.colliderect(bloco1):
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5
               if player.colliderect(parede14):
                      x = x - 5

                
               if player.colliderect(parede15):
                  
                     x = x - 5
               if player.colliderect(parede16):
                  
                    x = x + 5

               if player.colliderect(parede17):
                   x = x - 5

               if player.colliderect(bloco3):
                  
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5

                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5
               if player.colliderect(bloco4):
                  
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5

                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5
               if player.colliderect(parede20):
                      x = x - 5

               if player.colliderect(parede7):
                   x = x + 5
        

               if player.colliderect(parede8):
                  x = x -5

               if player.colliderect(parede9):
                      x = x - 5
                
               if player.colliderect(parede10):
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5
                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5

               if player.colliderect(parede11):
                      x = x - 5
                  

               if player.colliderect(chao7):
                      y = y + 5
                  


               if player.colliderect(chao4):
                     y = y - 5
                
               if player.colliderect(chao5):
                      y = y + 5

               if player.colliderect(chao6):
                      y = y - 5

               if player.colliderect(chao8):
                      y = y + 5
                  
               if player.colliderect(bloco2):
                  
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5

                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5

               if player.colliderect(chao9):
                    y = y + 5

               if player.colliderect(bloco5):
                  
                  if esquerda == True and direita == False:
                      x = x + 5
                  elif direita == True and esquerda == False :
                      x = x - 5

                  elif cima == True and baixo == False :
                      y = y + 5
                  elif baixo == True and cima == False:
                      y = y - 5

               if player.colliderect(parede6):
                  x = x - 5
                 
               #
               if player.colliderect(chao1) :
                  y = y - 5

               if player.colliderect(chao2):
                  y = y - 5

               if player.colliderect(chao3):
                  y = y + 5

               if player.colliderect(portal):
                   fase1_2 = False
                   pygame.mixer.music.stop()
                   webbrowser.open("fase1_2.mp4")
                   iniciar3()
                   
               if player.colliderect(parede5_pass) and x > 200:
                       x = x + 5

               if player.colliderect(bau):
                   pygame.draw.rect(tela,(255,255,255),(x,y, 210, 100))
                   textformat4= fonte2.render("Pressione CTRL",True,(preto))
                   textformat5= fonte2.render("para inibir o monstro",True,(preto))
                   tela.blit(textformat4,(x,y))
                   tela.blit(textformat5,(x,y+20))
                   if key[K_LCTRL]:
                       print('INIBIDO')
                       monster = False
                       
               if monster == True:
                    if player.colliderect(monstro):
                        pygame.mixer.music.stop()
                        fase1_2 = False
                        webbrowser.open("morreu_ciclope.mp4")
                  
               pygame.display.flip()

#fase1_2()
#jogo


