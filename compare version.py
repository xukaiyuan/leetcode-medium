class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        i = 0
        j = 0
        d1 = 0
        d2 = 0

        while(i < len(version1) or j < len(version2)):
            while(i < len(version1) and version1[i] != "."):
                d1 = d1 * 10 + int(version1[i])
                i += 1

            while(j < len(version2) and version2[j] != "."):
                d2 = d2 * 10 + int(version2[j])
                j += 1

            if(d1 > d2):
                return 1
            elif(d1 < d2):
                return -1
            d1 = 0
            d2 = 0
            i += 1
            j += 1

        return 0