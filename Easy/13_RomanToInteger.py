
def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        i = 0
        while i < len(s):
            print(total)
            curr = s[i]
            
            if i != len(s)-1:
                next_two = s[i] + s[i+1]

                if next_two == "IV":
                    total += 4
                    i += 2
                    continue
                elif next_two == "IX":
                    total += 9
                    i += 2
                    continue
                elif next_two == "XL":
                    total += 40
                    i += 2
                    continue
                elif next_two == "XC":
                    total += 90
                    i += 2
                    continue
                elif next_two == "CD":
                    total += 400
                    i += 2
                    continue
                elif next_two == "CM":
                    total += 900
                    i += 2
                    continue
            
            if curr == "I":
                total += 1
                i += 1
            elif curr == "V":
                total += 5
                i += 1
            elif curr == "X":
                total += 10
                i += 1
            elif curr == "L":
                total += 50
                i += 1
            elif curr == "C":
                total += 100
                i += 1
            elif curr == "D":
                total += 500
                i += 1
            elif curr == "M":
                total += 1000
                i += 1
            
        return total
            


romanToInt("MCMXCIV")