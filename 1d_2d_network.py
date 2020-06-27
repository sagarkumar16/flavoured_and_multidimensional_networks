import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbs
import statistics
import random
import numpy as np

s = np.random.normal(0.5, 0.1, 1000)

def build_network_1D(N, 
                   s,
                   beta,
                   fitness_dist 
                   ):
    G = nx.Graph()
    G.add_node(0, fitness = random.choice(fitness_dist))
    G.add_node(1, fitness = random.choice(fitness_dist))
    G.add_edge(0,1)
    for source in range(N):
        G.add_node(source, fitness = random.choice(fitness_dist))
        zeta = sum([np.exp(-beta*dict(G.nodes())[i]['fitness'])*(1+s*(G.degree(i)-1)) for i in G.nodes])
        
        for i in G.nodes():
            if i != source:
                
                p = np.exp(-beta*dict(G.nodes())[i]['fitness'])*(1+s*(G.degree(i)-1))/zeta
                
                if random.random() <= p:
                    G.add_edge(source, i)
                    
                else:
                    pass
            else:
                pass
            
    return G


class triad:
    
    def __init__(self, name, face_1, face_2, face_3):
        self.name = name 
        self.face_1 = face_1
        self.face_2 = face_2
        self.face_3 = face_3



 class face:
    
    def __init__(self, G, source, target, energy_source, energy_target):
        
        G.add_node(source, energy = energy_source)
        G.add_node(target, energy = energy_target)
        G.add_edge(source, target)
        
        self.graph = G
        self.name = (source, target)
        self.node_1 = G[source]
        self.node_2 = G[target]
        self.neighbors = []
        
    def fitness(self):
        return dict(self.graph.nodes())[self.name[0]]['energy'] + dict(self.graph.nodes())[self.name[0]]['energy']
    
    def add_neighbor(self, node_num, node_energy, name):
        face_1 = face(self.graph, node_num, self.name[0], node_energy, 
                      dict(self.graph.nodes())[self.name[0]]['energy'])
        face_2 = face(self.graph, node_num, self.name[1], node_energy, 
                      dict(self.graph.nodes())[self.name[1]]['energy'])
        name = triad(name, self, face_1, face_2)
        
        self.neighbors.append(name)
        
        return face_1, face_2
        
    def degree(self):
        return len(self.neighbors)



def prob_coefficient(face, flavour, beta):
    return np.exp(-beta * face.fitness())*(1 + flavour*face.degree())

def build_edges_2d(n, lof, flavour, beta, energy_distribution, rand = random.random()):
    
    z = sum([prob_coefficient(i, flavour, beta) for i in lof])
    
    possible_edges = [i for i in lof if prob_coefficient(i, flavour, beta) >= rand]
    
    if len(possible_edges) > 0:
        a = random.choice(possible_edges).add_neighbor(n, random.choice(energy_distribution), n)
        
        lof.append(a[0])
        lof.append(a[1])
    else:
        build_edges_2d(lof, flavour, beta, energy_distribution)
        
    return possible_edges


def build_network_2D(N, flavour, beta, energy_distribution):
    
    G = nx.Graph()
    
    first_face = face(G, 0, 1, random.choice(energy_distribution), random.choice(energy_distribution))
    
    lof = [first_face]
    
    for n in range(2, N):
        build_edges_2d(n, lof, flavour, beta, energy_distribution)
    
    return G


def build_network(dim, N, flavour, beta, energy_distribution):
    
    if dim == 1:
        return build_network_1D(N, flavour, beta, energy_distribution)
    
    elif dim == 2: 
        return build_network_2D(N, flavour, beta, energy_distribution)
        
    else:
        print('That dimension is not yet supported :(')       