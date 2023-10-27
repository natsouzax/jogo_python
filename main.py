import pygame
import sys
import math
import random
import webbrowser
#from Jogo import perdeu
from fase3 import *


#from Jogo import *
pygame.init()
pygame.mixer.init()

# Constantes para o jogo
matheus = [
        pygame.mixer.Sound('sounds/aaa.ogg'),
        pygame.mixer.Sound('sounds/zezao.ogg'),
        pygame.mixer.Sound('sounds/peste.ogg')
    ]
piu = pygame.mixer.Sound('sounds/es_flecha.ogg')
sounds = pygame.mixer.Sound('sounds/clique.mp3')
x = 0
y = 0
width = 720
height = 480
ground_level = height - 50
gravity = 0.5
jump_force = -10
clock = pygame.time.Clock()
dano = pygame.mixer.Sound('sounds/hurting.mp3')
#musica_principal = pygame.mixer.music.load('sounds/battle.mp3')
#musica_principal = pygame.mixer.music.set_volume(0.3)
screen = pygame.display.set_mode((width, height))

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
        

class Animation:
    def __init__(self, images, position, speed):
        self.directions = ['right', 'left', 'up', 'down']
        self.frames = {}
        self.frame_index = {}
        self.animation_speed = speed
        self.last_update = pygame.time.get_ticks()
        self.rect = None
        self.velocity = [0, 0]
        self.stopped = True
        self.collisions_count = 0  # Contador de colisões com o inimigo
        self.is_alive = True  # Variável para verificar se a animação está viva


        for direction in self.directions:
            self.frames[direction] = []
            self.frame_index[direction] = 0

        for direction, image_list in images.items():
            for path in image_list:
                image = pygame.image.load(path)
                self.frames[direction].append(image)

        self.current_direction = 'down'
        self.image = self.frames[self.current_direction][0]
        self.rect = self.image.get_rect()
        self.pos_y0 = height - 70 - 31//2
        self.rect.topleft = position
        self.jump = False

    def pular(self):
        if not self.jump and self.rect.y == self.pos_y0:  # Verifica se a animação está no chão antes de pular
            self.jump = True
            self.rect.y -= 1
    
    def update(self):
        if self.jump:
            if self.rect.y <= 300 - (10 // 100):
                self.jump = False
            self.rect.y -= 10
        else:
            if self.rect.y < self.pos_y0:
                self.rect.y += 6
            else:
                self.rect.y = self.pos_y0

        if not self.stopped:
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]

            current_time = pygame.time.get_ticks()
            if current_time - self.last_update >= 1000 / self.animation_speed:
                self.frame_index[self.current_direction] = (self.frame_index[self.current_direction] + 1) % len(self.frames[self.current_direction])
                self.image = self.frames[self.current_direction][self.frame_index[self.current_direction]]
                self.last_update = current_time

            if self.rect.colliderect(chao_rect):
            # Se houver colisão, impedir o movimento para a direita
                if self.velocity[0] > 0:  # Verifica se está indo para a direita
                    self.velocity[0] = 0

        if self.velocity[0] == 0 and self.velocity[1] == 0:
            self.stopped = True

    def set_direction(self, direction):
        if direction in self.directions:
            self.current_direction = direction

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect

class Arrow:
    def __init__(self, position, direction):
        self.image = pygame.image.load("sprites/arrow.png")
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.direction = direction
        self.velocity = [0, 0]
        self.speed = 3
        self.collisions = 0
        #self.enemies_hit = []
        #self.enemies_hit = set()

        if direction == 'left':
            self.velocity[0] = -self.speed
            self.image = pygame.transform.rotate(self.image, 180)  # Rotaciona a flecha para a esquerda
        elif direction == 'right':
            self.velocity[0] = self.speed
        elif direction == 'up':
            self.velocity[1] = -self.speed
            self.image = pygame.transform.rotate(self.image, 90)  # Rotaciona a flecha para cima
        elif direction == 'down':
            self.velocity[1] = self.speed
            self.image = pygame.transform.rotate(self.image, -90)

    def update(self, enemies):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class FightingEnemy:
    def __init__(self, x, y, screen_width):
        self.velocity = [1, 0]
        self.screen_width = screen_width

        # Carregar imagens da animação
        self.images = [pygame.image.load("sprites/enemy_1.png"), pygame.image.load("sprites/enemy_2.png"), pygame.image.load("sprites/enemy_3.png")]
        self.image_index = 0
        self.image_timer = 0
        self.image_delay = 200  # Delay em milissegundos entre as mudanças de imagem
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.collisions_count = 0
        self.is_alive = True
        self.collided = False
        self.player = animation
        self.velocidade_do_inimigo = 1
        self.pos_y0 = height - 70 - 31//2

    def follow_player(self):
        pass

    def update(self, chao_rect):
        if self.player:
            dx = self.player.rect.x - self.rect.x
            dy = self.player.rect.y - self.rect.y
            distance = math.sqrt(dx**2 + dy**2)
            if distance != 0:
                dx /= distance
                dy /= distance
            self.rect.x += dx * self.velocidade_do_inimigo
            self.rect.y += dy * self.velocidade_do_inimigo
            
        # Movimentar o inimigo
        self.rect.x += self.velocity[0]

        # Verificar colisão com o chão e inverter a direção
        if not chao_rect.contains(self.rect):
            self.velocity[0] *= -1

        # Atualizar a animação
        current_time = pygame.time.get_ticks()
        if current_time - self.image_timer >= self.image_delay:
            self.image_timer = current_time
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
        # Verificar colisões com o retângulo chao_posicao
        if self.rect.colliderect(chao_rect):
            self.is_colliding = True
            if self.velocity[0] > 0:  # Se estava indo para a direita antes da colisão
                self.rect.x -= chao_rect.left  # Definir a posição do inimigo para a esquerda do retângulo
            elif self.velocity[0] < 0:  # Se estava indo para a esquerda antes da colisão
                self.rect.left = chao_rect.right  # Definir a posição do inimigo para a direita do retângulo
        else:
            self.is_colliding = False

        # Ajustar a direção de movimento baseado em is_colliding
        if self.is_colliding:
            self.velocity[0] = -self.velocity[0]  # Inverter a direção horizontal

            # Inverter a imagem quando mudar de direção
            self.image = pygame.transform.flip(self.image, True, False)

        

        # Garantir que o inimigo permaneça na tela
        if self.rect.left < 0:
            self.rect.left = 0
            self.velocity[0] = abs(self.velocity[0])
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
            self.velocity[0] = -abs(self.velocity[0])
        # Fazer o inimigo voltar quando sair da tela
        #if self.rect.left < 0 or self.rect.right > self.screen_width:
        #    self.velocity[0] *= -1

    #def take_damage(self, damage):
    #    self.health -= damage
    #    if self.health <= 0:
    #        # Inimigo derrotado, você pode adicionar a lógica para removê-lo da tela ou reiniciar a luta
    #        pass

    def attack(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Chaos:
    def __init__(self, x0, y0, x1, y1):
        self.chao_posicao = pygame.Rect(x0, y0, x1, y1)
''''
class Health:
    def __init__(self):
        self.images = [pygame.image.load('imagens/l0_vida1.png'), pygame.image.load('imagens/l0_vida2.png'), pygame.image.load('imagens/l0_vida3.png'), 
                       pygame.image.load('imagens/l0_vida4.png'), pygame.image.load('imagens/l0_vida5.png')]

    def update(self, animation, screen):  # You need to pass the animation and screen parameters here
        if animation.collisions_count <= 12:
            screen.blit(self.images[0], (x, y))  # You need to specify the position (x, y) to blit the image

        elif animation.collisions_count <= 24:
            screen.blit(self.images[1], (x, y))

        elif animation.collisions_count <= 36:
            screen.blit(self.images[2], (x, y))

        elif animation.collisions_count <= 48:
            screen.blit(self.images[3], (x, y))

        else:
            screen.blit(self.images[4], (x, y))
'''
#class Game_Over:
#    def __init__(self):
#        self.imagem = pygame.image.load('game_over.jpg')
#
#    def update(self):
#        while game_over:
#            self.imagem.blit(screen)
#            if event.type == pygame.KEYDOWN:
#                if event.key == pygame.K_1:
#                    game_over = False
#
#                if event.key == pygame.K_2:
#                    pygame.quit()


image_paths = {
    'right': ["sprites/animation_right1.png", "sprites/animation_right2.png", "sprites/animation_right3.png"],
    'left': ["sprites/animation_left1.png", "sprites/animation_left2.png", "sprites/animation_left3.png"],
    'up': ["sprites/animation_up1.png", "sprites/animation_up2.png"],
    'down': ["sprites/animation_down1.png", "sprites/animation_down2.png", "sprites/animation_down3.png"]
}

animation = Animation(image_paths, (0, 0), 7)
enemies = [FightingEnemy(300, ground_level - 50, width)]
enemy = FightingEnemy(300, ground_level - 50, width)
chao = Chaos(452, 235, 552, 335)
chao_rect = chao.chao_posicao
arrows = []
collision_limit = 60
game_over = False
flecha = Arrow((0,0), image_paths)
#vida = Health()
GameLoop = True
gg = False
#pygame.mixer.music.play(-1)

#fontes
fonte4 = pygame.font.SysFont('Bold',80, True, False)
fonte3 = pygame.font.SysFont('Monospace',15, True, False)
fonte2 = pygame.font.SysFont('Bold',30, True, False)
fonte1 = pygame.font.SysFont('Monospace',80, True, False)
fonte = pygame.font.SysFont('Monospace',60, True, True)     

def iniciar_fase3():
    pygame.mixer.music.load('sounds/waterfall.mp3')
    pygame.mixer.music.set_volume(0.5)
    waterfal = pygame.sprite.Group()
    fundo = Fundo()
    waterfal.add(fundo)
    iniciar = True
    pygame.mixer.music.play(-1)
    while iniciar: 
       
        textformat5= fonte3.render("Já se passaram 6 anos e você mudou.",True,(preto))
        textformat6= fonte3.render('Graças a sua conquista e aventura você adquiriu',True,(0,0,0))
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
def fase2():
    vida1 = pygame.image.load('sprites/vida.png')
    #vida = pygame.transform.scale(vida1,(200,200))
    cvd = 0 #contador de vida
    xv = 0
    yv = 0
    collision_limit = 4
    game_over = False
    GameLoop = True
    while GameLoop:
        
        
    
        for event in pygame.event.get():
            if flecha.collisions >= 50:
                GameLoop = False
                game_over = True
                

            if animation.is_alive and animation.get_rect().colliderect(enemies[0] or enemies[1] or enemies[2].rect):
                # Incrementar o contador de colisões do inimigo com a animação
                #print('ok')
                enemies[0].collisions_count += 1
                cvd = cvd + 1
                if cvd >= 1:
                    yv = yv + 100

                dano.play()
            # Se o inimigo colidir com a animação o número especificado de vezes, encerrar o jogo
            if enemies[0].collisions_count >= collision_limit:
                
               
                print('Atingiu o limite')
                animation.is_alive = False  # O jogador morre
                game_over = True
                GameLoop = False

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    animation.velocity[0] = -4
                    animation.set_direction('left')
                    animation.stopped = False
                elif event.key == pygame.K_RIGHT:
                    animation.velocity[0] = 4
                    animation.set_direction('right')
                    animation.stopped = False
                elif event.key == pygame.K_UP:
                    animation.pular()
                    animation.stopped = False
                elif event.key == pygame.K_LCTRL or event.key == pygame.K_RCTRL:
                    arrow = Arrow(animation.rect.center, animation.current_direction)
                    arrows.append(arrow)
                    piu.play()

            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    animation.velocity[0] = 0

            if game_over:
                while game_over:  # Loop para exibir a tela de "Game Over" até o jogador fechar o jogo
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()

                    # Limpar a tela antes de exibir a mensagem de "Game Over"
                    screen.fill((0, 0, 0))

                    #Exibir tela final
                    if flecha.collisions >= 50:
                        ganhou = webbrowser.open("ciclope_morte.mp4")
                        GameLoop = False
                        iniciar_fase3()
                        
                        #gg = True
                    else:
                        fim_de_jogo = webbrowser.open("morreu_ciclope.mp4")
                      

                        #gg = False

                    if gg == True:
                        GameLoop = False
                        fase3_1()
                    screen.blit(fim_de_jogo, (width // 2 - fim_de_jogo.get_width() // 2, height // 2 - fim_de_jogo.get_height() // 2))
                    screen.blit(ganhou, (width // 2 - ganhou.get_width() // 2, height // 2 - ganhou.get_height() // 2))
                    pygame.display.flip()

                    # Aguardar 2 segundos antes de fechar a janela do jogo
                    pygame.time.delay(2000)

        clock.tick(60)
        animation.update()
        
        img_fundo = pygame.image.load('imagens/cave.png')
        img_fundo = pygame.transform.scale(img_fundo, (width, height))
        screen.blit(img_fundo, (0, 0))
        
        tela.blit(vida1,(0,0),(xv, yv, 140, 100))#vida
        

        while True:    
            som_escolhido = random.choice(matheus)
            break
        
        for arrow in arrows:
            arrow.update(enemies)
            if arrow.rect.colliderect(enemy.rect):
                arrows.remove(arrow)
                flecha.collisions += 1
                if flecha.collisions == 10 or flecha.collisions == 20 or flecha.collisions == 30 or flecha.collisions == 40 or flecha.collisions == 50 or flecha.collisions == 55:# or 20 or 30 or 40 or 50 or 55:
                    som_escolhido.play()

        # Verificar colisões entre a animação e o inimigo
        for enemy in enemies:
            if animation and animation.get_rect().colliderect(enemy.rect):
                # Implementar ações quando a animação colidir com o inimigo
                pass

        # Atualizar e desenhar os inimigos
        for enemy in enemies:
            if enemy.is_alive:
                enemy.update(chao_rect)
                enemy.draw(screen)

        # Desenhar as flechas
        for arrow in arrows:
            arrow.draw(screen)
            

        # Desenhar a animação
        animation.draw(screen)

        #vida.update(animation, screen)

        # Atualizar a tela
        pygame.display.flip()

#fase2()