# hint kind of gave away the solution... all nodes in an acyclic graph can be
# reached by the set of nodes that have zero incoming edges. So just add all the
# verticies with no incoming edges to a list and that list is the answer.
# I suppose this is just one of those basic facts about graphs you either know or dont
# beats 100% in time! and 57% in space

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_edge_nodes = set()
        ans = []
        for x, y in edges:
            in_edge_nodes.add(y)
        for i in range(n):
            if i not in in_edge_nodes:
                ans.append(i)
        return ans