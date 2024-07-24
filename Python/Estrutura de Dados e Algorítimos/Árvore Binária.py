import numpy as np

class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

    def imprimirNo(self):
        return self.chave

class Arvore:
    def __init__(self):
        self.raiz = None 

    def inserirArvore(self, raiz, no):#não é o mais eficiente
        if self.raiz is None:
            self.raiz = no
        else:
            if raiz.chave >= no.chave:
                if raiz.esquerda:
                    self.inserirArvore(raiz.esquerda, no)
                else:
                    raiz.esquerda = no
            else:
                if raiz.direita:
                    self.inserirArvore(raiz.direita, no)
                else:
                    raiz.direita = no

    def imprimirPreOrdem(self, raiz):#pré-ordem
        if raiz:
            print(f'{raiz.chave}')
            self.imprimirPreOrdem(raiz.esquerda)
            self.imprimirPreOrdem(raiz.direita)

    def imprimirPosOrdem(self, raiz):#pós-ordem
        if raiz:
            self.imprimirPosOrdem(raiz.esquerda)
            self.imprimirPosOrdem(raiz.direita)
            print(f'{raiz.chave}')

    def imprimirEmOrdem(self, raiz):#em-ordem
        if raiz:
            self.imprimirEmOrdem(raiz.esquerda)
            print(f'{raiz.chave}')
            self.imprimirEmOrdem(raiz.direita)
            
def main():
    l = Arvore()
    l.inserirArvore(l.raiz, No(2))
    l.inserirArvore(l.raiz, No(5))
    l.inserirArvore(l.raiz, No(3))
    l.inserirArvore(l.raiz, No(4))
    l.inserirArvore(l.raiz, No(9))
    l.inserirArvore(l.raiz, No(8))
    l.imprimirPreOrdem(l.raiz)
    l.imprimirPosOrdem(l.raiz)
    l.imprimirEmOrdem(l.raiz)
main()