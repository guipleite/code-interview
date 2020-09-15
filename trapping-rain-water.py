class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        left_pointer = left

        right = len(height)-1
        right_pointer = right
        
        vol = 0

        while left_pointer < right_pointer :
            
            if height[left_pointer] <= height[right_pointer]:
                left_pointer+=1
                
                if height[left_pointer] <= height[left]:
                    vol+= abs(height[left_pointer]-height[left])
                    
                else:
                    left=left_pointer
                    
            else:
                right_pointer-=1
                
                if height[right_pointer] <= height[right]:
                    vol+= abs(height[right_pointer]-height[right])
                
                else:
                    right=right_pointer
                    
        return vol

                
            