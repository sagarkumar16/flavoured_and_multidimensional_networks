# flavoured_and_multidimensional_networks
Create networks with flavors {-1, 0, 1} in 1, 2, or 3 dimensional simplice using equations and descriptions found in the paper: Network geometry with flavor: from complexity to quantum geometry. 

A Networkx Graph is built using build_network(dimension, N, flavor, beta, energy_distribution).

dimension: The dimension of each simplex ({1,2,3}), as described in the paper. 

N: The number of nodes (int)

flavor: The flavor of the network ({-1, 0, 1}), as described in the paper. 

beta: The inverse temperature ([0, 1]) as described in the paper. 

energy_distribution: any numpy distribution (np.array)

NOTE: 3 dimensional simplices not yet available. 
NOTE: Currently, all networks are built with m = 1, i.e. each new simplex attaches to only one existing face

Resources:
Bianconi, G., & Rahmede, C. (2016). Network geometry with flavor: from complexity to quantum geometry. Physical Review E, 93(3), 032315.
