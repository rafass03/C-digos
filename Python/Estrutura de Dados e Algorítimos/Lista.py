#1ª Avaliação de Estrutura de Dados e Algorítimos
#Aluno: Rafael Silva Santana

#Questão 1

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
        if self.emptyList():
            print(f'A lista já está vazia!')
        else:
            self.head = None
            self.tail = None
    
    def insert (self, n, pos):
        temp = self.head
        Counter = 0
        n = Node(n)
        while temp and (Counter != pos-1):
            temp = temp.next
            Counter += 1
        n.next = temp.next
        temp.next = n
        self.size += 1

    def sum (self):
        if self.empty_list():
            print(f'A lista está vazia!')
        else:
            temp = self.head.next
            current = self.head.key
            current_global = self.head.key
            while temp:
                current = max(current + temp.key, temp.key)
                current_global = max(current_global, current)
                temp = temp.next
        print (current_global)

        
def main():
    L = Lista()
    n = int(input())
    x = np.fromstring(input(),dtype = int, sep= " ")
    for i in range(n):
        L.append(x[i])
    L.sum()
main()