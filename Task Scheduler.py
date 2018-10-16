class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        record = [0] * 26
        mx = 0
        numberMx = 0

        for i in tasks:
            record[ord(i) - ord("A")] += 1
            if(record[ord(i) - ord("A")] == mx):
                numberMx += 1
            elif(record[ord(i) - ord("A")] > mx):
                mx = record[ord(i) - ord("A")]
                numberMx = 1

        partCnt = mx - 1
        partLen = n - (numberMx - 1)

        totalEmpty = partCnt * partLen

        taskLeft = len(tasks) - mx * numberMx

        idles = max(0, totalEmpty - taskLeft)

        return len(tasks) + idles