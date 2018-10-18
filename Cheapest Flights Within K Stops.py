class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        # key:sorce, value {}: key: destination, value: cost 
        map = {}

        for i in flights:
            start = i[0]
            to = i[1]
            cost = i[2]

            if(start not in map):
                map[start] = {}
            map[start][to] = cost

        # pq: (cost, city, count)
        pq = [(0, src, 0)]

        while(len(pq) != 0):
            cost, city, count = heapq.heappop(pq)
            if(count > K + 1):
                continue
            if(city == dst):
                return cost
            if(city in map):
                next =  map[city]
                for nextCity in next:
                    heapq.heappush(pq, (cost + next[nextCity], nextCity, count + 1))

        return -1