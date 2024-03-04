class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = defaultdict(list)
        # compute all distances 
        for xy in points:
            x = xy[0]
            y = xy[1]
            xSumSquared = (x - 0)**2
            ySumSquared = (y - 0)**2

            distanceBeforeSQRT = xSumSquared + ySumSquared
            distances[distanceBeforeSQRT].append(xy)
        # sort them
        dictKeys = list(distances.keys())
        dictKeys.sort()

        # take top k elements
        shortestInK = []
        for dist in dictKeys:
            print(dist)
            if len(shortestInK) < k:
                for coords in distances[dist]:
                    shortestInK.append(coords)
            else:
                break

        return shortestInK
        
