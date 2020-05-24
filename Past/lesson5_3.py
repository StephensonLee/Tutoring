def distanceBetweenBusStops(distance, start, destination):
    if start > destination: start, destination = destination, start  # Swap start and desination numbers
    pathA = distance[start:destination]
    pathB = distance[destination:] + distance[:start]
    return min(sum(pathA), sum(pathB))

test= [1,2,3,4,5]
print (sum(test))
print (distanceBetweenBusStops(test,0,3))