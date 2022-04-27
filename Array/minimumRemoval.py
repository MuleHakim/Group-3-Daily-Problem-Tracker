class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        n = len(beans)
        beans = sorted(beans)
        total = sum(beans)
        output = total
        for i in range(n):
            curValue = total - (n - i) * beans[i]
            output = min(output, curValue)
        return output
    