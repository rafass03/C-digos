#1ª Avaliação de Estrutura de Dados e Algorítimos
#Aluno: Rafael Silva Santana

#Questão 3

import numpy as np

class Node:
    def __init__ (self, key):
        self.key = key
        self.next = None

    def NodeKey (self):
        return self.key
    
class Fila:
    def __init__ (self):
        self.first = None
        self.last = None
        self.size = 0
        self.maxsize = 0

    def empty_list (self):
        if self.first is None:
            return True
    
    def push (self, key):
        key = Node(key)
        if self.last is None:
            self.last = key
        else:
            self.last.next = key
            self.last = key
        if self.first is None:
            self.first = key
        self.size += 1
    
    def pop (self):
        if self.empty_list():
            return print(f'A fila já está vazia!')
        else:
            temp = self.first.key
            self.first = self.first.next
            self.size -= 1
            return print(temp)

    def peek (self):
        if self.empty_list():
            print(f'A fila está vazia!')
        else:
            return self.first.key
        
    def display (self):
        if self.empty_list():
            return
        else:
            temp = self.first
            while temp:
                print(f'{temp.NodeKey()}', end=" ")
                temp = temp.next

    def project (self, X, Y):
        self.maxsize = Y
        while X != 0:
            Z = np.array(input().split())
            if str(Z[0]) == "A":
                if self.size < self.maxsize:
                    self.push(str(Z[1]))
            elif str(Z[0]) == "M":
                self.maxsize = int(Z[1])
            elif str(Z[0]) == "F":
                for i in range (int(Z[1])):
                    self.pop()
            X -= 1
        return

def main():
    F = Fila()
    X, Y = np.fromstring(input(),dtype = int, sep= " ")
    F.project(X, Y)
main()