# Might be some of the ugliest code i've written
def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_list = []

        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False

        for i in s:
            if i == "(" or i == "{" or i == "[":
                my_list.append(i)

            if i == ")" or i == "}" or i == "]":
                if i == ")":
                    try:
                        if my_list[len(my_list)-1] == "(":
                            my_list.pop()
                        else: 
                            return False
                    except:
                        return False

                elif i == "}":
                    try: 
                        if my_list[len(my_list)-1] == "{":
                            my_list.pop()
                        else: 
                            return False
                    except:
                        return False

                elif i == "]":
                    try:
                        if my_list[len(my_list)-1] == "[":
                            my_list.pop()
                        else: 
                            return False
                    except:
                        return False
 
        if len(my_list) == 0:
            return True
        else: 
            return False