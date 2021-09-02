import pygame
import var
import func
import objetos
from random import randint

# Inicia a engine
pygame.init()

# Constantes
FRAMES_POR_SEGUNDO = 60 # 60

# Variaveis
BOT = {"JOGADOR1": False,
       "JOGADOR2": True}
contadorJogadaBot = 0
contadorJogadaBotMax = 30 # Normal = 30

# Estados de Fim de Jogo
NINGUEM = -1
JOGADOR1 = 0
JOGADOR2 = 1
VELHA = 2

velhas = 0
vitoriasO = 0
vitoriasX = 0
interfaceGrafica = True

mouseOverRect = 0
jogadorJogou = False

vezDe = JOGADOR1
jogadas = 0
tempoReset = 0

pecasPreview = []
pecasEmJogo = []

tabuleiro = objetos.Tabuleiro()
TOTAL_CORES = 17

# Update paleta de cores
paletaDeCores = randint(0, TOTAL_CORES)
cores = func.mudarPaletaCores(pecasPreview, pecasEmJogo, tabuleiro, paletaDeCores)
corPreviewO = cores[0]
corPecasO = cores[1]
corTabuleiro = cores[2]
corFundo = cores[3]
corTabSombra = cores[4]
corPecasX = cores[5]
corPreviewX = cores[6]

coresAleatorias = True

# Titulo da janela
pygame.display.set_caption("Tic Tac Toe") # Titulo da janela

# ---------- MAIN LOOP ---------- 
jogoRodando = True
clock = pygame.time.Clock() # Framerate (Velocidade que a tela da update)

while jogoRodando:
    # --------- MAIN EVENT (O usuario entrou algum input?)
    for evento in pygame.event.get(): # User entrou um input
        if evento.type == pygame.QUIT: # Se o jogador fechou o jogo
            jogoRodando = False
        if evento.type == pygame.MOUSEMOTION:
            # Ve se o mouse está em cima de algum grid
            for coluna in range(len(tabuleiro.rects)):
                for linha in range(len(tabuleiro.rects)):
                    grid = tabuleiro.rects[linha][coluna]
                    gridDentro = tabuleiro.grid[linha][coluna]
                    if grid.collidepoint(pygame.mouse.get_pos()):
                        break
                    else:
                        mouseOverRect = 0
                if grid.collidepoint(pygame.mouse.get_pos()):
                    mouseOverRect = grid
                    mouseOverRectLinha = linha
                    mouseOverRectColuna = coluna
                    break
        if evento.type == pygame.MOUSEBUTTONDOWN: # Jogador apertou botão do mouse
            mouseBotEsquerdo = pygame.mouse.get_pressed()[0] # Update estado BEM
            if mouseOverRect != 0:
                mouseOverRectSave = mouseOverRect
            mouseBotMeio = pygame.mouse.get_pressed()[1] # Update estado BMM
            mouseBotDireito = pygame.mouse.get_pressed()[2] # Update estado BDM
            
        if evento.type == pygame.MOUSEBUTTONUP: # Jogador soltou botão do mouse
            if mouseBotEsquerdo and mouseOverRect == mouseOverRectSave and func.humanoJogando(vezDe, BOT) and var.vitoria == NINGUEM and gridDentro == 0: 
                # A ação só acontece se:
                # O mouse esquerdo foi pressionado
                # O mouse está em cim uma do mesmo retangulo que ele estava quando clicou
                # Este não é o turno do Computador
                # Ninguem ganhou a partida atual
                jogadorJogou = True
            mouseBotEsquerdo = pygame.mouse.get_pressed()[0] # Update estado BEM

        if evento.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_1]:
                if paletaDeCores < TOTAL_CORES:
                    paletaDeCores += 1
                else:
                    paletaDeCores = 0
                # Update paleta de cores
                cores = func.mudarPaletaCores(pecasPreview, pecasEmJogo, tabuleiro, paletaDeCores)
                corPreviewO = cores[0]
                corPecasO = cores[1]
                corTabuleiro = cores[2]
                corFundo = cores[3]
                corTabSombra = cores[4]
                corPecasX = cores[5]
                corPreviewX = cores[6]
            if pygame.key.get_pressed()[pygame.K_2]:
                if var.semSombra:
                    var.semSombra = False
                else:
                    var.semSombra = True
                # Update paleta de cores
                cores = func.mudarPaletaCores(pecasPreview, pecasEmJogo, tabuleiro, paletaDeCores)
                corPreviewO = cores[0]
                corPecasO = cores[1]
                corTabuleiro = cores[2]
                corFundo = cores[3]
                corTabSombra = cores[4]
                corPecasX = cores[5]
                corPreviewX = cores[6]

    
    # --------- GAME LOGIC (O que ocorre entre frames)
    for peca in pecasPreview: # Animação Preview Das peças
        if peca.emAnimacaoPreview and ((jogadorJogou == True and peca.grid != mouseOverRect) or jogadorJogou == False):
            peca.animacaoPreview() # update Animação Preview
        else:
            pecasPreview.remove(peca) # Remove Preview

    for peca in pecasEmJogo: # Animação entrada Peças
        if peca.emAnimacaoJogar:
            peca.animacaoJogar() # update Animação Jogar
    if tabuleiro.emAnimacaoMarcador:
        tabuleiro.animacaoMarcadorVitoria() # update Animação Marcador
    
    if var.vitoria != NINGUEM:
        if tempoReset > 60: # 60

            # TESTES
            if var.vitoria == JOGADOR1:
                vitoriasO += 1
            elif var.vitoria == JOGADOR2:
                vitoriasX += 1
            else:
                velhas += 1
            if velhas + vitoriasO + vitoriasX == 10000:
                print("Velhas: ", velhas)
                print("Vitorias O: ", vitoriasO)
                print("Vitorias X: ", vitoriasX)
                while True:
                    
                    pass

            """ # O = NOVA IA        X = ANTIGA IA
            1
            Velhas:  3891
            Vitorias O:  3139
            Vitorias X:  2970
            """
            """ # O = ANTIGA IA        X = ANTIGA IA
            1
            Velhas:  5118
            Vitorias O:  2438
            Vitorias X:  2444
            2
            Velhas:  5128
            Vitorias O:  2383
            Vitorias X:  2489
            """
            """ # O = NOVA IA        X = NOVA IA
            1
            Velhas:  3345
            Vitorias O:  3327
            Vitorias X:  3328
            2
            Velhas:  3313
            Vitorias O:  3332
            Vitorias X:  3355
            """
            
            if coresAleatorias:
                var.quantidadeGrid = randint(3, 3)
                paletaDeCores = randint(0, TOTAL_CORES)
            tempoReset = 0
            var.vitoria = NINGUEM
            jogadas = 0
            pecasPreview = []
            pecasEmJogo = []
            tabuleiro = objetos.Tabuleiro()

            # Update paleta de cores
            cores = func.mudarPaletaCores(pecasPreview, pecasEmJogo, tabuleiro, paletaDeCores)
            corPreviewO = cores[0]
            corPecasO = cores[1]
            corTabuleiro = cores[2]
            corFundo = cores[3]
            corTabSombra = cores[4]
            corPecasX = cores[5]
            corPreviewX = cores[6]
        else:
            tempoReset += 1
    else:     
        if func.humanoJogando(vezDe, BOT): # Verifica se é vez de um humano ou computador
            if mouseOverRect != 0:
                # Verifica se já há um preview no local
                naoPossuiPreview = True
                for peca in pecasPreview:
                    if peca.grid == mouseOverRect:
                        naoPossuiPreview = False
                        peca.contadorAnimacaoPreview = 0
                        break
            
                # Verifica se já há uma peça no local
                naoPossuiPeca = True
                for peca in pecasEmJogo:
                    if peca.grid == mouseOverRect:
                        naoPossuiPeca = False
                        break
            
                if vezDe == JOGADOR1 and naoPossuiPreview and naoPossuiPeca: # Coloca preview quando em local valido
                    pecasPreview.append(objetos.PecaCirculo(mouseOverRect, True, corPreviewO, corPecasO, corTabSombra)) # Coloca o preview circulo
                elif vezDe == JOGADOR2 and naoPossuiPreview and naoPossuiPeca:
                    pecasPreview.append(objetos.PecaXis(mouseOverRect, True, corPreviewX, corPecasX, corTabSombra)) # Coloca o preview X
            
                if jogadorJogou and naoPossuiPeca: # Joga peça quando em local valido
                    jogadorJogou = False
                    pecasPreview = []
                    jogadas += 1
                    if vezDe == JOGADOR1:
                        pecasEmJogo.append(objetos.PecaCirculo(mouseOverRect, False, corPreviewO, corPecasO, corTabSombra)) # Coloca a Peça Circulo
                        tabuleiro.grid[mouseOverRectLinha][mouseOverRectColuna] = "O"
                        vezDe = JOGADOR2 # Muda o turno
                        tabuleiro.checkVitoria(jogadas) # Checa se alguem canhou
                    elif vezDe == JOGADOR2:
                        pecasEmJogo.append(objetos.PecaXis(mouseOverRect, False, corPreviewX, corPecasX, corTabSombra)) # Coloca a Peça X
                        tabuleiro.grid[mouseOverRectLinha][mouseOverRectColuna] = "X"
                        vezDe = JOGADOR1 # Muda o turno
                        tabuleiro.checkVitoria(jogadas) # Checa se alguem canhou
                    """
                    print("EU:")
                    for i in range(var.quantidadeGrid):
                        print(tabuleiro.grid[i])
                    """
        elif jogadas < var.quantidadeGrid**2:
            if contadorJogadaBot > contadorJogadaBotMax: 
                contadorJogadaBot = 0
                jogadas += 1
                if vezDe == JOGADOR1:
                    jogadaBot = func.procurarJogada(vezDe, tabuleiro, 0)
                    pecasEmJogo.append(objetos.PecaCirculo(tabuleiro.rects[jogadaBot[0]][jogadaBot[1]], False, corPreviewO, corPecasO, corTabSombra))
                    tabuleiro.grid[jogadaBot[0]][jogadaBot[1]] = "O"
                    vezDe = JOGADOR2 # Muda o turno
                    tabuleiro.checkVitoria(jogadas) # Checa se alguem canhou
            
                elif vezDe == JOGADOR2:
                    jogadaBot = func.procurarJogada(vezDe, tabuleiro, 0)
                    pecasEmJogo.append(objetos.PecaXis(tabuleiro.rects[jogadaBot[0]][jogadaBot[1]], False, corPreviewX, corPecasX, corTabSombra))
                    tabuleiro.grid[jogadaBot[0]][jogadaBot[1]] = "X"
                    vezDe = JOGADOR1 # Muda o turno
                    tabuleiro.checkVitoria(jogadas) # Checa se alguem canhou
                """
                print("BOT:")
                for i in range(var.quantidadeGrid):
                    print(tabuleiro.grid[i])
                """
            else:
                contadorJogadaBot += 1
    
    # --------- DRAWING CODE (Update da tela)
    if interfaceGrafica:
        var.TELA.fill(corFundo) # Pinta o fundo

        tabuleiro.draw()

        for peca in pecasPreview:
            if peca.emAnimacaoPreview:
                peca.animacaoPreviewDraw()

        for peca in pecasEmJogo:           
            peca.draw()

        if var.vitoria == JOGADOR1 or var.vitoria == JOGADOR2:
            tabuleiro.drawMarcadorVitoria()
    
    # --------- UPDATE SCREEN
    pygame.display.flip()
    
    # --------- FRAME RATE
    clock.tick(FRAMES_POR_SEGUNDO)

# Para a engine quando o jogo para
pygame.quit()
