from typing import List, Dict

class Node:
    """
    >>> Node(1, [Node(3), Node(2)]).to_adjacency_list()
    [[2, 3], [], []]
    >>> Node.from_adjacency_list([[2, 4], [1, 3], [2, 4], [1, 3]]).to_adjacency_list()
    [[2, 4], [1, 3], [2, 4], [1, 3]]
    """

    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    @staticmethod
    def from_adjacency_list(adjacency_list: List[List[int]]):
        nodes: Dict[int, 'Node'] = {}
        for node_val, neighbor_vals in enumerate(adjacency_list, start=1):
            if node_val not in nodes:
                nodes[node_val] = Node(node_val)
            node = nodes[node_val]
            for neighbor_value in neighbor_vals:
                if neighbor_value not in nodes:
                    nodes[neighbor_value] = Node(neighbor_value)
                neighbor = nodes[neighbor_value]
                node.neighbors.append(neighbor)
        return nodes[1]

    def to_adjacency_list(self) -> List[List[int]]:
        adj_dict: Dict[int, List[int]] = {}
        stack: List['Node'] = [self]
        size: int = 0
        while len(stack) > 0:
            node = stack.pop()
            if node.val in adj_dict:
                continue
            size = max(size, node.val)
            adj_dict[node.val] = []
            for neighbor in node.neighbors:
                adj_dict[node.val].append(neighbor.val)
                stack.append(neighbor)

        adj_list: List[List[int]] = [[]] * size
        for node_val, neighbors in adj_dict.items():
            adj_list[node_val - 1] = sorted(neighbors)
        return adj_list
