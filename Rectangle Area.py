class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        total = abs(C - A) * abs(D - B) + abs(G - E) * abs(H - F)

        if(C <= E or G <= A):
            return total
        if(B >= H or F >= D):
            return total

        tmp_x = sorted([A, C, E, G])
        tmp_y = sorted([B, D, F, H])

        overlap = (tmp_y[2] - tmp_y[1]) * (tmp_x[2] - tmp_x[1])

        return total - overlap