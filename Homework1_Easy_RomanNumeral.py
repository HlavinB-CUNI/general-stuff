class Solution:
    def romanToInt(self, s: str) -> int:
        s = s + " "

        # establishing array with placeholder 0's
        intArray = [0] * len(s)

        # creating the loop for the numerals
        for i in range(len(s)):
            if s[i] == "I":
                if s[i+1] == "V":
                    intArray[i] = -1
                else:
                    intArray[i] = 1
                    print(intArray)
            elif s[i] == "V":
                intArray[i] = 5
            elif s[i] == "X":
                if s[i+1] == "L":
                    intArray[i] = -10
                elif s[i+1] == "C":
                    intArray[i] = -10
                else:
                    intArray[i] = 10
            elif s[i] == "L":
                intArray[i] = 50
            elif s[i] == "C":
                if s[i+1] == "D":
                    intArray[i] = -100
                elif s[i+1] == "M":
                    intArray[i] = -100
                else:
                    intArray[i] = 100
            elif s[i] == "D":
                intArray[i] = 500
            elif s[i] == "M":
                intArray[i] = 1000
            else:
                continue
        
    
        return sum(intArray)


