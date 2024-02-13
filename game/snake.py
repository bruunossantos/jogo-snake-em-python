import pygame
import random

pygame.init()
pygame.display.set_caption("Sake a Cobrinha")
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#------cores do game------

cor1 = (0, 0, 0) #Preto 
cor2 = (255, 255, 255) #Branco
cor3 = (255, 0, 0) #Vermelho
cor4 = (0, 255, 0) #Vermelho

#------Parametros------

tamanho_quadrado = 10
velocidade_jogo = 15

#------Jogo------

def menu():
    tela.fill(cor1)
    fonte = pygame.font.SysFont('Helvetica', 40)
    fonte2 = pygame.font.SysFont('Helvetica', 20)
    texto1 = fonte.render('Game Over', True, cor2)
    texto2 = fonte2.render('    Pressione ENTER para tentar novamente', True, cor2)
    tela.blit(texto1, [largura/2 - 100, altura/2 - 30])
    tela.blit(texto2, [largura/2 - 200, altura/2 + 30])
    pygame.display.update()

    aguardando_escolha = True
    while aguardando_escolha:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    return True
    return False


def gerar_comida():
    comida_x = round(random.randrange(0, largura-tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura-tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, cor4, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, cor2, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont('Helvetica', 15)
    texto = fonte.render(f'Pontuação: {pontuacao}', True, cor3)
    tela.blit(texto, [1, 1])

def selecionar_velocidade(tecla):
    
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0    
    return velocidade_x, velocidade_y

def rodar_jogo():
    while True:  # Adicionei um loop para reiniciar o jogo

        fim_jogo = False

        comida_x, comida_y = gerar_comida()
            
        x = largura/2
        y = altura/2

        velocidade_x = 0
        velocidade_y = 0
        
        tamanho_cobra = 1
        pixels_cobra = []

        while not fim_jogo:
            tela.fill(cor1)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    fim_jogo = True
                elif evento.type == pygame.KEYDOWN:
                    velocidade_x, velocidade_y = selecionar_velocidade(evento.key)

            #desenhar comida
            desenhar_comida(tamanho_quadrado, comida_x, comida_y)
            
            #Atualizar posição da cobra
            if x < 0 or x >= largura or y < 0 or y >= altura:
                fim_jogo = True

            x += velocidade_x
            y += velocidade_y

            #desenhar cobra
            pixels_cobra.append([x, y])
            if len(pixels_cobra) > tamanho_cobra:
                del pixels_cobra[0]

            for pixel in pixels_cobra[:-1]:
                if pixel == [x, y]:
                    fim_jogo = True

            desenhar_cobra(tamanho_quadrado, pixels_cobra)
            desenhar_pontuacao(tamanho_cobra - 1)

            #atualização da tela
            pygame.display.update()

            #Desenhando nova comida
            
            if x == comida_x and y == comida_y:
                tamanho_cobra += 1
                comida_x, comida_y = gerar_comida()

            relogio.tick(velocidade_jogo)

        if not menu():  # Se o jogador não quiser tentar novamente, encerra o programa
            break    

rodar_jogo()