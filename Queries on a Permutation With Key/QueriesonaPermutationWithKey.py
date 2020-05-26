class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i for i in range(1, m+1)]
        output = []
        for i in range(len(queries)):
            output.append(P.index(queries[i]))
            P.insert(0, P.pop(P.index(queries[i])))
        return output
