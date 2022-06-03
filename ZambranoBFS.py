from queue import Queue

class Grafo:
    

    def __init__(self, numero_nodos, nodo_dirigido=True):
        """Creamos una funcion denominada init 
        El método __init__ es el primer método que se ejecuta cuando se crea un objeto.
        La función Self ofrece un modo de cálculo para hacer referencia al contenido del
        objeto con el que está asociado sin tener que hacer referencia explícitamente al objeto.
        Se envian por parametro la funcion self que en español significa yo, o uno mismo
        Se envia por parámetro a self, el numero de nodos y donde va el nodo dirigido con un
        valor boleano de verdadero.

        Args:
            numero_nodos ([tipo]): [descripcion]
            nodo_dirigido (bool, opcional): [descripcion]. Por defecto es verdadero.
        """        
        self.m_numero_nodos = numero_nodos #objeto del numero de nodos será igual al numero de nodos
        self.m_nodos = range(self.m_numero_nodos) #Le damos un rango al numero de nodos
		
        # Nodo dirigido o no dirigido
        self.m_nodo_dirigido = nodo_dirigido
		
        #Utilizamos un diccionario de datos para implementar un lista de adyacencia.       
        self.m_adj_lista = {node: set() for node in self.m_nodos} 
    
     # Añademos una arista al gráfico
        """Los arcos también son llamados aristas o líneas. Los nodos suelen usarse para
         representar objetos y los arcos para representar la relación entre ellos.
        """
    def agregar_borde(self, nodo1, nodo2, peso=1):
        """ 
            Agregamos un borde a los nodos
            se envian por parametro la funcion self que en español significa yo, o uno mismo
            El peso que se inicializa en 1 
        Args:
            node1 (_tipo_): _description_
            node2 (_tipo_): _description_
            pes (int, optional): _description_. Por defecto es 1.
        """
        #Agreamos el objeto self a la lsta adyacente y le agregamos el nodo y el peso
        self.m_adj_lista[nodo1].add((nodo2, peso)) 
        """_Sí no agramos un nodo dirigido, se agregará un segundo
        nodo a la lista adyacente y le agraomso el nodo 1 y el peso _
        """
        if not self.m_nodo_dirigido:

            self.m_adj_lista[nodo2].add((nodo1, peso))
    # Procedmos a imprimir la representacion gráfica del nodo
    def print_adj_lista(self):
        """_Creams una funcion para imprimir la lista adyacente y se
        enviar por parámetro a la función self_
        """
        #Creamos un ciclo for para cada valor de la variable iteradora.
        for llave in self.m_adj_lista.keys():
            #printeamos el nodo   y la lista adyacente con su llave 
            print("nodo", llave, ": ", self.m_adj_lista[llave])


    def bfs_traversal(self, nodo_empieza):
        """Funcion que va a imprimir a el recoorido,
        como parámetro el objetivo self y el estado inicial del nodo
        Args:
            start_node (_type_): _description_
        """
        # Conunto de nodos totalmente visitado, con el fin de evitar bucles
        visitado = set()
        queue = Queue() #permite crear y trabajar con colas de manera sencilla.
        # añadir el nodo_de_inicio a la cola y a la lista de visitas
        queue.put(nodo_empieza)
        visitado.add(nodo_empieza)
        while not queue.empty():
            #va aun vertice de cola y lo imprime
            nodo_actual = queue.get() #btiene el nodo actual
            print(nodo_actual, end = " ") #imprimire 
          # Obtener todos los vértices adyacentes del
            # vértice desencolado. Si un adyacente
            # no ha sido visitado, luego márcalo
            # visitado y ponerlo en cola
            for (next_node, weight) in self.m_adj_lista[nodo_actual]: #Obtener todos los vértices adyacentes del
                if next_node not in visitado: #Si un vértice adyacente no ha sido visitado, entonces márcalo
                    queue.put(next_node)
                    visitado.add(next_node) #visitarlo y agregarlo en cola
if __name__ == "__main__":
    
        #Instanciamos la clase grafo
        #Grafo no dirigido y se imprimirá con cinco nodos

    grafoImprime = Grafo(7, nodo_dirigido=False)


    # agregamos al grafo para que imprima
    grafoImprime.agregar_borde(0,3)
    grafoImprime.agregar_borde(0, 1)
    grafoImprime.agregar_borde(0, 2)
    grafoImprime.agregar_borde(2, 4)
    grafoImprime.agregar_borde(2, 5)
    grafoImprime.agregar_borde(5, 0)
    grafoImprime.agregar_borde(4, 6)
    # grafoImprime.agregar_borde(0, 2)
    # grafoImprime.agregar_borde(0, 3)
    # grafoImprime.agregar_borde(2, 4)
    # grafoImprime.agregar_borde(2, 5)
    # grafoImprime.agregar_borde(4, 6)
    # grafoImprime.agregar_borde(5, 0)
    

    # Imprime la lista de adyacencia en el formulario nodo n: {(nodo, peso)}
    grafoImprime.print_adj_lista()
    print ("Lo siguiente es la primera travesía de ancho"
                    "(empezando por el vértice 0))")
    grafoImprime.bfs_traversal(0)
    print()