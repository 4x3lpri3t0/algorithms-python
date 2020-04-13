""" https://www.interviewcake.com/question/python3/mesh-message
* Given information about active users on the network, find the shortest route for a message from one user (the sender) to another (the recipient). Return a list of users that make up this route.

First, we do a breadth-first search of the user network starting from the sender.
Then, we use the results of our search to backtrack and find the shortest path.

TC: O(N + M)
SC: O(N)

Cases:
    1- There isn't a route from the sender to the recipient -> None
    2- Either start node or end node are not in graph -> Exception
"""
import unittest
from collections import deque


def reconstruct_path(previous_nodes, start_node, end_node):
    reversed_shortest_path = []

    # Start from the end of the path and work backwards
    current_node = end_node
    while current_node:
        reversed_shortest_path.append(current_node)
        current_node = previous_nodes[current_node]

    # Reverse our path to get the right order
    reversed_shortest_path.reverse()  # flip it around, in place
    return reversed_shortest_path  # no longer reversed


def get_path(graph, start_node, end_node):
    if start_node not in graph or end_node not in graph:
        raise Exception('Start or end node not in graph')

    # Find the shortest route in the network between the two users using BFS
    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)

    # Keep track of how we got to each node
    # We'll use this to reconstruct the shortest path at the end
    # We'll ALSO use this to keep track of which nodes we've already visited
    how_we_reached_nodes = {start_node: None}

    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()

        # Stop when we reach the end node (since it's BFS)
        if current_node == end_node:
            return reconstruct_path(how_we_reached_nodes, start_node, end_node)

        for neighbor in graph[current_node]:
            if neighbor not in how_we_reached_nodes:
                nodes_to_visit.append(neighbor)
                how_we_reached_nodes[neighbor] = current_node

    # There's NO path from start_node to end_node
    return None


class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)
