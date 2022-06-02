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