# Clase que representa un nodo en el árbol
class TreeNode:
    # Constructor del nodo que inicializa el valor y las referencias
    def __init__(self, value):
        self.value = value        # Valor almacenado en el nodo
        self.children = []        # Lista de nodos hijos
        self.parent = None        # Referencia al nodo padre

    # Método para agregar un nodo hijo
    def add_child(self, child_node):
        child_node.parent = self  # Establece el padre del nodo hijo
        self.children.append(child_node)  # Agrega el hijo a la lista de hijos

    # Método para remover un nodo hijo
    def remove_child(self, child_node):
        # Filtra la lista de hijos para remover el nodo especificado
        self.children = [child for child in self.children if child != child_node]
        child_node.parent = None  # Elimina la referencia al padre

    # Método para obtener el nivel del nodo en el árbol
    def get_level(self):
        level = 0
        p = self.parent
        # Cuenta cuántos niveles hay hasta la raíz
        while p:
            level += 1
            p = p.parent
        return level

    # Método para imprimir el árbol de forma visual
    def print_tree(self):
        # Crea el prefijo de espacios según el nivel del nodo
        prefix = ' ' * 4 * self.get_level()
        print(f"{prefix}{self.value}")  # Imprime el valor del nodo
        # Recursivamente imprime todos los hijos
        if self.children:
            for child in self.children:
                child.print_tree()

    # Método para buscar un nodo por su valor
    def find_node(self, value):
        # Si encuentra el valor, retorna el nodo actual
        if self.value == value:
            return self
        
        # Busca recursivamente en todos los hijos
        for child in self.children:
            found = child.find_node(value)
            if found:
                return found
        
        return None  # Retorna None si no encuentra el valor

    # Método para recorrer todo el árbol y obtener todos los nodos
    def traverse(self):
        nodes = [self]  # Comienza con el nodo actual
        # Agrega recursivamente todos los nodos hijos
        for child in self.children:
            nodes.extend(child.traverse())
        return nodes


# Ejemplo de uso del árbol
if __name__ == "__main__":
    # Crear el nodo raíz del árbol
    root = TreeNode("Electronics")
    
    # Crear y configurar la rama de laptops
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))
    
    # Crear y configurar la rama de celulares
    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))
    
    # Crear y configurar la rama de TVs
    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    
    # Agregar todas las ramas principales al nodo raíz
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    # Imprimir la estructura del árbol
    print("Tree structure:")
    root.print_tree()
    
    # Ejemplo de búsqueda de un nodo
    print("\nFinding 'iPhone':")
    node = root.find_node("iPhone")
    if node:
        print(f"Found node: {node.value}")
        print(f"Parent: {node.parent.value}")
    
    # Ejemplo de recorrido completo del árbol
    print("\nAll nodes in tree:")
    all_nodes = root.traverse()
    print([node.value for node in all_nodes])
