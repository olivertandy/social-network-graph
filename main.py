import pygame
from math import *
from random import randint, random

from network import *

def randomNetwork(nodes = 0, connections = 0):
    connectionList = []
    for i in range(connections):
        connectionList.append((randint(0, nodes/2), randint(0, nodes/2)))

    for i in range(connections):
        connectionList.append((randint(nodes/2, nodes - 1), randint(nodes/2, nodes - 1)))

    for i in range(connections/10):
        connectionList.append((randint(nodes/2, nodes - 1), randint(0, nodes - 1)))
        
    return Network(nodes, connectionList)

testNetwork = randomNetwork(20, 20)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (100, 100, 100)

pygame.init()

w = 1024
h = 768
size = (w, h)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Social Network")

xCentre = w/2
yCentre = h/2

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    def drawLines():
        for i in range(testNetwork.nodes):
            for j in range(testNetwork.nodes):
                if testNetwork.particlesConnected(i, j):
                    x0 = xCentre + testNetwork.particles[i].position.x
                    y0 = yCentre + testNetwork.particles[i].position.y
                    x1 = xCentre + testNetwork.particles[j].position.x
                    y1 = yCentre + testNetwork.particles[j].position.y
                    pygame.draw.line(screen, GREY, [x0, y0], [x1, y1], 1)

    drawLines()
    
    for n in range(testNetwork.nodes):
        radius = 7*testNetwork.neighbourCount(n)
        x = xCentre + testNetwork.particles[n].position.x - radius/2
        y = yCentre + testNetwork.particles[n].position.y - radius/2
        if radius > 1:
            pygame.draw.ellipse(screen, WHITE, [x, y, radius, radius], 1)

    pygame.display.flip()

    testNetwork.updateForces()
    testNetwork.updatePositions()
    testNetwork.dampVelocities(0.3)
        
    clock.tick(25)

pygame.quit()
