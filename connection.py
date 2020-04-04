def listIntersection(A = [], B = []) :
    intersection = []
            
    for i in range(len(A)) :
        for j in range(len(B)) :
            if A[i] == B[j] :
                intersection.append(A[i])

    return intersection

class ConnectionTable :
    def __init__(self, size) :
        self.size = size
        self.table = [[False for i in range(size)] for j in range(size)]
        
    def __str__(self) :
        output = ""

        for i in range(self.size) :
            for j in range(self.size) :
                output += str(self.connected(i, j)) + " "
            output += "\n"

        return output

    def set(self, i, j, value) :
        if i != j :
            self.table[i][j] = value
            #ensures table symmetric
            self.table[j][i] = value
        else :
            #ensures diagonal is always false
            self.table[i][j] = False

    def connected(self, i = 0, j = 0) :
        return self.table[i][j]

    def neighbourCount(self, i = 0) :
        number = 0
        for j in range(self.size):
            if self.connected(i, j):
                number = number + 1
        return number

    def numberOfMutualConnections(self, A = 0, B = 0) :
        return len(self.mutualConnections(A, B))

    def mutualConnections(self, A = 0, B = 0) :
        AConnections = []
        BConnections = []

        for i in range(self.size) :
            if self.connected(A, i) :
                AConnections.append(i)
            if self.connected(B, i) :
                BConnections.append(i)

        return listIntersection(AConnections, BConnections)
    
def test() :
    a = ConnectionTable(5)
    #print(a)

    for i in range(a.size) :
        for j in range(a.size) :
            a.set(i, j, True)
        print(a)
        
    #a.set(0, 2, False)
    #print(a)
    #print("\n")
        
    A = [1, 2, 3, 4, 5, 6, 7]
    B = [3, 4, 1, 10, 2, 11, 6]
    print(listIntersection(A, B))
    
    print(a.numberOfMutualConnections(0, 1))
    
    #print(a.connected(3, 3))
    #print(a.connected(6, 7))
    #print(a.connected())
    #a.set(0, 0, True)
    #print(a.connected())
    #a.set(3, 3, 7)
    #print(a.connected(3, 3))
    #print(a.size)
        
