"""Example runs with Little Ball of Fur."""

import networkx as nx

from littleballoffur.dataset import GraphReader
from littleballoffur.node_sampling import RandomNodeSampler, DegreeBasedSampler, PageRankBasedSampler
from littleballoffur.exploration_sampling import RandomWalkSampler, RandomNodeNeighborSampler, MetropolisHastingsRandomWalkSampler
from littleballoffur.exploration_sampling import RandomWalkWithRestartSampler, RandomWalkWithJumpSampler, FrontierSampler, ForestFireSampler
from littleballoffur.edge_sampling import RandomEdgeSampler, RandomNodeEdgeSampler, HybridNodeEdgeSampler, RandomEdgeSamplerWithInduction
 


reader = GraphReader("twitch")

graph = reader.get_graph()

#--------------------------
# Frontier Sampler Example
#--------------------------

sampler = FrontierSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#---------------------------
# ForestFire Sampler Example
#---------------------------

sampler = ForestFireSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#-----------------------------
# Random Walk Sampler Example
#-----------------------------

sampler = RandomWalkSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#-----------------------------
# Random Node Sampler Example
#-----------------------------

sampler = RandomNodeSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#-----------------------------
# Random Edge Sampler Example
#-----------------------------

sampler = RandomEdgeSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#--------------------------------------------
# Random Edge Sampler With Induction Example
#--------------------------------------------

sampler = RandomEdgeSamplerWithInduction()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#------------------------------
# Degree Based Sampler Example
#------------------------------

sampler = DegreeBasedSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#--------------------------------
# PageRank Based Sampler Example
#--------------------------------

sampler = PageRankBasedSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#----------------------------------
# Random Node Edge Sampler Example
#----------------------------------

sampler = RandomNodeEdgeSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#----------------------------------
# Hybrid Node Edge Sampler Example
#----------------------------------

sampler = HybridNodeEdgeSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#--------------------------------------
# Random Node Neighbor Sampler Example
#--------------------------------------

sampler = RandomNodeNeighborSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))


#------------------------------------------
# Random Walk With Restart Sampler Example
#------------------------------------------

sampler = RandomWalkWithRestartSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#-------------------------------
# Random Walk With Jump Example
#-------------------------------

sampler = RandomWalkWithJumpSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

#-----------------------------------------
# Metropolis Hastings Random Walk Example
#-----------------------------------------

sampler = MetropolisHastingsRandomWalkSampler()

new_graph = sampler.sample(graph)

print(nx.transitivity(new_graph))

