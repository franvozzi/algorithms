# Nodo de una lista doblemente enlazada
class Node:
    def __init__(self, data):
        self.data = data        # Valor del nodo
        self.prev = None        # Puntero al nodo anterior
        self.next = None        # Puntero al siguiente nodo

# Clase de la lista doblemente enlazada
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Cabeza (inicio) de la lista

    # Agrega un nodo al final de la lista
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Si la lista está vacía
            self.head = new_node
            return

        current = self.head
        while current.next:  # Recorremos hasta el último nodo
            current = current.next

        current.next = new_node  # El último nodo apunta al nuevo nodo
        new_node.prev = current  # El nuevo nodo apunta al anterior

    # Agrega un nodo al principio de la lista
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:  # Si la lista está vacía
            self.head = new_node
            return

        new_node.next = self.head  # El nuevo nodo apunta al actual primero
        self.head.prev = new_node  # El anterior primero apunta al nuevo nodo
        self.head = new_node       # El nuevo nodo se convierte en la cabeza

    # Elimina el primer nodo que contiene el valor 'key'
    def delete(self, key):
        current = self.head

        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next  # Si era la cabeza, actualizamos

                if current.next:
                    current.next.prev = current.prev
                return  # Eliminado, salimos
            current = current.next

    # Muestra los elementos de la lista hacia adelante
    def display_forward(self):
        elems = []
        current = self.head
        while current:
            elems.append(current.data)
            current = current.next
        return elems

    # Muestra los elementos de la lista hacia atrás
    def display_backward(self):
        elems = []
        current = self.head
        if not current:
            return elems

        # Ir al último nodo
        while current.next:
            current = current.next

        # Volver al inicio recogiendo los datos
        while current:
            elems.append(current.data)
            current = current.prev
        return elems
