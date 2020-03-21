import numpy as np
import math
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

    def direction(self):
        self.dir = self.p1 - self.p2
        return (self.dir[0], self.dir[1])

def angle2point(goal, actual, last):
    """ Function that receive 3 points and calc the angle between then"""
    goal = np.array(goal)
    actual = np.array(actual)
    last = np.array(last)

    dir2obj = goal - actual
    direction = last - actual

    cos_a = (np.dot(dir2obj, direction)) / (np.linalg.norm(dir2obj) * np.linalg.norm(direction))
    angle = np.arccos(np.clip(cos_a, -1.0, 1.0)) 
    return round((angle*180)/np.pi, 2)


def angle2vector(vetor1, vetor2):


    cos_a = (np.dot(vetor1, vetor2)) / (np.linalg.norm(vetor1) * np.linalg.norm(vetor2))
    angle = np.arccos(np.clip(cos_a, -1.0, 1.0)) 
    return round(math.degrees(angle), 2)