import InterfaceGrafica.interfaceGrafica as gui
import Tabuleiro.tabuleiro as t

def main():

  tabuleiro = t.Tabuleiro()
  gui.connect_4(tabuleiro)

if __name__ == '__main__':
  main()