class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Escape special regex characters in the pattern
        # Convert the wildcard pattern to regex pattern

        regex_pattern='^'  # Add start anchor
        i=0

        while i<len(p):
            if p[i]!="?" and p[i]!="*":
                # Escape special regex characters
                if p[i] in '.+()[]{}\\':
                    regex_pattern+='\\'
                regex_pattern+=p[i]
            elif p[i]=='?':
                regex_pattern+='.'
            else:
                # Optimize consecutive '*' characters
                while i+1<len(p) and p[i+1]=='*':
                    i+=1
                regex_pattern+='.*'
            i+=1
        
        regex_pattern+='$'  # Add end anchor
        # print(regex_pattern)
        
        # Compile the regex pattern once for better performance
        try:
            pattern = re.compile(regex_pattern)
            return bool(pattern.match(s))
        except re.error:
            return False