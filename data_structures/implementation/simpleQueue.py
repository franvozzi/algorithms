class Cola:
    """
    Implementación de una estructura de datos tipo Cola (Queue) que sigue
    el principio FIFO (First In, First Out)
    """
    
    def __init__(self):
        """
        Constructor que inicializa una cola vacía usando una lista
        """
        self.items = []  # Utilizamos una lista de Python para almacenar los elementos
    
    def esta_vacia(self):
        """
        Verifica si la cola está vacía
        Retorna: True si la cola está vacía, False en caso contrario
        """
        return len(self.items) == 0  # Retorna True si no hay elementos en la lista
    
    def encolar(self, item):
        """
        Añade un elemento al final de la cola
        Parámetro:
            item: El elemento a añadir a la cola
        """
        self.items.append(item)  # Usamos append para añadir al final de la lista
    
    def desencolar(self):
        """
        Elimina y retorna el primer elemento de la cola
        Retorna: El elemento del frente de la cola
        Excepción: Levanta un IndexError si la cola está vacía
        """
        if self.esta_vacia():  # Verificamos si la cola está vacía
            raise IndexError("No se puede desencolar de una cola vacía")
        return self.items.pop(0)  # Eliminamos y retornamos el primer elemento (índice 0)
    
    def ver_frente(self):
        """
        Retorna el elemento al frente de la cola sin eliminarlo
        Retorna: El elemento del frente de la cola
        Excepción: Levanta un IndexError si la cola está vacía
        """
        if self.esta_vacia():  # Verificamos si la cola está vacía
            raise IndexError("La cola está vacía")
        return self.items[0]  # Retornamos el primer elemento sin eliminarlo
    
    def tamano(self):
        """
        Retorna el número de elementos en la cola
        Retorna: Cantidad de elementos en la cola
        """
        return len(self.items)  # Retornamos la longitud de la lista
    
    def __str__(self):
        """
        Método especial para convertir la cola a una cadena de texto
        Retorna: Representación en texto de la cola
        """
        return str(self.items)  # Convertimos la lista a string para visualizar la cola


# Ejemplo de uso:
if __name__ == "__main__":
    # Creamos una nueva instancia de la cola
    mi_cola = Cola()
    
    # Verificamos si la cola está vacía (debería ser True)
    print("¿Está vacía la cola?", mi_cola.esta_vacia())
    
    # Añadimos algunos elementos a la cola
    print("Encolando elementos: 'Primero', 'Segundo', 'Tercero'")
    mi_cola.encolar("Primero")
    mi_cola.encolar("Segundo")
    mi_cola.encolar("Tercero")
    
    # Mostramos el estado actual de la cola
    print("Cola actual:", mi_cola)
    
    # Mostramos el tamaño de la cola
    print("Tamaño de la cola:", mi_cola.tamano())
    
    # Vemos el elemento al frente sin desencolarlo
    print("Elemento al frente:", mi_cola.ver_frente())
    
    # Desencolamos y mostramos los elementos
    print("Desencolando:", mi_cola.desencolar())
    print("Desencolando:", mi_cola.desencolar())
    
    # Mostramos la cola actualizada
    print("Cola después de desencolar dos elementos:", mi_cola)
    
    # Desencolamos el último elemento
    print("Desencolando el último elemento:", mi_cola.desencolar())
    
    # Verificamos si la cola está vacía nuevamente
    print("¿Está vacía la cola?", mi_cola.esta_vacia())