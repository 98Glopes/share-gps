import numpy as np

class LinAlg2CV():

    def __init__(self, p1, p2):
        """ Vector for p1 to p2 = p2 - p1 """
        self.p1 = np.array(p1, dtype=int)
        self.p2 = np.array(p2, dtype=int)


    def dirVector(self):
        """ Return 2 tuples with cartesian points to opencv """
        self.dir = self.p1 - self.p2
        self.first_point = self.p1.copy()
        self.last_point = self.first_point + self.dir

        return (self.first_point[0], self.first_point[1]) , (self.last_point[0], self.last_point[1])


    def dir2obj(self):
        """ Return 2 tuples with cartesian points to opencv """
        self.dir = self.p1 - self.p2
        self.first_point = self.p1.copy()
        self.last_point = self.first_point - self.dir*0.5

        return (self.first_point[0], self.first_point[1]) , (int(self.last_point[0]), int(self.last_point[1])) 