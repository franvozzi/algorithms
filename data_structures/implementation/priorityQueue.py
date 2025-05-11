class ColaPrioridad:
    """
    Implementación de una estructura de datos tipo Cola de Prioridad.
    Los elementos con mayor prioridad (valor numérico más bajo) salen primero.
    """
    
    def __init__(self):
        """
        Constructor que inicializa una cola de prioridad vacía
        """
        self.items = []  # Lista para almacenar tuplas (prioridad, elemento)
    
    def esta_vacia(self):
        """
        Verifica si la cola de prioridad está vacía
        Retorna: True si la cola está vacía, False en caso contrario
        """
        return len(self.items) == 0  # Retorna True si no hay elementos en la lista
    
    def encolar(self, item, prioridad):
        """
        Añade un elemento a la cola con su respectiva prioridad
        Parámetros:
            item: El elemento a añadir a la cola
            prioridad: Valor numérico que determina la prioridad (menor valor = mayor prioridad)
        """
        # Creamos una tupla con la prioridad y el elemento
        entrada = (prioridad, item)
        
        # Buscamos la posición correcta para insertar según la prioridad
        posicion = 0
        for i, (p, _) in enumerate(self.items):
            if p > prioridad:  # Encontramos donde insertar (ordenado por prioridad)
                posicion = i
                break
            else:
                posicion = i + 1
        
        # Insertamos en la posición correcta para mantener el orden
        self.items.insert(posicion, entrada)
    
    def desencolar(self):
        """
        Elimina y retorna el elemento con mayor prioridad (menor valor numérico)
        Retorna: El elemento con mayor prioridad
        Excepción: Levanta un IndexError si la cola está vacía
        """
        if self.esta_vacia():  # Verificamos si la cola está vacía
            raise IndexError("No se puede desencolar de una cola vacía")
        
        # Retornamos solo el elemento (segundo valor de la tupla)
        return self.items.pop(0)[1]  
    
    def ver_frente(self):
        """
        Retorna el elemento con mayor prioridad sin eliminarlo
        Retorna: El elemento con mayor prioridad
        Excepción: Levanta un IndexError si la cola está vacía
        """
        if self.esta_vacia():  # Verificamos si la cola está vacía
            raise IndexError("La cola está vacía")
        
        # Retornamos solo el elemento (segundo valor de la tupla)
        return self.items[0][1]  
    
    def tamano(self):
        """
        Retorna el número de elementos en la cola de prioridad
        Retorna: Cantidad de elementos en la cola
        """
        return len(self.items)  # Retornamos la longitud de la lista
    
    def __str__(self):
        """
        Método especial para convertir la cola de prioridad a una cadena de texto
        Retorna: Representación en texto de la cola de prioridad mostrando prioridad y valor
        """
        if self.esta_vacia():
            return "Cola de prioridad vacía"
        
        # Formateamos para mostrar prioridad y elemento
        resultado = "Cola de prioridad: ["
        for i, (prioridad, item) in enumerate(self.items):
            resultado += f"(prioridad:{prioridad}, valor:{item})"
            if i < len(self.items) - 1:
                resultado += ", "
        resultado += "]"
        return resultado


# Ejemplo de uso:
if __name__ == "__main__":
    # Creamos una nueva instancia de la cola de prioridad
    mi_cola = ColaPrioridad()
    
    # Verificamos si la cola está vacía (debería ser True)
    print("¿Está vacía la cola?", mi_cola.esta_vacia())
    
    # Añadimos algunos elementos con diferentes prioridades
    # Nota: Menor número = Mayor prioridad
    print("Encolando elementos con sus prioridades:")
    mi_cola.encolar("Tarea urgente", 1)
    mi_cola.encolar("Tarea normal", 3)
    mi_cola.encolar("Tarea importante", 2)
    mi_cola.encolar("Tarea muy urgente", 0)
    
    # Mostramos el estado actual de la cola
    print(mi_cola)
    
    # Mostramos el tamaño de la cola
    print("Tamaño de la cola:", mi_cola.tamano())
    
    # Vemos el elemento con mayor prioridad sin desencolarlo
    print("Elemento con mayor prioridad:", mi_cola.ver_frente())
    
    # Desencolamos y mostramos los elementos
    print("Desencolando:", mi_cola.desencolar())  # Debería ser "Tarea muy urgente"
    print("Desencolando:", mi_cola.desencolar())  # Debería ser "Tarea urgente"
    
    # Mostramos la cola actualizada
    print(mi_cola)
    
    # Añadimos un nuevo elemento
    mi_cola.encolar("Nueva tarea crítica", 1)
    print("Después de añadir 'Nueva tarea crítica' con prioridad 1:")
    print(mi_cola)
    
    # Desencolamos los elementos restantes
    print("Desencolando:", mi_cola.desencolar())  # Debería ser "Nueva tarea crítica"
    print("Desencolando:", mi_cola.desencolar())  # Debería ser "Tarea importante"
    print("Desencolando:", mi_cola.desencolar())  # Debería ser "Tarea normal"
    
    # Verificamos si la cola está vacía nuevamente
    print("¿Está vacía la cola?", mi_cola.esta_vacia())