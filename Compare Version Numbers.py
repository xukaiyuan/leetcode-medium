class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        index = -1
        for i in range(len(version1)):
            if(version1[i] != "0"):
                index = i
                break
        if(index != -1 and version1[index] != "."):
            version1 = version1[index:]
        
        index = -1
        for i in range(len(version2)):
            if(version2[i] != "0"):
                index = i
                break
        if(index != -1 and version2[index] != "."):
            version2 = version2[index:]

        len1 = len(version1)
        len2 = len(version2)
        tmp1 = version1.split(".")
        tmp2 = version2.split(".")
        padding = int((max(len(tmp1), len(tmp2)) - min(len(tmp1), len(tmp2))))
        
        
        
        def pad(str, padding):
            for i in range(padding):
                str += ".0"
            return str

        if(len1 > len2):
            version2 = pad(version2, padding)
        elif(len1 < len2):
            version1 = pad(version1, padding)
        
        tmp1 = version1.split(".")
        tmp2 = version2.split(".")
        

        equal = 1
        for i in range(len(tmp1)):           
            if(int(tmp1[i]) == int(tmp2[i])):
                continue
            elif(int(tmp1[i]) < int(tmp2[i])):
                equal = -1
                break
            else:
                equal = 0
                break
        if(equal == 1):
            return 0
        elif(equal == 0):
            return 1
        else:
            return -1
                
            

