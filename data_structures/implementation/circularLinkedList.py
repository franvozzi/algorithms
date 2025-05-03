# Nodo para lista enlazada circular
class Node:
    def __init__(self, data):
        self.data = data  # Valor del nodo
        self.next = None  # Puntero al siguiente nodo

# Clase para lista enlazada circular
class CircularLinkedList:
    def __init__(self):
        self.head = None  # Inicio de la lista

    # Agrega un nodo al final de la lista
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head  # Apunta a sí mismo para formar el ciclo
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head  # Nuevo nodo apunta a la cabeza

    # Agrega un nodo al principio de la lista
    def prepend(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node  # El último nodo apunta al nuevo nodo
        new_node.next = self.head
        self.head = new_node  # Actualizamos la_
