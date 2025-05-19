class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if('.' in queryIP and ':' not in queryIP):
            splitIP = queryIP.split('.')
            if(len(splitIP) == 4):
                for i in range(len(splitIP)):
                    try:
                        if(int(splitIP[i]) < 0 or int(splitIP[i]) >= 256):
                            return "Neither"
                        if(int(splitIP[i][0]) == 0 and len(splitIP[i]) != 1):
                            return "Neither"
                    except:
                            return "Neither"
                return "IPv4"
        if(':' in queryIP and '.' not in queryIP):
            splitIP = queryIP.split(':')
            if(len(splitIP) == 8):
                for i in range(len(splitIP)):
                    if (len(splitIP[i]) > 4):
                            return "Neither"
                    try:
                        if(int(splitIP[i], 16) < 0 or int(splitIP[i], 16) >= 65536):
                            return "Neither"
                    except:
                            return "Neither"
                return "IPv6"
        return "Neither"
        







queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
#Output: "IPv4"
sol = Solution()
print(sol.validIPAddress(queryIP))
