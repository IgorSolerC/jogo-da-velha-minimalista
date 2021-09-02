import pygame
import var
import objetos
import random
import copy

def humanoJogando(vezDe, BOT): # Verifica se o jogador atual é humano
    if vezDe == 0 and BOT["JOGADOR1"] == False:
        return True
    elif vezDe == 1 and BOT["JOGADOR2"] == False:
        return True
    return False

# Decide aonde o computador irá jogar
def procurarJogada(jogador, tabuleiro, DIFICULDADE_BOT):
    if jogador == 0:
        pecaAliada = "O"
        pecaInimiga = "X"
    else:
        pecaAliada = "X"
        pecaInimiga = "O"
    
    #procura Vitoria Vertical
    for linha in range(var.quantidadeGrid):
        qntPecasIguais = 0
        indexJogada = -1
        for coluna in range(var.quantidadeGrid):
            if tabuleiro.grid[linha][coluna] == pecaInimiga:
                break
            elif tabuleiro.grid[linha][coluna] == pecaAliada:
                qntPecasIguais += 1
            else:
                indexJogada = (linha, coluna)
        if indexJogada != -1 and qntPecasIguais == var.quantidadeGrid-1:
            return indexJogada
        
    #procura Vitoria Horizontal
    for coluna in range(var.quantidadeGrid):
        qntPecasIguais = 0
        indexJogada = -1
        for linha in range(var.quantidadeGrid):
            if tabuleiro.grid[linha][coluna] == pecaInimiga:
                break
            elif tabuleiro.grid[linha][coluna] == pecaAliada:
                qntPecasIguais += 1
            else:
                indexJogada = (linha, coluna)
        if indexJogada != -1 and qntPecasIguais == var.quantidadeGrid-1:
            return indexJogada
        
    #procura Vitoria Diagonal
    for incrementador in range(1, -2, -2):
        linha = 0
        qntPecasIguais = 0
        indexJogada = -1
        if incrementador == 1:
            coluna = var.quantidadeGrid - 1
        else:
            coluna = 0
            
        while linha < var.quantidadeGrid:
            if tabuleiro.grid[linha][coluna] == pecaInimiga:
                break
            elif tabuleiro.grid[linha][coluna] == pecaAliada:
                qntPecasIguais += 1
            elif tabuleiro.grid[linha][coluna] == 0:
                indexJogada = (linha, coluna)
            if indexJogada != -1 and qntPecasIguais == var.quantidadeGrid-1:
                return indexJogada
            linha += 1
            coluna -= incrementador
            
    #procura Defesas Horizontais
    for linha in range(var.quantidadeGrid):
        qntPecasIguais = 0
        indexJogada = -1
        for coluna in range(var.quantidadeGrid):
            if tabuleiro.grid[linha][coluna] == pecaAliada:
                break
            elif tabuleiro.grid[linha][coluna] == pecaInimiga:
                qntPecasIguais += 1
            else:
                indexJogada = (linha, coluna)
        if indexJogada != -1 and qntPecasIguais == var.quantidadeGrid-1:
            return indexJogada

    #procura Defesas Verticais
    for coluna in range(var.quantidadeGrid):
        qntPecasIguais = 0
        indexJogada = -1
        for linha in range(var.quantidadeGrid):
            if tabuleiro.grid[linha][coluna] == pecaAliada:
                break
            elif tabuleiro.grid[linha][coluna] == pecaInimiga:
                qntPecasIguais += 1
            else:
                indexJogada = (linha, coluna)
        if indexJogada != -1 and qntPecasIguais == var.quantidadeGrid-1:
            return indexJogada

    #procura Defesas Diagonais
    for incrementador in range(1, -2, -2):
        linha = 0
        qntPecasIguais = 0
        indexJogada = -1
        if incrementador == 1:
            coluna = var.quantidadeGrid - 1
        else:
            coluna = 0
            
        while linha < var.quantidadeGrid:
            if tabuleiro.grid[linha][coluna] == pecaAliada:
                break
            elif tabuleiro.grid[linha][coluna] == pecaInimiga:
                qntPecasIguais += 1
            elif tabuleiro.grid[linha][coluna] == 0:
                indexJogada = (linha, coluna)
            if indexJogada != -1 and qntPecasIguais == var.quantidadeGrid-1:
                return indexJogada
            linha += 1
            coluna -= incrementador

    # --------!!!!!Work In Progress Abaixo!!!!!--------
    if DIFICULDADE_BOT == 1:
        #prucura por jogadas que complementem uma jogada anterior
        gridPossiveisJogadas = [[0 for linhas in range(var.quantidadeGrid)] for colunas in range(var.quantidadeGrid)] # Cada posição da matriz mostra a quantidade de jogadas possiveis nessa posição
        gridPossiveisJogadasInimigo = [[0 for linhas in range(var.quantidadeGrid)] for colunas in range(var.quantidadeGrid)]
        for linha in range(var.quantidadeGrid): # Busca Horizontal
            qntPecasIguais = 0
            indexJogada = -1
            gridPossiveisJogadasBackUp = copy.deepcopy(gridPossiveisJogadas)
            indexVazios = []
            for coluna in range(var.quantidadeGrid):
                if tabuleiro.grid[linha][coluna] == pecaInimiga:
                    gridPossiveisJogadas[linha][coluna] = gridPossiveisJogadasBackUp[linha][coluna]
                    break
                elif tabuleiro.grid[linha][coluna] == pecaAliada:
                    qntPecasIguais += 1
                else:
                    indexVazios.append((linha, coluna))
            for index in indexVazios:
                gridPossiveisJogadas[index[0]][index[1]] += qntPecasIguais

        for linha in range(var.quantidadeGrid): # Busca Horizontal Inimigo
            qntPecasIguais = 0
            indexJogada = -1
            gridPossiveisJogadasInimigoBackUp = copy.deepcopy(gridPossiveisJogadasInimigo)
            indexVazios = []
            for coluna in range(var.quantidadeGrid):
                if tabuleiro.grid[linha][coluna] == pecaAliada:
                    gridPossiveisJogadasInimigo[linha][coluna] = gridPossiveisJogadasInimigoBackUp[linha][coluna]
                    break
                elif tabuleiro.grid[linha][coluna] == pecaInimiga:
                    qntPecasIguais += 1
                else:
                    indexVazios.append((linha, coluna))
            for index in indexVazios:
                gridPossiveisJogadasInimigo[index[0]][index[1]] += qntPecasIguais
            
        for coluna in range(var.quantidadeGrid): # Busca Vertical
            qntPecasIguais = 0
            indexJogada = -1
            gridPossiveisJogadasBackUp = copy.deepcopy(gridPossiveisJogadas)
            indexVazios = []
            for linha in range(var.quantidadeGrid):
                if tabuleiro.grid[linha][coluna] == pecaInimiga:
                    gridPossiveisJogadas[linha][coluna] = gridPossiveisJogadasBackUp[linha][coluna]
                    break
                elif tabuleiro.grid[linha][coluna] == pecaAliada:
                    qntPecasIguais += 1
                else:
                    indexVazios.append((linha, coluna))
            for index in indexVazios:
                gridPossiveisJogadas[index[0]][index[1]] += qntPecasIguais

        for coluna in range(var.quantidadeGrid): # Busca Vertical Inimigo
            qntPecasIguais = 0
            indexJogada = -1
            gridPossiveisJogadasInimigoBackUp = copy.deepcopy(gridPossiveisJogadasInimigo)
            indexVazios = []
            for linha in range(var.quantidadeGrid):
                if tabuleiro.grid[linha][coluna] == pecaAliada:
                    gridPossiveisJogadasInimigo[linha][coluna] = gridPossiveisJogadasInimigoBackUp[linha][coluna]
                    break
                elif tabuleiro.grid[linha][coluna] == pecaInimiga:
                    qntPecasIguais += 1
                else:
                        indexVazios.append((linha, coluna))
            for index in indexVazios:
                gridPossiveisJogadasInimigo[index[0]][index[1]] += qntPecasIguais
            
        for incrementador in range(1, -2, -2): # Busca Diagonal
            linha = 0
            qntPecasIguais = 0
            indexJogada = -1
            gridPossiveisJogadasBackUp = copy.deepcopy(gridPossiveisJogadas)
            gridPossiveisJogadasInimigoBackUp = copy.deepcopy(gridPossiveisJogadasInimigo)
            indexVazios = []
            if incrementador == 1:
                coluna = var.quantidadeGrid - 1
            else:
                coluna = 0
            
            while linha < var.quantidadeGrid:
                if tabuleiro.grid[linha][coluna] == pecaInimiga:
                    gridPossiveisJogadas[linha][coluna] = gridPossiveisJogadasBackUp[linha][coluna]
                    break
                elif tabuleiro.grid[linha][coluna] == pecaAliada:
                    qntPecasIguais += 1
                else:
                    indexVazios.append((linha, coluna))
                linha += 1
                coluna -= incrementador
            for index in indexVazios:
                gridPossiveisJogadas[index[0]][index[1]] += qntPecasIguais

        for incrementador in range(1, -2, -2): # Busca Diagonal Inimigo
            linha = 0
            qntPecasIguais = 0
            indexJogada = -1
            gridPossiveisJogadasInimigoBackUp = copy.deepcopy(gridPossiveisJogadasInimigo)
            indexVazios = []
            if incrementador == 1:
                coluna = var.quantidadeGrid - 1
            else:
                coluna = 0
            
            while linha < var.quantidadeGrid:
                if tabuleiro.grid[linha][coluna] == pecaInimiga:
                    gridPossiveisJogadasInimigo[linha][coluna] = gridPossiveisJogadasInimigoBackUp[linha][coluna]
                    break
                elif tabuleiro.grid[linha][coluna] == pecaAliada:
                    qntPecasIguais += 1
                else:
                    indexVazios.append((linha, coluna))
                linha += 1
                coluna -= incrementador
            for index in indexVazios:
                gridPossiveisJogadasInimigo[index[0]][index[1]] += qntPecasIguais    

        """
        print("JOGADA ALIDADO:")
        for i in range(var.quantidadeGrid):
            print(gridPossiveisJogadas[i])
        print("JOGADA INIMIGO:")
        for i in range(var.quantidadeGrid):
            print(gridPossiveisJogadasInimigo[i])
        for index in range(var.quantidadeGrid):
            gridPossiveisJogadasInimigo
        """
        
        melhorJogadaNum = -1  # Jogada no codigo abaixo
        valoresIguais = []
        for linha in range(var.quantidadeGrid):
            for coluna in range(var.quantidadeGrid):
                if gridPossiveisJogadas[linha][coluna] > melhorJogadaNum:
                    melhorJogadaNum = gridPossiveisJogadas[linha][coluna]
                    melhorJogadasIndex = [(linha, coluna)]
                elif gridPossiveisJogadas[linha][coluna] == melhorJogadaNum:
                    melhorJogadasIndex.append((linha, coluna))
                
        if melhorJogadaNum > 0:
            melhorJogadaInimigaNum = -1
            if len(valoresIguais) > 1:
                for linha in range(var.quantidadeGrid):
                    for coluna in range(var.quantidadeGrid):
                         if gridPossiveisJogadasInimigo[linha][coluna] > melhorJogadaInimigaNum:
                            melhorJogadaNum = gridPossiveisJogadas[linha][coluna]
                            melhorJogadaInimigaIndex = (linha, coluna)
                    indexJogada = melhorJogadaInimigaIndex
            else:
                indexJogada = melhorJogadasIndex[0]
            return indexJogada
        # --------!!!!!Work In Progress Acima!!!!!--------
        
    #procura Espações de não comprometidos Horizontais
    for linha in range(var.quantidadeGrid):
        qntPecasIguais = 0
        indexJogada = -1
        for coluna in range(var.quantidadeGrid):
            if tabuleiro.grid[linha][coluna] == pecaInimiga:
                break
            elif tabuleiro.grid[linha][coluna] == 0:
                indexJogada = (linha, coluna)
        if indexJogada != -1 and qntPecasIguais == var.quantidadeGrid-1:
            return indexJogada

    #procura Espações de não comprometidos VERTICAL
    for coluna in range(var.quantidadeGrid):
        qntPecasIguais = 0
        indexJogada = -1
        for linha in range(var.quantidadeGrid):
            if tabuleiro.grid[linha][coluna] == pecaInimiga:
                break
            elif tabuleiro.grid[linha][coluna] == 0:
                indexJogada = (linha, coluna)
        if indexJogada != -1 and qntPecasIguais == var.quantidadeGrid-1:
            return indexJogada

    #procura Espações de não comprometidos DIAGONAL
    for incrementador in range(1, -2, -2):
        linha = 0
        qntPecasIguais = 0
        indexJogada = -1
        if incrementador == 1:
            coluna = var.quantidadeGrid - 1
        else:
            coluna = 0
            
        while linha < var.quantidadeGrid:
            if tabuleiro.grid[linha][coluna] == pecaInimiga:
                break
            elif tabuleiro.grid[linha][coluna] == 0:
                indexJogada = (linha, coluna)
            if indexJogada != -1 and qntPecasIguais == var.quantidadeGrid-1:
                return indexJogada
            linha += 1
            coluna -= incrementador
            
    #procura Posicao Aleatoria
    linhas = list(range(var.quantidadeGrid))
    colunas = list(range(var.quantidadeGrid))
    random.shuffle(linhas)
    random.shuffle(colunas)
    for linha in range(var.quantidadeGrid):
        for coluna in range(var.quantidadeGrid):
            if tabuleiro.grid[linhas[linha]][colunas[coluna]] == 0:
                return (linhas[linha], colunas[coluna])

# Muda a paleta de cores utilizada
def mudarPaletaCores(pecasPreview, pecasEmJogo, tabuleiro, paletaDeCores):
    if paletaDeCores == 0: # PALETA 0 PADRÃO
        corFundo = pygame.Color("#23232d") # CINZA_AZULADO
        corPreviewO = pygame.Color("#646473") # CINZA
        corPecasO = pygame.Color("#c8c8d7") # CINZA_BRANCO
        corPecasX = pygame.Color("#c8c8d7") # CINZA_BRANCO
        corPreviewX = pygame.Color("#646473") # CINZA
        corTabuleiro = pygame.Color("#c8c8d7") # CINZA_BRANCO
        corTabSombra = pygame.Color("#1d1d26") # CINZA_AZULADO_ESCURO
    elif paletaDeCores == 1: # PALETA 1 ESCALDANTE
        corFundo = pygame.Color("#1a0000") # PRETO_VERMELHO
        corPreviewO = pygame.Color("#e2a528") # LARANJA
        corPecasO = pygame.Color("#ff3a32") # VERMELHO
        corPecasX = pygame.Color("#ff3a32") # VERMELHO
        corPreviewX = pygame.Color("#e2a528") # LARANJA
        corTabuleiro = pygame.Color("#e2a528") # LARANJA
        corTabSombra = pygame.Color("#000000") # PRETO
    elif paletaDeCores == 2: # PALETA 2 LABIRINTO
        corFundo = pygame.Color("#1f4437") # VERDE_ESCURO
        corPreviewO = pygame.Color("#3e7a65") # VERDE
        corPecasO = pygame.Color("#d6686f") # VERMELHO_ROSADO
        corPecasX = pygame.Color("#d6686f") # VERMELHO_ROSADO
        corPreviewX = pygame.Color("#3e7a65") # VERDE
        corTabuleiro = pygame.Color("#3e7a65") # VERDE
        corTabSombra = pygame.Color("#1a3d31") # VERDE_ESCURO2
    elif paletaDeCores == 3: # PALETA 3 MC DONALDS
        corFundo = pygame.Color("#ce1226") # VERMELHO2
        corPreviewO = pygame.Color("#fcd116") # AMARELO
        corPecasO = pygame.Color("#ffffff") # BRANCO
        corPecasX = pygame.Color("#ffffff") # BRANCO
        corPreviewX = pygame.Color("#fcd116") # AMARELO
        corTabuleiro = pygame.Color("#fcd116") # AMARELO
        corTabSombra = pygame.Color("#b51223") # VERMELHO_ESCURO
    elif paletaDeCores == 4: # PALETA 4 BENJAMIN
        corFundo = pygame.Color("#001200") # # VERDE_VIVO_ESCURO2
        corPreviewO = pygame.Color("#005500") # VERDE_VIVO_ESCURO
        corPecasO = pygame.Color("#00ee00") # VERDE_VIVO
        corPecasX = pygame.Color("#00ee00") # VERDE_VIVO
        corPreviewX = pygame.Color("#005500") # VERDE_VIVO_ESCURO
        corTabuleiro = pygame.Color("#00ee00") # VERDE_VIVO
        corTabSombra = pygame.Color("#001a00") # # VERDE_VIVO_ESCURO3
    elif paletaDeCores == 5: # PALETA 5 VELOZ
        corFundo = pygame.Color("#46453a") # CINZA_AMARELADO
        corPreviewO = pygame.Color("#46453a") # CINZA_AMARELADO
        corPecasO = pygame.Color("#ffffff") # BRANCO
        corPecasX = pygame.Color("#ffffff") # BRANCO
        corPreviewX = pygame.Color("#46453a") # CINZA_AMARELADO
        corTabuleiro = pygame.Color("#caca00") # AMARELO2
        corTabSombra = pygame.Color("#383730") # CINZA_AMARELADO_ESCURO2
    elif paletaDeCores == 6: # PALETA 6 SAKURA
        corFundo = pygame.Color("#ffffff") # BRANCO
        corPreviewO = pygame.Color("#93e8d3") # VERDE_AGUA
        corPecasO = pygame.Color("#f5b1cc") # ROSA_CLARO
        corPecasX = pygame.Color("#f5b1cc") # ROSA_CLARO
        corPreviewX = pygame.Color("#93e8d3") # VERDE_AGUA
        corTabuleiro = pygame.Color("#93e8d3") # VERDE_AGUA
        corTabSombra = pygame.Color("#e4fff9") # BRANCO_VERDE
    elif paletaDeCores == 7: # PALETA 7 JAVA SCRIPT
        corFundo = pygame.Color("#272727") # CINZA4
        corPreviewO = pygame.Color("#383838") # CINZA2
        corPecasO = pygame.Color("#097bd8") # AZUL_PASTEL
        corPecasX = pygame.Color("#499251") # VERDE_PASTEL
        corPreviewX = pygame.Color("#383838") # CINZA2
        corTabuleiro = pygame.Color("#e89011") # LARANJA_PASTEL
        corTabSombra = pygame.Color("#1f1f1f") # CINZA3
    elif paletaDeCores == 8: # PALETA 8 CONTRASTE
        corFundo = pygame.Color("#ffffff") # BRANCO
        corPreviewO = pygame.Color("#aaaaaa") # CINZA8
        corPecasO = pygame.Color("#000000") # PRETO
        corPecasX = pygame.Color("#000000") # PRETO
        corPreviewX = pygame.Color("#aaaaaa") # CINZA8
        corTabuleiro = pygame.Color("#000000") # PRETO
        corTabSombra = pygame.Color("#eeeeee") # BRANCO_ESCURO
    elif paletaDeCores == 9: # PALETA 9 CHEIRO DE CHUVA
        corFundo = pygame.Color("#634332") # MARROM_CLARO
        corPreviewO = pygame.Color("#9e6749") # MARROM_MAIS_CLARO
        corPecasO = pygame.Color("#7ec160") # VERDE_FOLHA
        corPecasX = pygame.Color("#7ec160") # VERDE_FOLHA
        corPreviewX = pygame.Color("#9e6749") # MARROM_MAIS_CLARO
        corTabuleiro = pygame.Color("#9e6749") # MARROM_MAIS_CLARO
        corTabSombra = pygame.Color("#523525") # MARROM
    elif paletaDeCores == 10: # PALETA 10 PURPLE PARADISE
        corFundo = pygame.Color("#171530") # ROXO_AZULADO
        corPreviewO = pygame.Color("#eedaea") # BRANCO_ROSADO
        corPecasO = pygame.Color("#cf6bdd") # ROXO
        corPecasX = pygame.Color("#cf6bdd") # ROXO
        corPreviewX = pygame.Color("#eedaea") # BRANCO_ROSADO
        corTabuleiro = pygame.Color("#eedaea") # BRANCO_ROSADO
        corTabSombra = pygame.Color("#121426") # ROXO_AZULADO_ESCURO
    elif paletaDeCores == 11: # PALETA 11 PRAGA
        corFundo = pygame.Color("#070707") # CINZA5
        corPreviewO = pygame.Color("#460f4d") # ROXO_ESCURO2
        corPecasO = pygame.Color("#cf6bdd") # ROXO
        corPecasX = pygame.Color("#84ff00") # VERDE_LIMAO
        corPreviewX = pygame.Color("#2d4a0e") # VERDE_LIMAO_ESCURO
        corTabuleiro = pygame.Color("#ffffff") # BRANCO
        corTabSombra = pygame.Color("#000000") # PRETO
    elif paletaDeCores == 12: # PALETA 12 CHICLETE
        corFundo = pygame.Color("#f35588") # ROSA_CHICLETE
        corPreviewO = pygame.Color("#ff78a3") # ROSA_CHICLETE_CLARO
        corPecasO = pygame.Color("#00fff6") # CIANO
        corPecasX = pygame.Color("#00fff6") # CIANO
        corPreviewX = pygame.Color("#ff78a3") # ROSA_CHICLETE_CLARO
        corTabuleiro = pygame.Color("#ffffff") # BRANCO
        corTabSombra = pygame.Color("#e45785") # ROSA_CHICLETE_ESCURO
    elif paletaDeCores == 13: # PALETA 13 GRAVATA
        corFundo = pygame.Color("#23232d") # CINZA_AZULADO
        corPreviewO = pygame.Color("#646473") # CINZA
        corPecasO = pygame.Color("#ffffff") # BRANCO
        corPecasX = pygame.Color("#ffffff") # BRANCO
        corPreviewX = pygame.Color("#646473") # CINZA
        corTabuleiro = pygame.Color("#f35588") # ROSA_CHICLETE
        corTabSombra = pygame.Color("#1d1d26") # CINZA_AZULADO_ESCURO
    elif paletaDeCores == 14: # PALETA 14 CAFÉ
        corFundo = pygame.Color("#ceb18d") # BEGE_CAFE
        corPreviewO = pygame.Color("#ffffff") # BRANCO
        corPecasO = pygame.Color("#6d5d49") # MARROM_CAFE
        corPecasX = pygame.Color("#6d5d49") # MARROM_CAFE
        corPreviewX = pygame.Color("#ffffff") # BRANCO
        corTabuleiro = pygame.Color("#a99174") # BEGE_CAFE_ESCURO2
        corTabSombra = pygame.Color("#bfa583") # BEGE_CAFE_ESCURO
    elif paletaDeCores == 15: # PALETA 15 AZEITE
        corFundo = pygame.Color("#faf1e4") 
        corPreviewO = pygame.Color("#3c403b") 
        corPecasO = pygame.Color("#618c56") 
        corPecasX = pygame.Color("#618c56") 
        corPreviewX = pygame.Color("#3c403b") 
        corTabuleiro = pygame.Color("#c2b8aa") 
        corTabSombra = pygame.Color("#efe6da") 
    elif paletaDeCores == 16: # PALETA 16 CHÃO DO OCEANO
        corFundo = pygame.Color("#1a2b3e") # AZUL_MARINHO
        corPreviewO = pygame.Color("#635238") # BEGE_ESCURO
        corPecasO = pygame.Color("#af8f5c") # BEGE
        corPecasX = pygame.Color("#af8f5c") # BEGE
        corPreviewX = pygame.Color("#635238") # BEGE_ESCURO
        corTabuleiro = pygame.Color("#c8c8d7") # CINZA_BRANCO
        corTabSombra = pygame.Color("#141f2b") # AZUL_MARINHO_ESCURO
    elif paletaDeCores == 17: # PALETA 17 EMERGENCIA
        corFundo = pygame.Color("#111111") # CINZA_AZULADO
        corPreviewO = pygame.Color("#646473") # CINZA
        corPecasO = pygame.Color("#00bb00") # VERDE_VIVO2
        corPecasX = pygame.Color("#bb0000") # VERMELHO_VIVO
        corPreviewX = pygame.Color("#646473") # CINZA
        corTabuleiro = pygame.Color("#888888") # CINZA_BRANCO
        corTabSombra = pygame.Color("#090909") # CINZA_AZULADO_ESCURO

    if var.semSombra:
        corTabSombra = corFundo
    
    mudarCores(pecasPreview, pecasEmJogo, tabuleiro, corPreviewO, corPecasO, corTabuleiro, corTabSombra, corPecasX, corPreviewX)
    
    return (corPreviewO, corPecasO, corTabuleiro, corFundo, corTabSombra, corPecasX, corPreviewX)

# Muda as cores de cada objeto do jogo
def mudarCores(pecasPreview, pecasEmJogo, tabuleiro, corPreviewO, corPecasO, corTabuleiro, corTabSombra, corPecasX, corPreviewX):

    for peca in pecasPreview:
        if type(peca) == objetos.PecaCirculo:
            peca.cor = corPecasO
            peca.corPreview = corPreviewO
        elif type(peca) == objetos.PecaXis:
            peca.cor = corPecasX
            peca.corPreview = corPreviewX
        peca.corSombra = corTabSombra
    for peca in pecasEmJogo:
        if type(peca) == objetos.PecaCirculo:
            peca.cor = corPecasO
            peca.corPreview = corPreviewO
        elif type(peca) == objetos.PecaXis:
            peca.cor = corPecasX
            peca.corPreview = corPreviewX
        peca.corSombra = corTabSombra

    tabuleiro.cor = corTabuleiro
    tabuleiro.corSombra = corTabSombra
