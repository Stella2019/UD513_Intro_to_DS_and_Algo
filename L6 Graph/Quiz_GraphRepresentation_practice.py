class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_found = None
        to_found = None
        
        for node in self.nodes:
            if node_from_val == node.value:
                from_found = node
            if node_to_val == node.value:
                to_found = node
                
        if from_found == None:
            from_found = Node(node_from_val)
            self.nodes.append(from_found)
            
        if to_found == None:
            to_found = Node(node_to_val)
            self.nodes.append(to_found)
            
        new_edge = Edge(new_edge_val, from_found, to_found)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        
        edge_list = []
        for edge in self.edges:
            
            edge_tuple = ( edge.value, edge.node_from.value , edge.node_to.value )
            edge_list.append( edge_tuple )
            
            
        return edge_list


    

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        
        adj_list = []
        
        max_element = max( self.nodes, key=lambda v: v.value )
        #print( max_element.value )
        #sorted_nodes = sorted( self.nodes, key=lambda v: v.value )
        
        for node_index in range(0, max_element.value+1):
            
            to_list = []
        
            node_with_index = [ x for x in self.nodes if x.value == node_index ]
        
            
            if len(node_with_index) == 0:
                # node with node_index not exist
                
                # print("not_found")
                adj_list.append( None )
                
            else:
                # node with node_index exists
                #print node_with_index[0].value
                n = node_with_index[0]
                
                
                for edge in n.edges:
                    
                    if edge.node_from.value == n.value:
                        
                        to_tuple = ( edge.node_to.value, edge.value)
                        to_list.append( to_tuple )
                    
               
                if len(to_list) == 0:
                    adj_list.append( None )
                else:
                    adj_list.append( to_list )
                
                
        return adj_list
    
    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        
        adj_matrix = []
        
        max_element = max( self.nodes, key=lambda v: v.value )
        total_node_size = max_element.value + 1
        # visit each node with index start from #0
        for node_index in range(0, max_element.value+1):
            
            node_with_index = [ x for x in self.nodes if x.value == node_index ]
            
            if len(node_with_index) == 0:
                node = None
            else:
                node = node_with_index[0]
            
            
            adj_row = [0] * total_node_size
            
            if node == None or len(node.edges) == 0:
                
                adj_matrix.append( adj_row )
                
            else:
                
                for edge in node.edges:
                    
                    if edge.node_from.value == node.value:
                        adj_row[ edge.node_to.value ] = edge.value
                        
                adj_matrix.append( adj_row )
                
            
            
        return adj_matrix

graph = Graph()
graph.insert_edge(100, 1, 2)
graph.insert_edge(101, 1, 3)
graph.insert_edge(102, 1, 4)
graph.insert_edge(103, 3, 4)
# Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
print( graph.get_edge_list() ) 
# Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
print( graph.get_adjacency_list() ) 
# Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
print( graph.get_adjacency_matrix() )