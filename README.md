# social-network-graph
Force-directed social network graph visualisation implemented in Python

![Example](/example.png)

## Description
A social network is modelled as a graph of nodes representing individuals, and a table of connections representing a social association. Each node is associated with a particle. The force between each pair of particles is essentially Hooke's law for a spring, but changes depending on the nature of the connections between the two:
* If the 2 nodes are directly connected, the force will have a relative strength factor of 2.
* If the 2 nodes are not connected, but have one or more mutual connections, the strength factor is 1.
* For nodes that have no direct or mutual connection, if required, a very slight force is applied to prevent the graph from 'spreading out' too far.

The radius of each the circle representing each node is relative to the number of connections it has. The simulation starts at 'high temperature' (particles are given a lot kinetic energy) and is gradually 'cooled' (the velocities decreased by a factor for every frame of simulation) until the graph becomes stationary.

## Running the code
This program uses the Pygame library (https://github.com/pygame/pygame).
