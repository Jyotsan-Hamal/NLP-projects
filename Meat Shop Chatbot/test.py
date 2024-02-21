def maxArea(height):
        left,right = 0,len(height)-1
        water_level = 0
        max_water = 0
        for i in range(len(height)):
            
            
            if height[left] < height[right]:
                
                water_level = height[left]*(right-left)
                if water_level>max_water:
                    max_water = water_level
                    
                left+=1
            elif height[right]<height[left]:
                water_level = height[right]*(right-left)
                if water_level>max_water:
                    max_water = water_level
                    
                    
                right-=1
            else:
                if height[right]==height[left]:
                    water_level = height[left]*(right-left)
                    if water_level>max_water:
                        max_water = water_level
                    right-=1
            

        return max_water
    
print(maxArea([1,3,2,5,25,24,5]))