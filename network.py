from math import *

from connection import *
from particle import *
from random import random

class Network :
    def __init__(self, nodes = 0, connections = [(0, 0)]) :
        self.nodes = nodes

        def createConnectionTable() :
            table = ConnectionTable(nodes)
            for c in range(len(connections)) :
                i = connections[c][0]
                j = connections[c][1]
                table.set(i, j, True)
            return table

        def createNodeList():
            nodeList = []
            for n in range(nodes):
                x = 200*random() - 100
                y = 200*random() - 100
                nodeList.append(Particle((x, y), (0, 0), (0, 0), 1))
            return nodeList

        self.connectionTable = createConnectionTable()
        self.particles = createNodeList()

    def __str__(self) :
        return ""

    def forceBetweenParticles(self, i = 0, j = 0) :
        A = self.particles[i]
        B = self.particles[j]
        
        rVector = B.position.sub(A.position)
        r = distanceBetweenParticles(A, B)
        rNormalized = rVector.divide(r)
        
        if self.connectionTable.connected(i, j) :
            connectionFactor = 1
        else :
            connectionFactor = 0

        mutualConnectionFactor = self.connectionTable.numberOfMutualConnections(i, j)
        attractionFactor = connectionFactor + mutualConnectionFactor
        
        if connectionFactor == 1:
            return rNormalized.multiply(0.2*(r - 100))
        elif mutualConnectionFactor > 0:
            return rNormalized.multiply(0.1*(r - 200))
        else:
            return rNormalized.multiply(-0.01)
        
    def forceOnParticle(self, i = 0) :
        totalForce = Vector2D(0, 0)

        for j in range(self.nodes) :
            if(i != j) :
                totalForce = totalForce.add(self.forceBetweenParticles(i, j))

        return totalForce

    def updatePositions(self) :
        for i in range(self.nodes) :
            self.particles[i].updatePosition()
    
    def updateForces(self) :
        for i in range(self.nodes) :
            self.particles[i].updateForce(self.forceOnParticle(i))

    def dampVelocities(self, factor = 1.) :
        for i in range(self.nodes) :
            v = self.particles[i].velocity
            self.particles[i].velocity = v.multiply(factor)

    def particlesConnected(self, i = 0, j = 0):
        return self.connectionTable.connected(i, j)

    def neighbourCount(self, i):
        return self.connectionTable.neighbourCount(i)



    








    
    
def test() :
    a = Particle((1., 1.), (0., 0.), (0., 0.))
    b = Particle((2., 2.), (0., 0.), (0., 0.))
    #print(b.position.sub(a.position))

    #print(distanceBetweenParticles(a, b))
    
    testConnections = [(0, 1), (0, 2), (0, 3), (1,2), (1,3), (2, 3), (4, 3), (5, 3)]
    testNetwork = Network(7, testConnections)

    for t in range(20) :
        print("T---------" + str(t))
        testNetwork.updateForces()
        testNetwork.updatePositions()
    
#test()
