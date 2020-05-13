class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        self.candies = candies
        self.extraCandies = extraCandies
        maxCandies = max(self.candies)
        result = []
        for i in range(len(self.candies)):
            if ((self.candies[i] + self.extraCandies) >= maxCandies):
                result.append(True)
            else:
                result.append(False)
        return result
