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
    