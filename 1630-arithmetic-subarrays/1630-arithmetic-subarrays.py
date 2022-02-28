class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        n = len(l)
        
        for i in range(n):
            length = r[i] - l[i] + 1
            
            min_element = min(nums[l[i]:r[i]+1])
            max_element = max(nums[l[i]:r[i]+1])
            '''
            we find the common difference of the AP using
            cd = (max_e - min_e) / len - 1
            
            '''
            if min_element == max_element:
                res.append(True)
            elif (max_element-min_element) % (length-1) != 0:
                res.append(False)
            else:
                check = [False]*length
                commonDiff = (max_element - min_element) / (length-1)
                count = 0
                for j in range(l[i],r[i]+1):
                    num = nums[j]
                    index = (num - min_element) / commonDiff
                    
                    '''
                    We check for negative cases
                    1. if index is not an integer then its not part of the AP
                    2. if the num - min_element is not divisible by cd then its not part of the AP
                    3. We use a boolean array to keep track of the visited numbers, if any number is repeated
                    then its not an AP
                    '''
                    if index != int(index):
                        break
                    
                    index = int(index)
                    
                    if (num - min_element) % commonDiff != 0  or check[index] == True:
                        break
                        
                    check[index] = True
                    count += 1
                    
                if count == length: res.append(True)
                else: res.append(False)
                
                
        
        return res