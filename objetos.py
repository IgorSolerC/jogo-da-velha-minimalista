import pygame
import var

class Tabuleiro():
    def __init__(self, ):
        if var.TAMANHO_TELA[0] < var.TAMANHO_TELA[1]:
            indexTela = 0
        else:
            indexTela = 1
        self.grid = self.definirGrid(var.quantidadeGrid)
        self.tamanhoGrid = int(var.TAMANHO_TELA[indexTela]/len(self.grid)*0.9)
        self.gapBordasX = (var.TAMANHO_TELA[0] - self.tamanhoGrid*len(self.grid))/2 # Distancia entre tabuleiro e bordas da janela
        self.gapBordasY = (var.TAMANHO_TELA[1] - self.tamanhoGrid*len(self.grid))/2 # Distancia entre tabuleiro e bordas da janela
        self.rects = self.definirRect()
        self.pontosSombra = self.definirPontosSombra()
        self.grossuraBordas = 4 #4

        self.porcentTamanhoContador = 0
        self.velAnimacaoMarcador = 0.4
        self.emAnimacaoMarcador = False

    def definirGrid(self, tamanho):
        matriz = [[0 for linhas in range(tamanho)] for colunas in range(tamanho)] 
        return matriz
    
    def definirRect(self):
        rects = self.definirGrid(var.quantidadeGrid)
        for linha in range(len(self.grid)):
            for coluna in range(len(self.grid[linha])):
                x = coluna*self.tamanhoGrid + self.gapBordasX
                y = linha*self.tamanhoGrid + self.gapBordasY
                rects[linha][coluna] = pygame.Rect((x, y), (self.tamanhoGrid, self.tamanhoGrid))
        return rects

    def definirPontosSombra(self):
        pontos = []
        
        # VERTICAL
        y = self.tamanhoGrid
        for i in range(len(self.grid)*2-2, 0, -1): # Pontos Cima
            if i % 2 == 0:
                y = self.tamanhoGrid*(i/2)
                y += self.gapBordasY
                
            x = self.gapBordasX+(self.tamanhoGrid*((i)%2))
            pontos.append([x, y])
        # HORIZONTAL
        x = self.tamanhoGrid + self.gapBordasX
        for i in range(0, len(self.grid)*2-2, 1): # Pontos Cima
            if i % 2 == 0:
                x = self.tamanhoGrid*((i+2)/2)
                x += self.gapBordasX
                
            y = self.gapBordasY+(self.tamanhoGrid*((i-1)%2))
            pontos.append([x, y])

        # DIAGONAL
        multiplicador = 0
        while True: # Determina ponto Direita
            limiteTela = self.tamanhoGrid * multiplicador
            if pontos[-1][0] + limiteTela >= var.TAMANHO_TELA[0] or pontos[-1][1] + limiteTela >= var.TAMANHO_TELA[1]:
                pontoDireita = [pontos[-1][0] + limiteTela, pontos[-1][1] + limiteTela]
                break
            multiplicador += 1
        multiplicador = 0
        while True: # Determina ponto Baixo
            limiteTela = self.tamanhoGrid * multiplicador
            if pontos[0][0] + limiteTela >= var.TAMANHO_TELA[0] or pontos[0][1] + limiteTela >= var.TAMANHO_TELA[1]:
                pontoBaixo = [pontos[0][0] + limiteTela, pontos[0][1] + limiteTela]
                break
            multiplicador += 1
        
        pontoMeio = var.TAMANHO_TELA
        pontos.append(pontoDireita)
        pontos.append(pontoMeio)
        pontos.append(pontoBaixo)
        
        return pontos

    def draw(self):
        JOGADOR1 = 0
        JOGADOR2 = 1
        
        self.drawSombra()
        for linhas in range(1, len(self.grid), 1):  
            pygame.draw.line(var.TELA, self.cor, (self.tamanhoGrid*linhas+self.gapBordasX, self.gapBordasY), (self.tamanhoGrid*linhas+self.gapBordasX, self.gapBordasY + self.tamanhoGrid*len(self.grid)), self.grossuraBordas)
            pygame.draw.line(var.TELA, self.cor, (self.gapBordasX, self.tamanhoGrid*linhas+self.gapBordasY), (self.gapBordasX + self.tamanhoGrid*len(self.grid), self.tamanhoGrid*linhas+self.gapBordasY), self.grossuraBordas)
        
        #self.drawHitbox()

    def drawHitbox(self):
        for linha in range(len(self.rects)):
            for coluna in range(len(self.rects[linha])):
                pygame.draw.rect(var.TELA, var.PRETO, self.rects[linha][coluna], 4) # HIT BOX

    def drawSombra(self):
        if var.quantidadeGrid > 1:
            pygame.draw.polygon(var.TELA, self.corSombra, self.pontosSombra) # Desenha combra

    def checkVitoria(self, jogadas):
        JOGADOR1 = 0
        JOGADOR2 = 1
        VELHA = 2
        HORIZONTAL = 0
        VERTICAL = 1
        DIAGONAL = 2
        self.orientacoesVitoria = []
        self.indexVitoria = []
        
        for linha in range(var.quantidadeGrid): # Check vitorias Verticais
            qntPecasO = 0
            qntPecasX = 0
            for coluna in range(var.quantidadeGrid) or (qntPecasO > 0 and qntPecasX > 0):
                if self.grid[linha][coluna] == "O":
                    qntPecasO += 1
                if self.grid[linha][coluna] == "X":
                    qntPecasX += 1
                if qntPecasO == var.quantidadeGrid:
                    var.vitoria = JOGADOR1
                    self.orientacoesVitoria.append(VERTICAL)
                    self.indexVitoria.append(linha)
                elif qntPecasX == var.quantidadeGrid:
                    var.vitoria = JOGADOR2
                    self.orientacoesVitoria.append(VERTICAL)
                    self.indexVitoria.append(linha)

        for coluna in range(var.quantidadeGrid): # Check vitorias Horizontais
            qntPecasO = 0
            qntPecasX = 0
            for linha in range(var.quantidadeGrid) or (qntPecasO > 0 and qntPecasX > 0):
                if self.grid[linha][coluna] == "O":
                    qntPecasO += 1
                if self.grid[linha][coluna] == "X":
                    qntPecasX += 1
                if qntPecasO == var.quantidadeGrid:
                    var.vitoria = JOGADOR1
                    self.orientacoesVitoria.append(HORIZONTAL)
                    self.indexVitoria.append(coluna)
                elif qntPecasX == var.quantidadeGrid:
                    var.vitoria = JOGADOR2
                    self.orientacoesVitoria.append(HORIZONTAL)
                    self.indexVitoria.append(coluna)

                
        for incrementador in range(1, -2, -2): # Check vitorias Verticais Diagonal
            linha = 0
            qntPecasO = 0
            qntPecasX = 0
            if incrementador == 1:
                coluna = var.quantidadeGrid - 1
            else:
                coluna = 0
            
            while linha < var.quantidadeGrid:
                if self.grid[linha][coluna] == "O":
                    qntPecasO += 1
                if self.grid[linha][coluna] == "X":
                    qntPecasX += 1
                if qntPecasO == var.quantidadeGrid:
                    var.vitoria = JOGADOR1
                    self.orientacoesVitoria.append(DIAGONAL)
                    self.indexVitoria.append(incrementador)
                elif qntPecasX == var.quantidadeGrid:
                    var.vitoria = JOGADOR2
                    self.orientacoesVitoria.append(DIAGONAL)
                    self.indexVitoria.append(incrementador)
                linha += 1
                coluna -= incrementador

        if var.vitoria == -1 and jogadas == var.quantidadeGrid**2:
            var.vitoria = VELHA

    def animacaoMarcadorVitoria(self):
        if self.porcentTamanhoContador < 1:
            self.velAnimacaoMarcador -= self.velAnimacaoMarcador*.1
            self.porcentTamanhoContador += self.velAnimacaoMarcador
        elif self.porcentTamanhoContador > 1:
            self.porcentTamanhoContador = 1
            self.velAnimacaoMarcador = 0.1
            
    def drawMarcadorVitoria(self):
        NINGUEM = -1
        JOGADOR1 = 0
        JOGADOR2 = 1
        VELHA = 2
        
        HORIZONTAL = 0
        VERTICAL = 1
        DIAGONAL = 2

        CENTRO_X = var.TAMANHO_TELA[0]/2
        CENTRO_Y = var.TAMANHO_TELA[1]/2
        DIST_CENTRO_BORDA = (self.tamanhoGrid*var.quantidadeGrid/2)*self.porcentTamanhoContador

        if var.vitoria == JOGADOR1 or var.vitoria == JOGADOR2:
            self.emAnimacaoMarcador = True
            for i in range(len(self.orientacoesVitoria)):
                if self.orientacoesVitoria[i] == HORIZONTAL:
                    pygame.draw.line(var.TELA, self.cor, (self.tamanhoGrid/2+self.tamanhoGrid*self.indexVitoria[i]+self.gapBordasX, CENTRO_Y-DIST_CENTRO_BORDA), (self.tamanhoGrid/2+self.tamanhoGrid*self.indexVitoria[i]+self.gapBordasX, CENTRO_Y+DIST_CENTRO_BORDA), self.grossuraBordas)
                elif self.orientacoesVitoria[i] == VERTICAL:
                    pygame.draw.line(var.TELA, self.cor, (CENTRO_X-DIST_CENTRO_BORDA, self.tamanhoGrid/2+self.tamanhoGrid*self.indexVitoria[i]+self.gapBordasY), (CENTRO_X+DIST_CENTRO_BORDA, self.tamanhoGrid/2+self.tamanhoGrid*self.indexVitoria[i]+self.gapBordasY), self.grossuraBordas)
                else:
                    if self.indexVitoria[i] == -1:
                        pygame.draw.line(var.TELA, self.cor, (CENTRO_X-DIST_CENTRO_BORDA, CENTRO_Y-DIST_CENTRO_BORDA), (CENTRO_X+DIST_CENTRO_BORDA, CENTRO_Y+DIST_CENTRO_BORDA), round(self.grossuraBordas*1.5))
                    else:
                        pygame.draw.line(var.TELA, self.cor, (CENTRO_X-DIST_CENTRO_BORDA, CENTRO_Y+DIST_CENTRO_BORDA), (CENTRO_X+DIST_CENTRO_BORDA, CENTRO_Y-DIST_CENTRO_BORDA), round(self.grossuraBordas*1.5))

# ---------------------------------------------------------------------------------------------------

class PecaCirculo():
    def __init__(self, grid, preview, corPreview, corPecas, corSombra):
        self.grid = grid
        self.cor = corPecas # CORES CIRCULO ----------------------
        self.corPreview = corPreview # CORES XIS PREVIEW ----------------------
        self.corSombra = corSombra
        self.definirTamanho()
        self.grossuraBordas = 4 #4
        
        # Animação Preview
        self.contadorAnimacaoPreview = 0
        self.contadorAnimacaoMaxPreview = 3
        self.velAnimacaoPreview = self.grid.width/40
        self.emAnimacaoPreview = preview
        self.animacaoPreview()

        # Animação Jogar
        self.emAnimacaoJogar = not preview
        
    def definirTamanho(self):
        gridX = self.grid.left
        gridY = self.grid.top
        gridTamanho = self.grid.width
        self.gridCentro = (gridX+gridTamanho/2, gridY+gridTamanho/2)
        self.tamanhoMax = round(gridTamanho/3.5)
        self.tamanho = 0

    def animacaoPreview(self):
        if self.contadorAnimacaoPreview < self.contadorAnimacaoMaxPreview:
            if self.tamanho < self.tamanhoMax:
                if self.velAnimacaoPreview > 5:
                    self.velAnimacaoPreview -= self.velAnimacaoPreview*.3
                self.tamanho += self.velAnimacaoPreview
            elif self.tamanho > self.tamanhoMax:
                self.tamanho = self.tamanhoMax
                self.velAnimacaoPreview = self.grid.width/40
        else:
            if self.tamanho > 0:
                if self.velAnimacaoPreview > 5:
                    self.velAnimacaoPreview -= self.velAnimacaoPreview*.3
                self.tamanho -= self.velAnimacaoPreview
            elif self.tamanho <= 0:
                self.tamanho = 0
                self.emAnimacaoPreview = False # Termina animação caso o contador chegue ao maximo
        self.contadorAnimacaoPreview += 1 # Incrementa contador animação

    def animacaoPreviewDraw(self):
        self.drawSombra()
        pygame.draw.circle(var.TELA, self.corPreview, self.gridCentro, self.tamanho, self.grossuraBordas)

    def animacaoJogar(self):
        if self.tamanho < self.tamanhoMax:
            if self.velAnimacaoPreview > 5:
                self.velAnimacaoPreview -= self.velAnimacaoPreview*.3
            self.tamanho += self.velAnimacaoPreview
        elif self.tamanho > self.tamanhoMax:
            self.tamanho = self.tamanhoMax
            self.velAnimacaoPreview = self.grid.width/40

    def draw(self):
        self.drawSombra()
        pygame.draw.circle(var.TELA, self.cor, self.gridCentro, self.tamanho, self.grossuraBordas) # Circulo

    def drawSombra(self):
        for distSombra in range(8, 80, 1):
            pygame.draw.circle(var.TELA, self.corSombra, (self.gridCentro[0]+(self.tamanho/distSombra), self.gridCentro[1]+(self.tamanho/distSombra)), self.tamanho, self.grossuraBordas) # Sombra

# ---------------------------------------------------------------------------------------------------

class PecaXis():
    def __init__(self, grid, preview, corPreview, corPecas, corSombra):
        self.grid = grid
        self.cor = corPecas
        self.corPreview = corPreview
        self.corSombra = corSombra
        self.definirTamanho()
        self.grossuraBordas = 5
        
        # Animação Preview
        self.contadorAnimacaoPreview = 0
        self.contadorAnimacaoMaxPreview = 3
        self.velAnimacaoPreview = self.grid.width/40
        self.emAnimacaoPreview = preview
        self.animacaoPreview()

        # Animação Jogar
        self.emAnimacaoJogar = not preview
        
    def definirTamanho(self):
        gridX = self.grid.left
        gridY = self.grid.top
        gridTamanho = self.grid.width
        self.gridCentro = (gridX+gridTamanho/2, gridY+gridTamanho/2)
        self.tamanhoMax = (gridTamanho/4)
        self.tamanho = 0

    def animacaoPreview(self):
        if self.contadorAnimacaoPreview < self.contadorAnimacaoMaxPreview:
            if self.tamanho < self.tamanhoMax:
                if self.velAnimacaoPreview > 5:
                    self.velAnimacaoPreview -= self.velAnimacaoPreview*.3
                self.tamanho += self.velAnimacaoPreview
            elif self.tamanho > self.tamanhoMax:
                self.tamanho = self.tamanhoMax
                self.velAnimacaoPreview = self.grid.width/40
        else:
            if self.tamanho > 0:
                if self.velAnimacaoPreview > 5:
                    self.velAnimacaoPreview -= self.velAnimacaoPreview*.3
                self.tamanho -= self.velAnimacaoPreview
            elif self.tamanho <= 0:
                self.tamanho = 0
                self.emAnimacaoPreview = False # Termina animação caso o contador chegue ao maximo
        self.contadorAnimacaoPreview += 1 # Incrementa contador animação

    def animacaoPreviewDraw(self):
        self.drawSombra()
        pygame.draw.line(var.TELA, self.corPreview, (self.gridCentro[0]+self.tamanho, self.gridCentro[1]+self.tamanho), (self.gridCentro[0]-self.tamanho, self.gridCentro[1]-self.tamanho), self.grossuraBordas)
        pygame.draw.line(var.TELA, self.corPreview, (self.gridCentro[0]-self.tamanho, self.gridCentro[1]+self.tamanho), (self.gridCentro[0]+self.tamanho, self.gridCentro[1]-self.tamanho), self.grossuraBordas)

    def animacaoJogar(self):
        if self.tamanho < self.tamanhoMax:
            if self.velAnimacaoPreview > 5:
                self.velAnimacaoPreview -= self.velAnimacaoPreview*.3
            self.tamanho += self.velAnimacaoPreview
        elif self.tamanho > self.tamanhoMax:
            self.tamanho = self.tamanhoMax
            self.velAnimacaoPreview = self.grid.width/40

    def draw(self):
        self.drawSombra()
        pygame.draw.line(var.TELA, self.cor, (self.gridCentro[0]+self.tamanho, self.gridCentro[1]+self.tamanho), (self.gridCentro[0]-self.tamanho, self.gridCentro[1]-self.tamanho), self.grossuraBordas)
        pygame.draw.line(var.TELA, self.cor, (self.gridCentro[0]-self.tamanho, self.gridCentro[1]+self.tamanho), (self.gridCentro[0]+self.tamanho, self.gridCentro[1]-self.tamanho), self.grossuraBordas)

    def drawSombra(self):
        for distSombra in range(8, 70, 1):
            pygame.draw.line(var.TELA, self.corSombra, (self.gridCentro[0]+self.tamanho+(self.tamanho/distSombra), self.gridCentro[1]+self.tamanho+(self.tamanho/distSombra*1.5)), (self.gridCentro[0]-self.tamanho+(self.tamanho/distSombra), self.gridCentro[1]-self.tamanho+(self.tamanho/distSombra*1.5)), self.grossuraBordas)
            pygame.draw.line(var.TELA, self.corSombra, (self.gridCentro[0]-self.tamanho+(self.tamanho/distSombra), self.gridCentro[1]+self.tamanho+(self.tamanho/distSombra*1.5)), (self.gridCentro[0]+self.tamanho+(self.tamanho/distSombra), self.gridCentro[1]-self.tamanho+(self.tamanho/distSombra*1.5)), self.grossuraBordas)

