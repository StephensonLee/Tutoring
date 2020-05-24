# def maxEnvelopes(self, es):
#     es.sort(key=lambda x: (x[0], -x[1]))
#     heights = [0x3f3f3f3f] * len(es)
#     for _, h in es:
#         heights[bisect.bisect_left(heights, h)] = h
#     return bisect.bisect_right(heights, 0x3f3f3f3f - 1)

import bisect

def maxEnvelopes(envelopes) -> int:
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    heights = []
    preW = -1
    print(envelopes)
    for width, height in envelopes:
        if width > preW and (len(heights) == 0 or height > heights[-1]):
            preW = width
            heights.append(height)
        else:
            idx = bisect.bisect_left(heights, height)
            heights[idx] = height
        print(heights)

    return len(heights)

input=[[2, 3], [4, 5], [6, 7], [7, 4],[8, 6],[9,6.5]]
print(maxEnvelopes(input))