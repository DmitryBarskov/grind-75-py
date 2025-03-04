from graph_node import Node

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Dict, Optional, Set
from collections import deque

class Solution:
    """
    >>> Solution().cloneGraph(
    ...     Node.from_adjacency_list([[2, 4], [1, 3], [2, 4], [1, 3]])
    ... ).to_adjacency_list()
    [[2, 4], [1, 3], [2, 4], [1, 3]]
    >>> Solution().cloneGraph(
    ...     Node.from_adjacency_list([[]])
    ... ).to_adjacency_list()
    [[]]
    >>> Solution().cloneGraph(None) is None
    True
    """
    def cloneGraph(self, root: Optional['Node']) -> Optional['Node']:
        if root is None:
            return None
        clones: Dict[int, 'Node'] = {}
        fully_cloned: Set[int] = set()
        queue: deque = deque([root])
        while len(queue) > 0:
            original = queue.popleft()
            if original.val in fully_cloned:
                continue

            if original.val not in clones:
                clones[original.val] = Node(original.val)
            clone: 'Node' = clones[original.val]

            for neighbor in original.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val)
                clone.neighbors.append(clones[neighbor.val])
                queue.append(neighbor)
            fully_cloned.add(original.val)
        return clones[root.val]
