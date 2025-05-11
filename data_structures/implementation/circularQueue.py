class ColaCircular:
    """
    Implementación de una estructura de datos tipo Cola Circular
    con un tamaño fijo que reutiliza sus posiciones.
    """
    
    def __init__(self, capacidad):
        """
        Constructor que inicializa una cola circular con capacidad fija
        Parámetro:
            capacidad: Tamaño máximo de la cola circular
        """
        if capacidad <= 0:  # Validamos que la capacidad sea positiva
            raise ValueError("La capacidad debe ser un número positivo")
            
        self.capacidad = capacidad  # Capacidad máxima de la cola
        self.items = [None] * capacidad  # Creamos un arreglo de tamaño fijo inicializado con None
        self.frente = -1  # Puntero al frente de la cola (inicialmente -1 indicando cola vacía)
        self.final = -1  # Puntero al final de la cola (inicialmente -1 indicando cola vacía)
        self.tamano_actual = 0  # Contador de elementos en la cola
    
    def esta_vacia(self):
        """
        Verifica si la cola circular está vacía
        Retorna: True si la cola está vacía, False en caso contrario
        """
        return self.tamano_actual == 0  # La cola está vacía si no contiene elementos
    
    def esta_llena(self):
        """
        Verifica si la cola circular está llena
        Retorna: True si la cola está llena, False en caso contrario
        """
        return self.tamano_actual == self.capacidad  # La cola está llena si tiene tantos elementos como su capacidad
    
    def encolar(self, item):
        """
        Añade un elemento al final de la cola circular
        Parámetro:
            item: El elemento a añadir a la cola
        Excepción: Levanta un OverflowError si la cola está llena
        """
        if self.esta_llena():  # Verificamos si la cola está llena
            raise OverflowError("No se puede encolar: la cola circular está llena")
        
        # Si la cola está vacía, inicializamos ambos punteros
        if self.esta_vacia():
            self.frente = 0
            self.final = 0
        else:
            # Movemos el puntero final de forma circular (operador módulo para volver al inicio)
            self.final = (self.final + 1) % self.capacidad
        
        # Colocamos el elemento en la posición final
        self.items[self.final] = item
        self.tamano_actual += 1  # Aumentamos el contador de elementos
    
    def desencolar(self):
        """
        Elimina y retorna el elemento del frente de la cola circular
        Retorna: El elemento del frente de la cola
        Excepción: Levanta un IndexError si la cola está vacía
        """
        if self.esta_vacia():  # Verificamos si la cola está vacía
            raise IndexError("No se puede desencolar de una cola vacía")
        
        # Guardamos el elemento a retornar
        elemento = self.items[self.frente]
        
        # Marcamos la posición como vacía
        self.items[self.frente] = None
        
        # Si era el último elemento, reseteamos los punteros
        if self.frente == self.final:
            self.frente = -1
            self.final = -1
        else:
            # Movemos el puntero frente de forma circular
            self.frente = (self.frente + 1) % self.capacidad
        
        self.tamano_actual -= 1  # Disminuimos el contador de elementos
        return elemento  # Retornamos el elemento desencolado
    
    def ver_frente(self):
        """
        Retorna el elemento al frente de la cola circular sin eliminarlo
        Retorna: El elemento del frente de la cola
        Excepción: Levanta un IndexError si la cola está vacía
        """
        if self.esta_vacia():  # Verificamos si la cola está vacía
            raise IndexError("La cola está vacía")
        
        return self.items[self.frente]  # Retornamos el elemento sin eliminarlo
    
    def tamano(self):
        """
        Retorna el número de elementos actuales en la cola circular
        Retorna: Cantidad de elementos en la cola
        """
        return self.tamano_actual
    
    def __str__(self):
        """
        Método especial para convertir la cola circular a una cadena de texto
        Retorna: Representación en texto de la cola circular
        """
        if self.esta_vacia():
            return "Cola circular vacía"
        
        resultado = "Cola circular: ["
        
        # Si el frente está después del final, necesitamos dos recorridos
        if self.frente <= self.final:
            # Recorremos desde el frente hasta el final
            for i in range(self.frente, self.final + 1):
                resultado += str(self.items[i])
                if i < self.final:
                    resultado += ", "
        else:
            # Recorremos desde el frente hasta el final del arreglo
            for i in range(self.frente, self.capacidad):
                resultado += str(self.items[i])
                resultado += ", "
                
            # Recorremos desde el inicio del arreglo hasta el final de la cola
            for i in range(0, self.final + 1):
                resultado += str(self.items[i])
                if i < self.final:
                    resultado += ", "
        
        resultado += "]"
        return resultado


# Ejemplo de uso:
if __name__ == "__main__":
    # Creamos una nueva instancia de la cola circular con capacidad 5
    mi_cola = ColaCircular(5)
    
    # Verificamos si la cola está vacía (debería ser True)
    print("¿Está vacía la cola?", mi_cola.esta_vacia())
    
    # Añadimos algunos elementos a la cola
    print("Encolando elementos: A, B, C, D")
    mi_cola.encolar("A")
    mi_cola.encolar("B")
    mi_cola.encolar("C")
    mi_cola.encolar("D")
    
    # Mostramos el estado actual de la cola
    print(mi_cola)
    
    # Mostramos el tamaño de la cola
    print("Tamaño de la cola:", mi_cola.tamano())
    
    # Verificamos si la cola está llena (debería ser False)
    print("¿Está llena la cola?", mi_cola.esta_llena())
    
    # Vemos el elemento al frente sin desencolarlo
    print("Elemento al frente:", mi_cola.ver_frente())
    
    # Desencolamos y mostramos los elementos
    print("Desencolando:", mi_cola.desencolar())
    print("Desencolando:", mi_cola.desencolar())
    
    # Mostramos la cola actualizada
    print(mi_cola)
    
    # Demostramos el comportamiento circular añadiendo más elementos
    print("Encolando nuevos elementos: E, F, G")
    mi_cola.encolar("E")
    mi_cola.encolar("F")
    mi_cola.encolar("G")
    
    # Verificamos si la cola está llena ahora (debería ser True)
    print("¿Está llena la cola?", mi_cola.esta_llena())
    
    # Mostramos la cola circular completa
    print(mi_cola)
    
    # Intentamos encolar otro elemento (debería generar error)
    try:
        print("Intentando encolar H en una cola llena...")
        mi_cola.encolar("H")
    except OverflowError as e:
        print(f"Error capturado: {e}")
        
    # Desencolamos todos los elementos restantes
    print("Desencolando todos los elementos restantes...")
    while not mi_cola.esta_vacia():
        print("Desencolando:", mi_cola.desencolar())
        
    # Verificamos que la cola esté vacía nuevamente
    print("¿Está vacía la cola?", mi_cola.esta_vacia())