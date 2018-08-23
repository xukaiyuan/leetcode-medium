class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        lti_dict = {}
        for i in tickets:
            if(i[0] in lti_dict):
                if(self.compare(i[1], lti_dict[i[0]])):
                    lti_dict[i[0]] = i[1]
            else:
                lti_dict[i[0]] = i[1]
        
        res = ["JFK"]
        while(len(lti_dict) != 0):
            res.append(lti_dict[res[-1]])
            del lti_dict[res[-2]]
        return res

    def compare(self, str1, str2):
        return str1 < str2