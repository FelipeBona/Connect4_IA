class Tabuleiro:
  
  # A posição do grid deverá ser acessada da seguinte forma:
  # grid[linha][coluna]

  grid = list()

  larguraTabuleiro = 7
  alturaTabuleiro = 6
  
  def __init__(self):

    for i in range(self.alturaTabuleiro): 
      self.grid.append([])
      for _ in range(self.larguraTabuleiro):
        self.grid[i].append(0)
  
  def colocar_peca(self, coluna, tipoPeca):

    for linha in self.grid:
      if (linha[coluna]) == 0:
        linha[coluna] = tipoPeca
        return
      
    else:
      raise Exception("Não é mais possível colocar peças nessa coluna")
    
  