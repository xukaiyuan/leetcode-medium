class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        stopToBus = {}
        visited = set()
        res = 1
        if(S == T):
            return 0
        for i in range(len(routes)):
            for j in routes[i]:
                if(j not in stopToBus):
                    tmp = [i]
                    stopToBus[j] = tmp
                else:
                    tmp = stopToBus[j]
                    tmp.append(i)
                    stopToBus[j] = tmp


        queue = []
        for i in stopToBus[S]:
            queue.append(i)
            visited.add(i)

        while(len(queue) != 0):
            tmp_queue = []
            while(len(queue) != 0):
                cur = queue.pop(0)
                for i in routes[cur]:
                    if(i == T):
                        return res
                    for next in stopToBus[i]:
                        if(next not in visited):
                            tmp_queue.append(next)
                            visited.add(next)
            res += 1
            queue = tmp_queue


        return -1