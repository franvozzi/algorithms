# Definimos el nodo básico de la lista enlazada
class Node:
    def __init__(self, data):
        self.data = data  # El valor almacenado en el nodo
        self.next = None  # Puntero al siguiente nodo (inicialmente None)

# Definimos la clase de la lista enlazada simple
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # El primer nodo de la lista (cabeza)

    # Agrega un nuevo nodo al final de la lista
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Si la lista está vacía
            self.head = new_node
            return
        current = self.head
        while current.next:  # Recorremos hasta el último nodo
            current = current.next
        current.next = new_node  # Agregamos el nuevo nodo al final

    # Agrega un nuevo nodo al principio de la lista
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  # El nuevo nodo apunta al actual primero
        self.head = new_node  # El nuevo nodo se convierte en la cabeza

    # Elimina el primer nodo que contiene el valor 'key'
    def delete(self, key):
        current = self.head

        # Caso especial: el nodo a eliminar es el primero
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        # Buscamos el nodo a eliminar
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:  # No se encontró el valor
            return

        # Saltamos el nodo actual para eliminarlo
        prev.next = current.next
        current = None

    # Devuelve una lista de los valores en la lista enlazada
    def display(self):
        elems = []
        current = self.head
        while current:
            elems.append(current.data)
            current = current.next
        return elems
