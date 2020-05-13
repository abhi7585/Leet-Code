class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        repeat = []
        tempArr = set(arr)
        tempArr = list(tempArr)
        flag = True
        for i in range(len(tempArr)):
            if arr.count(tempArr[i]) not in repeat:
                repeat.append(arr.count(tempArr[i]))
            else:
                flag = False
                break
        return flag
