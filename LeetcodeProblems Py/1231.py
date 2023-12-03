# bin search in solution space hard problem
# after studying logic in first sol below i came up
# with a slighly differenty bin search sol 
# beats 95% in time and 44% in space

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        num_people = k + 1
        left = min(sweetness)
        right = sum(sweetness) // num_people

        while left <= right:
            mid = (left + right) // 2
            num_slices = 0
            tot = 0
            for i in sweetness:
                tot += i
                if tot >= mid:
                    tot = 0
                    num_slices += 1
            
            if num_slices < num_people:
                right = mid - 1
            else:
                left = mid + 1
        return right
    
# this is the editorial sol i used for informing my bin search

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        # Initialize the left and right boundaries.
        # left = 1 and right = (total sweetness) / (number of people).
        number_of_people = k + 1
        left = min(sweetness)
        right = sum(sweetness) // number_of_people
        
        while left < right:
            # Get the middle index between left and right boundary indexes.
            # cur_sweetness stands for the total sweetness for the current person.
            # people_with_chocolate stands for the number of people that have 
            # a piece of chocolate of sweetness greater than or equal to mid.  
            mid = (left + right + 1) // 2
            cur_sweetness = 0
            people_with_chocolate = 0
            
            # Start assigning chunks to the current person.
            for s in sweetness:
                cur_sweetness += s
                
                # If the total sweetness is no less than mid, this means we can break off
                # the current piece and move on to assigning chunks to the next person.
                if cur_sweetness >= mid:
                    people_with_chocolate += 1
                    cur_sweetness = 0

            if people_with_chocolate >= k + 1:
                left = mid
            else:
                right = mid - 1
                
        return right