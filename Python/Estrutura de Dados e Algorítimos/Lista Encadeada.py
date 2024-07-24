#1ª Avaliação de Estrutura de Dados e Algorítimos
#Aluno: Rafael Silva Santana

#Questão 4

import numpy as np

class Node:
    def __init__ (self, key):
        self.key = key
        self.next = None

    def NodeKey (self):
        return self.key

class Lista:
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0

    def new_list (self):
        return Lista()

    def empty_list (self):
        if self.head is None:
            return True
    
    def append (self, key):
        key = Node(key)
        if self.empty_list():
            self.head = key
            self.tail = self.head
        else:
            self.tail.next = key
            self.tail = key
        self.size += 1   
        
    def display (self):
        if self.empty_list():
            print(f'A lista está vazia!')
        else:
            temp = self.head
            while temp:
                print(f'{temp.NodeKey()}', end=" ")
                temp = temp.next
    
    def remove (self, key):
        temp = self.head
        if self.empty_list():
            print(f'A lista está vazia!')
        elif self.head.key == key:
            self.head = self.head.next
            self.tail = self.head
        else:
            while temp.next.key != key:
                temp = temp.next        
            temp.next = temp.next.next  
        self.size -= 1

    def free_list (self):
        if self.emptyList() is True:
            print(f'A lista já está vazia!')
        else:
            self.head = None
            self.tail = None
    
    def insert (self, key, pos):
        key = Node(key)
        temp = self.head
        Counter = 0
        while temp and (Counter != pos-1):
            temp = temp.next
            Counter += 1
        key.next = temp.next
        temp.next = key
        self.size += 1

    def Interpol(self, LA, LB):
        temp = LB.head
        temp2 = LA.head
        tempback = 0
        buffer = 0
        Contador = 1
        Tamanho = LA.size + LB.size
        while Tamanho:
            if temp2 is not None and temp is not None:
                if temp2.key == Contador:
                    buffer = temp2.next
                    tempback = temp        
                    temp2.next = temp.next 
                    LA.head = buffer                       
                    temp.next = temp2
                    temp = temp2
                    temp2 = buffer
                    buffer = 0
                    Contador = 1
                elif temp2.key == 0 and tempback == 0:
                    buffer = temp2.next
                    tempback = temp2
                    LA.head = buffer
                    temp2.next = temp
                    LB.head = temp2
                    temp2 = buffer
                    buffer = 0
                    Contador = 1
                elif temp2.key == 0:
                    temp = tempback
                    buffer = temp2.next
                    temp2.next = temp.next
                    LA.head = buffer
                    temp.next = temp2
                    temp = temp2
                    temp2 = buffer
                    buffer = 0
                    Contador = 1
                elif temp2 == None:
                    print(f'Não é possível fazer a interpolação.')
                    return
                elif LA.size >= LB.size:
                    print(f'Não é possível fazer a interpolação.')
                    return
                else:
                    Contador += 1
                    temp = temp.next
            else:
                break
            Tamanho -= 1

def main():
    LA = Lista()
    LB = Lista()
    Tamanho_LA = int(input())
    A = np.fromstring(input(),dtype = int, sep= " ")
    Tamanho_LB = int(input())
    B = np.fromstring(input(),dtype = int, sep= " ")
    for i in range(Tamanho_LB):
        if (i < Tamanho_LA):
            LA.append(A[i])
        LB.append(B[i])
    LB.Interpol(LA, LB)
    LB.display()
main()