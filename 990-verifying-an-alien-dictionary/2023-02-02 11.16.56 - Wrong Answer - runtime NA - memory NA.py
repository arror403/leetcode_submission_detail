class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Python program to sort a string and return
        # its reverse string according to pattern string
        
        # This function will return the reverse of sorted string
        # according to the pattern
        
        def sortbyPattern(pat, str):
        
            priority = list(pat)
        
            # Create a dictionary to store priority of each character
            myDict = { priority[i] : i for i in range(len(priority))}
        
            str = list(str)
        
            # Pass lambda function as key in sort function
            str.sort( key = lambda ele : myDict[ele])
        
            # Reverse the string using reverse()
            str.reverse()
        
            new_str = ''.join(str)
            return new_str
        b=[]
        for i in words: b.append(sortbyPattern(order,i))
        print (b)
        return sorted(b)==b
