class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        sec_dic = {}
        gus_dic = {}
        for i in range(len(secret)):
            if(secret[i] == guess[i]):
                bulls += 1
            else:
                sec_dic[secret[i]] = sec_dic.get(secret[i], 0) + 1
                gus_dic[guess[i]] = gus_dic.get(guess[i], 0) + 1
        cows = 0
        for key in sec_dic:
            if(key in gus_dic):
                cows += min(sec_dic[key], gus_dic[key])
        res = str(bulls) + "A" + str(cows) + "B"

        return res