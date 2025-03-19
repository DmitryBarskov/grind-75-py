from typing import List, Set

class Solution:
    """
    >>> Solution().canFinish(2, [[1,0]])
    True
    >>> Solution().canFinish(2, [[1,0],[0,1]])
    False
    """
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph: List[List[int]] = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        visited = [False] * numCourses
        for node in range(numCourses):
            if Solution._has_loop(graph, node, set(), visited):
                return False
        return True

    @staticmethod
    def _has_loop(
            graph: List[List[int]], current_node: int,
            path: Set[int], visited: List[bool]
    ) -> bool:
        if current_node in path:
            return True
        if visited[current_node]:
            return False

        path.add(current_node)
        for adjacent in graph[current_node]:
            if Solution._has_loop(graph, adjacent, path, visited):
                return True
        path.remove(current_node)

        visited[current_node] = True
        return False
