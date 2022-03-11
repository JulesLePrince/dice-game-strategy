"""
@author: julesleprince
"""

import matplotlib.pyplot as plt

class Tree:
    def __init__(self, nb_faces, nb_lancers, prudence):
        self.nb_faces = nb_faces
        self.nb_lancers = nb_lancers
        self.prudence = prudence
        self.data = {}
        
        for i in range(1,self.nb_faces+1):
            self.data[i] = 0
    
    
    def make_tree(self, lancers, faces):
        
        # On enlève un lancer
        lancers = lancers - 1
        
        # On initialise le noeud
        node = {}
        
        # On crée faces branches au nouveau noeud
        for i in range(1,faces+1):
            
            # On calcul le pourcentage de chance d'avoir un meilleur score
            a = 1-(i/faces)**lancers
            
            
            # Si a est supérieur à tem et qu'il reste des lancers on rempli une nouvelle branche par recursion
            if a >= self.prudence and lancers != 0:
                node[i] = self.make_tree(lancers, faces)
                
            # Sinon on fini la branche et ajoute le dé de cette branche à data pour calculer l'espérance par la suite
            else:
                node[i] = "end"
                self.data[i] = self.data[i] + (1/self.nb_faces)**(self.nb_lancers - lancers)
        
        return node
    
    
    def esperance(self):
        self.esperance = 0
        
        for i in range(1,self.nb_faces+1):
            self.esperance += i*self.data[i]
            
        return self.esperance
        
    
    

# parametres
nb_faces = 4
nb_lancers = 2

graph = {}
graph['x'] = []
graph['y'] = []


for i in range(101):
    graph['x'].append(i/100)
    tree = Tree(nb_faces, nb_lancers, i/100)
    tree.make_tree(tree.nb_lancers, tree.nb_faces)
    graph['y'].append(tree.esperance())


plt.plot(graph['x'], graph['y'])

plt.show()





