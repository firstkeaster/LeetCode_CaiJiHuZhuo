class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_par={')':'(','}':'{',']':'['}
        set_par={'(','{','['}
        list_str=[]
        for i in s:
            if i in set_par:
                list_str.append(i)
            elif i in dict_par:
                if list_str == []:
                    return False
                elif dict_par[i] == list_str[-1]:
                    list_str.pop()
                else:
                    return False
            else:
                continue
                
        if list_str == []:
            return True
        else:
            return False
