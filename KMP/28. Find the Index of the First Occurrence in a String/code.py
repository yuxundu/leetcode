class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        haystackLength = len(haystack)
        needleLength = len(needle)
       
        lps = [0] * needleLength
        point, i = 0, 1

        while i < needleLength:
            if needle[point] == needle[i]:
                lps[i] = point + 1
                point += 1
                i += 1
            else:
                if point != 0:
                    point = lps[point-1]
                else:
                    lps[i] = 0
                    i += 1
        i,j = 0,0
        while i < haystackLength:
            if haystack[i] == needle[j]:
               i += 1
               j += 1
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
            if j == needleLength:
                return i - needleLength
        return -1


        