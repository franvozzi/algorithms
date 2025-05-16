# Clase que representa un nodo en el árbol binario
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value          # Valor almacenado en el nodo
        self.left = None            # Referencia al hijo izquierdo
        self.right = None           # Referencia al hijo derecho
        self.parent = None          # Referencia al nodo padre

# Clase que implementa el árbol binario
class BinaryTree:
    def __init__(self):
        self.root = None            # Nodo raíz del árbol

    # Método para insertar un nuevo valor en el árbol
    def insert(self, value):
        if not self.root:
            self.root = BinaryTreeNode(value)
            return

        self._insert_recursive(self.root, value)

    # Método auxiliar recursivo para insertar
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BinaryTreeNode(value)
                node.left.parent = node
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = BinaryTreeNode(value)
                node.right.parent = node
            else:
                self._insert_recursive(node.right, value)

    # Método para buscar un valor en el árbol
    def search(self, value):
        return self._search_recursive(self.root, value)

    # Método auxiliar recursivo para buscar
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    # Método para eliminar un valor del árbol
    def delete(self, value):
        node = self.search(value)
        if node:
            self._delete_node(node)

    # Método auxiliar para eliminar un nodo
    def _delete_node(self, node):
        # Caso 1: Nodo sin hijos
        if node.left is None and node.right is None:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = None
                else:
                    node.parent.right = None
            else:
                self.root = None

        # Caso 2: Nodo con un solo hijo
        elif node.left is None:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent
            else:
                self.root = node.right
                self.root.parent = None

        elif node.right is None:
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
            else:
                self.root = node.left
                self.root.parent = None

        # Caso 3: Nodo con dos hijos
        else:
            successor = self._find_min(node.right)
            node.value = successor.value
            self._delete_node(successor)

    # Método para encontrar el valor mínimo en un subárbol
    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Método para recorrer el árbol en orden (in-order traversal)
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    # Método auxiliar recursivo para recorrido in-order
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    # Método para recorrer el árbol en pre-orden (pre-order traversal)
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    # Método auxiliar recursivo para recorrido pre-order
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    # Método para recorrer el árbol en post-orden (post-order traversal)
    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    # Método auxiliar recursivo para recorrido post-order
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    # Método para imprimir el árbol de forma visual
    def print_tree(self):
        if not self.root:
            print("Árbol vacío")
            return
        self._print_tree_recursive(self.root, "", True)

    # Método auxiliar recursivo para imprimir el árbol
    def _print_tree_recursive(self, node, prefix, is_left):
        if node:
            print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
            self._print_tree_recursive(node.left, prefix + ("    " if is_left else "│   "), True)
            self._print_tree_recursive(node.right, prefix + ("    " if is_left else "│   "), False)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un árbol binario
    tree = BinaryTree()
    
    # Insertar valores
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        tree.insert(value)
    
    # Imprimir el árbol
    print("Estructura del árbol:")
    tree.print_tree()
    
    # Realizar diferentes recorridos
    print("\nRecorrido en orden (in-order):", tree.inorder_traversal())
    print("Recorrido en pre-orden (pre-order):", tree.preorder_traversal())
    print("Recorrido en post-orden (post-order):", tree.postorder_traversal())
    
    # Buscar un valor
    search_value = 40
    result = tree.search(search_value)
    print(f"\nBúsqueda del valor {search_value}:", "Encontrado" if result else "No encontrado")
    
    # Eliminar un valor
    delete_value = 30
    print(f"\nEliminando el valor {delete_value}")
    tree.delete(delete_value)
    
    # Imprimir el árbol después de la eliminación
    print("\nEstructura del árbol después de la eliminación:")
    tree.print_tree()
