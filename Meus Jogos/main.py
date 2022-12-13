# Jogo de nave simples

import pygame, random
pygame.init()

# 1 - Dimensões da Tela do Jogo:
x = 1280   # Largura
y = 720    # Altura

# 2 - Definir Python para Abrir a Janela do Jogo:
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption('Meu Jogo em Python')
# Se tentar abrir a tela agora, a janela vai surgir e sair no mesmo instante, pois ainda não há um laço de repetição
# para manter a janela aberta.

bg = pygame.image.load('Imagens/Fundo.jpg').convert_alpha() # Para baixar o background e transformar ele em alpha
bg = pygame.transform.scale(bg, (x, y)) # Convertemos o tamanho do background para o tamanho de x e y.

# criando o inimigo do jogo (alien, no caso)
alien = pygame.image.load('imagens/Alien.png').convert_alpha()
alien = pygame.transform.scale(alien, (100,100))

# Criando a nave do jogador:
playerImg = pygame.image.load('Imagens/Nave 2.png')
playerImg = pygame.transform.scale(playerImg, (200,200)) #conversao do tamanho da nave
playerImg = pygame.transform.rotate(playerImg, -90) # Para rotacionar a nave em -90 graus

missil = pygame.image.load('Imagens/missil.jpg').convert_alpha()
missil = pygame.transform.scale(missil, (50,50))
missil = pygame.transform.rotate(missil, 0)

pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

vel_x_missil = 0
pos_x_missil = 250 #200 para que a imagem do missil fique sobreposta a da nave
pos_y_missil = 300

# 3 - Criando Loop para Manter a Janela Aberta:
rodando = True

# Funções:
#Função para fazer o alien reaparecer em um determinado local depois de sair da tela.


def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]


# O fato do "rodando" já ser True dispensa a necessidade de colocar True depois de while no loop abaixo (eu acho).
while rodando:
    for event in pygame.event.get(): # Estrutura criada para parar o loop
        if event.type == pygame.QUIT:
            rodando = False

            screen.blit(bg, (0,0)) # Cria fundo na posição 0, 0 (x e y respectivamente)

    # Criando carrossel do background
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    # Comando de movimento da nave:
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_alien_y > 1:
        pos_player_y -= 1
    if tecla[pygame. K_DOWN] and pos_player_y < 665:
        pos_player_y += 1

    #respawn
    if pos_alien_x == -5:
        pos_alien_x = respawn()[0] # Zero corresponde a x na função respawn lá em cima
        pos_alien_y = respawn()[1] # Um corresponde a y na função respawn lá em cima

    #movimento
    x -= 2
    pos_alien_x -= 1

    #criando as imagens
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missil, (pos_x_missil, pos_y_missil))
    screen.blit(playerImg, (pos_player_x, pos_player_y))

    pygame.display.update()