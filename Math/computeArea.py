class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x1 = max(ax1, bx1)
        x2 = min(ax2, bx2)
        y1 = max(ay1, by1)
        y2 = min(ay2, by2)
        def area(x1: int, y1: int, x2: int, y2: int) -> int:
            if (x2 - x1) < 0 or (y2 - y1) < 0:
                return 0
            return (x2 - x1) * (y2 - y1)
        A1_n_A2 = area(x1, y1, x2, y2)
        A1 = area(ax1, ay1, ax2, ay2)
        A2 = area(bx1, by1, bx2, by2)

        return A1 + A2 - A1_n_A2