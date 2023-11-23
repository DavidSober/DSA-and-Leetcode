'''
# Storing the url patterns
- I used a hash set for the url_patterns in case I needed to access any particular url in constant time later. The generator function ties the url_patterns to the Solutions object. 
  Doing this allows the object to be repeatedly updated with new url patterns later on as needed.

# Register url method
- I started on the register_url method and realized I needed a way to check if a url was valid. The examples shown used a url without the scheme component. 
  So I decided to not include that in any of my solutions as well. 
- note: I could have used a python build in method to check if a string was a valid url. But I believe that would go against the goal of this 
  question as it would trivialize creating the 'register_url' method. 
- To make the is_valid_url method I started by looking at the examples and using them to find all the rules that could be broken. 
  Rules such as '/' must be the first character, two '/' must have a minimum distance of 1 between them, '*' had to be at the end etc. 
For checking allowed characters I used a hash set containing all allowed characters so that I could check if any char in the 'some_url' was not allowed in constant time complexity. 
- Time complexity is O(n) since there are only for loops and index methods with nothing nested.
- Space complexity is O(m) m being the number of ':' present in a url since I store the indexes of the colons in 'idx' to later 
  check if the colons had a min distance of 1 between them. 

# Match url method
- First I use the is_valid_url method to check if url_to_match is valid. Because if the input url is not valid it will not match any patterns
- I split the url to match by its '/' delimiter. I do the same for all patterns in the url_patterns hash map. 
  I store these patterns in a list of lists. So now we go from '/some/url/in/here' to ['some', 'url', 'in', 'here]. 
  I use these lists of components check if components match between url_to_match and pattern_urls at each iteration of a for loop further down.
- I realized that if the length of the pattern url does not match the length of the url_to_match then that pattern has no 
  chance of being a correct pattern. Thus I use list comprehension to eliminate any pattern whose length does not match the input
- I now loop through the remaining url patterns, the index 'i' represents the same component for both the url_to_match and url_pattern 
  because their lengths are now equal. This allows me to do a comparison on a component to component basis
- I create a temporary list called outputs. This list will store the outputs of the parameters and if the entire url matches 
  the pattern then the temporary list will be extended to the 'output_params' and returned. However if at a later iteration 
  we find a that a component does not match we will move on to the next pattern and the output loop gets reset. This prevents 
  output data from failed pattern matches from leaking into the 'output_params' variable
- if we get through the nested for loops and did not hit a return that means no patterns matched the url_to_match and thus 
  we return 0 and the empty output_params list
- Time compexity is O(n^2) where n is the number of components in the url_to_match input. This is due to the nested for loops 
  length n checking all possible length matching patterns against the url_to_match.
- Space complexity is O(n * m) where n is the number of components in the url_to_match input and m is the number of url 
  patterns that have the same length n. This is due to the pruning of the url patterns hash map into the list of lists representing 
  the patterns that match the input length n. This occurs in this line here: url_patterns_matches = [pattern for pattern in url_patterns_matches if len(pattern) == len(url_to_match_split)]

# Test Cases
- I considered as many combinations of ways to break both methods. Covering a range of scenarios for valid and invalid registrations, different types of matches, and various combinations of patterns.
'''

from typing import *
class Solution():
    def __init__(self, url_patterns: List[str]):
            # stores the pattern data 
            self.url_patterns = url_patterns

    def register_url(self, some_url) -> int:
        # checks if some_url is valid, if it is we register it (add it to url_patterns)
        # returns `1` if the URL was valid and successfully registered, `0` otherwise
        if self.is_valid_url(some_url) and some_url not in self.url_patterns:
            self.url_patterns.add(some_url)
            return 1
        return 0
   
    # helper function that checks to see if a url is valid before adding it to url_patterns
    def is_valid_url(self, some_url) -> int:
        # set uses constant time to check if an element exists we use this for checking later
        allowed_characters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*:")
        if some_url[0] != '/':  # '/' can only be at the start
            return 0
        elif some_url[-1] == '/':   # '/' cannot be the last element
            return 0
        elif any( not char for char in some_url.split('/')[1:]): # '//' is not valid
            return 0 
        elif '*' in some_url:  
            if some_url.index('*') != len(some_url) - 1: # '*' can only be at the end
                return 0
            if some_url[some_url.index('*') - 1] != '/': # '*' must come after a '/'
                return 0
        elif ':' in some_url:
            idx = []
            for i in range(len(some_url)): # we collect the indexes of ':' for later checks
                if some_url[i] == ':':
                    idx.append(i)
            for i in range(len(idx) - 1):
                if not idx[i + 1] - idx[i] > 1: # colons must have at least one char between them
                    return 0
            for i in idx:
                if some_url[i - 1] != '/': # ':' must come after a '/'
                    return 0 
        elif not all(char in allowed_characters for char in some_url): # checks if valid chars are allowed chars
            return 0    
        # passed all valid checks
        return 1
    
    # matches a url to a stored pattern url
    def match(self, url_to_match, output_params) -> Tuple[int, List]:
        # if url_to_match is not valid it will not match any pattern
        if self.is_valid_url(url_to_match) == 0:
            return 0
        # split url_to_match into a list of its components
        url_to_match_split = url_to_match.split('/')[1:]
        # split all url_patterns into a list of their components
        url_patterns_matches = [] # contains possible url patterns to match with input
        for pattern in url_patterns:
            url_patterns_matches.append(pattern.split('/')[1:])
         
        # finds URL pattern length and eleminates patterns whose length does not match length of url_to_match_split
        url_patterns_matches = [pattern for pattern in url_patterns_matches if len(pattern) == len(url_to_match_split)]

        # loops through all patterns and checks rules to see if the pattern matches the url_to_match
        for pattern_components in url_patterns_matches:
            # stores temporary parameters into outputs, if the url matches the pattern this will be the output
            outputs = [] 
            # loop through each component in url_to_match and current pattern to check for matching components
            for i in range(len(url_to_match_split)):
                # exact text match
                if pattern_components[i] == url_to_match_split[i]: 
                    continue
                # Wildcard match 
                if pattern_components[i] == '*' and i == len(url_to_match_split) - 1:
                    output_params.extend(outputs)
                    return 1, output_params
                # parameter match and last element    
                elif pattern_components[i][0] == ':' and i == len(url_to_match_split) - 1:
                    outputs.append(url_to_match_split[i]) # add the output
                    output_params.extend(outputs)
                    return 1, output_params
                # parameter match in middle of url
                elif pattern_components[i][0] == ':':
                    outputs.append(url_to_match_split[i])
                    continue
                # no match of any kind
                elif pattern_components[i] != url_to_match_split[i]:
                    break
        # no pattern matched the url_to_match thus we return 0
        return 0, []


# Test Cases

# Example given in question
url_patterns = { '/api/hardware/inputs', 
                '/api/hardware/actuators', 
                '/api/hardware/actuators/:id',
                '/api/hardware/*',
                '/modules/:mod/items/:item'}
A = Solution(url_patterns)

# tests for match method

# MATCH method tests
# exact match test
    # expected output (1, [])
# A.match('/api/hardware/inputs', [])

# test for a parameter and wildcard match
    # expected output (1, ['somecolon', 'coffee'])
# A.register_url('/modules/:id/items/:idagain/*')
# A.match('/modules/somecolon/items/coffee/wildcard', [])

# test for two parameters
#   expected output (1, ['somecolon', 'coffee'])
# A.match('/modules/somecolon/items/coffee', []) # somecolon and coffee are parameters here

# test wildcard match
#   expected output (1, [])
# A.match('/api/hardware/randomwildcardinput', []) 

# test no matching pattern
# expected output (0, [])
# A.match('/api/hardware/notcorrect/wild', [])

# REGISTRATION method tests

# test duplicate url registration 
#   expected output case fails returns 0 and does not add new url shows example url_patterns only
# print(A.register_url('/api/hardware/inputs')) 
# print(A.url_patterns)

# test parameterized url registration
#   expected output 1 and the new url inside of url_patterns
# print(A.register_url('/lolapi/helloWorld/ok/:idx')) 
# print(A.url_patterns)

# test double slashes 
#   expected output case fails returns 0 and does not add new url shows example url_patterns only
# print(A.register_url('/lolapi//helloWorld/ok/:idx/*')) 
# print(A.url_patterns)

# test adding both parameter and wildcard 
#   expected output 1 and the new url inside of url_patterns
# print(A.register_url('/lolapi/helloWorld/ok/:idx/*')) 
# print(A.url_patterns)