"""
@author: julesleprince
"""

import matplotlib.pyplot as plt
import random as rnd

class Simu:
    def __init__(self, nb_faces, nb_lancers, prudence):
        self.nb_faces = nb_faces
        self.nb_lancers = nb_lancers
        self.prudence = prudence
        self.data = {}
        
        
        
    def jeu(self):
        a = 1
        nb_lancers = self.nb_lancers
        
        while a >= self.prudence and nb_lancers > 0:
            d = rnd.randint(1, self.nb_faces)
            nb_lancers = nb_lancers - 1
            a = 1-(d/self.nb_faces)**nb_lancers
            
        return d
    
    
    def launch(self, n):
        results = [] # résultat des simulations
        
        for i in range(n):
            results.append(self.jeu())
                    
    
        total = 0 # Pour calculer la moyenne par la suite
        
        for ele in range(len(results)):
            total = total + results[ele]

        moyenne = total/n
        
        return moyenne
    
# parametres
nb_faces = 4
nb_lancers = 2
nb_simulations = 100000

graph = {}
graph['x'] = []
graph['y'] = []

for i in range(101):
    graph['x'].append(i/100)
    simu = Simu(nb_faces, nb_lancers, i/100)
    moyenne = simu.launch(nb_simulations)
    graph['y'].append(moyenne)


plt.plot(graph['x'], graph['y'])
plt.show()

