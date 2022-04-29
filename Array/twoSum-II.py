class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        i = 0
        j = len(numbers) - 1
        while i < j:
            value = numbers[i] + numbers[j]
            if value == target:
                result.append(i+1)
                result.append(j+1)
                break
            elif value > target:
                j -= 1
                while (j >= 0 and numbers[j + 1] == numbers[j]):
                    j -= 1
            else:
                i += 1
                while (i < len(numbers) and numbers[i - 1] == numbers[i]):
                    i += 1
        return result