from copy import copy, deepcopy

class Labyrinth:

    def __init__(self):
        textlines = self.read_file()

        self.matrix = [[x for x in y] for y in textlines]

        self.create_representation()

    def read_file(self):
        labyrinth = open('blatt3_environment.txt', 'r')
        ascii = labyrinth.readlines()

        for i, n in enumerate(ascii):
            k = n[:-1]
            ascii[i] = k
        return ascii


    def create_representation(self):
        node_matrix = deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for n in range(len(self.matrix[i])):
                if self.matrix[i][n] != 'x':
                    node_matrix[i][n] = Node()
                else:
                    node_matrix[i][n] = 'x'
        print(node_matrix)

    def connect_nodes(self, matrix):
        for i in range(len(self.matrix)):
            for n in range(len(self.matrix[i])):
                if self.matrix[i][n] != 'x':
                    matrix[i][n].find_neighbors()
                else:
                    matrix[i][n] = 'x'


class Node:
    def __init__(self, is_goal=False):

        self.goal = is_goal
        self.neighbors = []

    def find_neighbors(self, matrix, position):
        # (x, y)
        neighbors = []
        x = position[0]
        y = position[1]

        links = matrix[y][x-1]
        rechts = matrix[y][x+1]
        oben = matrix[y-1][x]
        unten = matrix[y+1][x]

        temp_neighbors = [links, rechts, oben, unten]

        self.neighbors = [i for i in temp_neighbors if i != 'x']

    def get_neighbors(self):
        return self.neighbors

    def is_goal(self):
        return self.goal

if __name__ == '__main__':
    maze = Labyrinth()
