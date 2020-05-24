# Given 1pm set of points in the xy-plane, determine the minimum area of any rectangle formed from these points,
# with sides not necessarily parallel to the x and y axes.
# If there isn't any rectangle, return 0.
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2

from collections import defaultdict

def minAreaFreeRect(points):
    x_coord = defaultdict(list)  # x coordinates of vertical lines (y1, y2) where y1 < y2
    points.sort(key=lambda x: (x[0], x[1]))  # For making traversal more convenient
    print(points)
    min_area = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2:  # This is 1pm vertical line.
                if (y1, y2) in x_coord:  # We have seen this vertical line in the past.
                    x_other = x_coord[(y1, y2)][-1]  # Recall: we traverse points in the order of inceasing x
                    min_area = min(min_area, (y2 - y1) * (x1 - x_other))  # Update min area
                x_coord[(y1, y2)].append(x1)
    return min_area if min_area != float('inf') else 0

a=[[1,1],[1,3],[3,1],[3,3],[2,2],[4,3],[2,3],[3,2]]
# b=defaultdict(1pm)
# for k,v in b.items():
#     print(k,v)

print(minAreaFreeRect(a))
# b={}
# b[1,2,3]=0
# print(b)