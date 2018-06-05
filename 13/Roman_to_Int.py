class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        switch={
            'I': self.funcI,
            'V': self.funcV,
            'X': self.funcX,
            'L': self.funcL,
            'C': self.funcC,
            'D': self.funcD,
            'M': self.funcM
        }
        
        roman_list = list(s)
        l = len(roman_list)
        i = 0
        arabic = 0
        while i < l:
            (i, arabic) = switch[roman_list[i]](roman_list, i, arabic)
        return arabic
        
    # given index and former sumed arabic,
    # return next index and sumed arabic
    def funcI(self, roman, i, arabic):
        if len(roman) == i+1:
            return (i+1, arabic+1)
        else:
            if roman[i+1] == 'V':
                i += 2
                arabic += 4
            elif roman[i+1] == 'X':
                i += 2
                arabic += 9
            else:
                i += 1
                arabic += 1
            return (i, arabic)

    def funcV(self, roman, i, arabic):
        i += 1
        arabic += 5
        return (i, arabic)

    def funcX(self, roman, i, arabic):
        if len(roman) == i+1:
            return (i+1, arabic+10)
        else:
            if roman[i+1] == 'L':
                i += 2
                arabic += 40
            elif roman[i+1] == 'C':
                i += 2
                arabic += 90
            else:
                i += 1
                arabic += 10
            return (i, arabic)

    def funcL(self, roman, i, arabic):
        i += 1
        arabic += 50
        return (i, arabic)

    def funcC(self, roman, i, arabic):
        if len(roman) == i+1:
            return (i+1, arabic+100)
        else:
            if roman[i+1] == 'D':
                i += 2
                arabic += 400
            elif roman[i+1] == 'M':
                i += 2
                arabic += 900
            else:
                i += 1
                arabic += 100
            return (i, arabic)

    def funcD(self, roman, i, arabic):
        i += 1
        arabic += 500
        return (i, arabic)

    def funcM(self, roman, i, arabic):
        i += 1
        arabic += 1000
        return (i, arabic)
