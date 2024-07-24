#1ª Avaliação de Estrutura de Dados e Algorítimos
#Aluno: Rafael Silva Santana

#Questão 2

import numpy as np

class Node:
    def __init__ (self, key):
        self.key = key
        self.next = None

    def NodeKey (self):
        return self.key

class Pilha:
    def __init__ (self):
        self.top = None
        self.size = 0

    def empty_list (self):
        if self.top is None:
            return True
    
    def push (self, key):
        key = Node(key)
        if self.empty_list():
            self.top = key
        else:
            key.next = self.top
            self.top = key
        self.size += 1   
    
    def pop (self):
        if self.empty_list():
            print(f'A pilha já está vazia!')
        else:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.key

    def peek(self):
        if self.empty_list():
            print(f'A pilha está vazia!')
        else:
            return self.top.key
        
    def display (self):
        if self.empty_list():
            print(f'A pilha está vazia!')
        else:
            temp = self.top
            while temp:
                print(f'{temp.NodeKey()}', end=" ")
                temp = temp.next
    
    def overflow(self, N, K):
        current = 1
        total = 0
        while N != 0:
            op = np.array(input().split())
            if str(op[0]) == "FOR":
                int(op[1])
                current = current * int(op[1])
                self.push(current)
            elif str(op[0]) == "ADD":
                total += self.top.key
            elif str(op[0]) == "END":
                self.pop()
                current = self.top.key
            N -= 1
        return total

def main():
    P = Pilha()
    P.push(1)
    N, K = np.fromstring(input(),dtype = int, sep= " ")
    total = P.overflow(N, K)
    if total <= K:
        print (total)
    else:
        print ("OVERFLOW")
main()