class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lstToStr = int("".join([str(i) for i in digits]))
        lstToStr = lstToStr + 1
        lstToStr = str(lstToStr)
        output = [int(j) for j in lstToStr]
        return output