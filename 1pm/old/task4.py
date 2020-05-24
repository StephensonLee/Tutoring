# You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north,
# then x[1] metres to the west, x[2] metres to the south,
# x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.
# #
# # Write 1pm one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """

        if len(x) < 4:
            return False

        for pos in range(3, len(x)):
            if x[pos - 1] <= x[pos - 3] and x[pos] >= x[pos - 2]:  # general case
                return True
            if pos >= 4 and x[pos - 1] == x[pos - 3] and x[pos] + x[pos - 4] == x[pos - 2]:  # connected rectangle
                return True
            # connected L-shape
            if pos >= 5 and x[pos - 1] <= x[pos - 3] and x[pos - 3] <= x[pos - 1] + x[pos - 5] and x[pos] + x[
                pos - 4] >= x[pos - 2] and x[pos - 4] <= x[pos - 2]:
                return True

        return False