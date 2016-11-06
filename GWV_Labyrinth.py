from copy import deepcopy


class Labyrinth:
    """
    Reads an ASCII-art representation of a search problem, converts it into a graph upon which
    to execute search algorithms.
    """
    #TODO too much functionality in one class. Separate Reading, Constructing, printing,...

    def __init__(self):
        textlines = self.read_file()

        self.input_matrix = [[char for char in row] for row in textlines]

        self.representation = self.create_representation()
        self.connect_nodes(self.representation)

    def read_file(self):
        """Read the textfile containing ASCII-characters and return as a String without linebreaks"""

        labyrinth = open('blatt3_environment.txt', 'r')
        ascii = labyrinth.readlines()

        for i, n in enumerate(ascii):
            k = n[:-1]
            ascii[i] = k
        return ascii

    def create_representation(self):
        """
        Create a 2D-Array containing either a Node-Object where necessary
        or an 'x' where no node is to be created (e.g. a wall). This Array
        sticks to the layout given by the textfile, meaning that adjacent
        characters in the textfile are adjacent Nodes in this array.
        """

        node_matrix = deepcopy(self.input_matrix)

        for rownumber, row in enumerate(self.input_matrix):
            for colnumber, val in enumerate(row):
                if val != 'x':
                    node_matrix[rownumber][colnumber] = Node()
                else:
                    node_matrix[rownumber][colnumber] = 'x'

        return node_matrix

    def connect_nodes(self, matrix):
        """
        Connect nodes which have been created before. Two nodes are connected
        if they are adjacent to each other in the 2D-Array (vertically or horizontally).
        :param matrix: 2D-Array containing the nodes / obstacle indicators
        """
        for rownumber, row in enumerate(self.input_matrix):
            for colnumber, val in enumerate(row):
                if self.input_matrix[rownumber][colnumber] != 'x':
                    matrix[rownumber][colnumber].find_neighbors(matrix, (colnumber, rownumber))
                else:
                    matrix[rownumber][colnumber] = 'x'

    def print_search_state(self):
        """Put out a human-readable representation of a search state"""
        ascii_rep = ''
        pass


class Node:
    """
    Nodes that can be connected to form a graph.
    """
    def __init__(self, is_goal=False):
        self.goal = is_goal
        self.neighbors = []

    def find_neighbors(self, matrix, position):
        """
        Find adjacent nodes and save them for later use. This effectively forms the connections between nodes.
        :param matrix: The 2D-Array containing the nodes / obstacle indicators
        :param position: the position of the current node in the Array
        """
        # (x, y)
        x = position[0]
        y = position[1]

        links = matrix[y][x - 1]
        rechts = matrix[y][x + 1]
        oben = matrix[y - 1][x]
        unten = matrix[y + 1][x]

        temp_neighbors = [links, rechts, oben, unten]

        self.neighbors = [i for i in temp_neighbors if i != 'x']

    def get_neighbors(self):
        """
        Getter for the Connections
        :return: List of neighbors
        """
        return self.neighbors

    def is_goal(self):
        """
        Is this node a goal?
        :return: True, if this node is a goal
        """
        return self.goal


if __name__ == '__main__':
    maze = Labyrinth()
